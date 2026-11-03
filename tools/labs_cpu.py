#!/usr/bin/env python3
"""Six bounded CPU-only teaching labs. Python >=3.9, standard library only.

No network, GPU access, subprocess, external data, or persistent writes.
Inputs are tiny original fixtures, never real hardware measurements.
Run --test for regression tests; run all or a lab number to show results.
"""
import argparse
import csv
import io
import json
import math
import platform
import statistics
import sys
import unittest

LAB_NAMES = ('training', 'memory_budget', 'pipeline', 'allreduce', 'telemetry', 'placement')

def training():
    """Fit y=w*x by real CPU gradient descent, then infer without updates."""
    samples = [(1.0, 2.0), (2.0, 4.0), (3.0, 6.0)]
    weight = 0.0
    initial = statistics.mean((weight * x - y) ** 2 for x, y in samples)
    for _ in range(200):
        gradient = statistics.mean(2 * x * (weight * x - y) for x, y in samples)
        weight -= 0.05 * gradient
    before = weight
    prediction = weight * 4.0
    return {'initial_mse': initial,
            'final_mse': statistics.mean((weight * x - y) ** 2 for x, y in samples),
            'prediction_x4': prediction,
            'parameters_before_inference': before,
            'parameters_after_inference': weight}


def memory_budget(parameters=1_000_000_000, bytes_per_parameter=2, extra_gib=2, margin=0.2):
    """Toy weights + explicit workspace + proportional margin. Not a GPU allocator."""
    if not all(math.isfinite(value) for value in (parameters, bytes_per_parameter, extra_gib, margin)):
        raise ValueError('finite numeric inputs required')
    if parameters <= 0 or bytes_per_parameter <= 0 or extra_gib < 0 or margin < 0:
        raise ValueError('positive parameters/byte width; nonnegative workspace/margin required')
    weight_bytes = parameters * bytes_per_parameter
    weight_gib = weight_bytes / (1024 ** 3)
    return {'weight_bytes': weight_bytes, 'weight_gib': weight_gib,
            'workspace_gib': extra_gib, 'margin_fraction': margin,
            'total_gib': (weight_gib + extra_gib) * (1 + margin)}


def pipeline(stages_ms=(50, 20, 10)):
    """Deterministic service-time model: no actual accelerator/IO timings."""
    if len(stages_ms) != 3 or any(not math.isfinite(t) or t <= 0 for t in stages_ms):
        raise ValueError('three finite strictly positive stage times required')
    longest = max(stages_ms)
    bottleneck = ('storage', 'preprocessing', 'compute')[stages_ms.index(longest)]
    if sum(t == longest for t in stages_ms) > 1:
        bottleneck = 'tie'
    return {'stage_ms': list(stages_ms), 'serial_batches_s': 1000 / sum(stages_ms),
            'overlap_ideal_batches_s': 1000 / longest, 'bottleneck': bottleneck}


def allreduce(vectors=((1.0, 2.0), (3.0, 4.0))):
    """Local list arithmetic illustrates equal-weight reduction + distribution."""
    if not vectors or not vectors[0] or any(len(v) != len(vectors[0]) for v in vectors):
        raise ValueError('nonempty vectors of equal positive length required')
    summed = [sum(column) for column in zip(*vectors)]
    averaged = [value / len(vectors) for value in summed]
    return {'sum': summed, 'mean': averaged,
            'replicas': [averaged.copy() for _ in vectors]}


def telemetry(text='uuid,util_pct,used_mib\ngpu-A,30,1000\ngpu-A,50,1200\ngpu-B,N/A,500\n'):
    """Parse a deliberately synthetic CSV schema, retaining unsupported samples."""
    grouped = {}
    for row in csv.DictReader(io.StringIO(text)):
        values = []
        for key in ('util_pct', 'used_mib'):
            value = None if row[key] == 'N/A' else float(row[key])
            if value is not None and (not math.isfinite(value) or value < 0):
                raise ValueError('finite nonnegative telemetry required')
            values.append(value)
        util, memory = values
        if util is not None and util > 100:
            raise ValueError('utilization must be at most 100 percent')
        group = grouped.setdefault(row['uuid'], {'util': [], 'mem': [], 'missing': 0})
        if util is None:
            group['missing'] += 1
        else:
            group['util'].append(util)
        if memory is not None:
            group['mem'].append(memory)
    return {gpu: {'mean_util_pct': statistics.mean(g['util']) if g['util'] else None,
                  'peak_used_mib': max(g['mem']) if g['mem'] else None,
                  'missing_util_samples': g['missing']}
            for gpu, g in sorted(grouped.items())}


def placement(jobs=(('A', 1, 6), ('B', 1, 6), ('C', 1, 4), ('D', 1, 2))):
    """One-pass first-fit placement over two fictitious nodes, not Slurm/K8s."""
    nodes = [{'slots': 2, 'memory_gib': 8}, {'slots': 2, 'memory_gib': 8}]
    assigned, pending, seen = {}, [], set()
    for name, slots, memory in jobs:
        if name in seen or slots <= 0 or memory <= 0:
            raise ValueError('unique job names and positive requirements required')
        seen.add(name)
        for index, node in enumerate(nodes):
            if node['slots'] >= slots and node['memory_gib'] >= memory:
                node['slots'] -= slots
                node['memory_gib'] -= memory
                assigned[name] = index
                break
        else:
            pending.append(name)
    return {'assigned': assigned, 'pending': pending, 'remaining': nodes}


# LAB_IMPLEMENTATIONS

class LabTests(unittest.TestCase):
    def test_training(self):
        self.assertTrue(callable(globals().get('training')), 'training is not implemented')
        result = training()
        self.assertLess(result['final_mse'], 1e-10)
        self.assertAlmostEqual(result['prediction_x4'], 8.0, places=5)
        self.assertGreater(result['initial_mse'], result['final_mse'])
        self.assertEqual(result['parameters_before_inference'], result['parameters_after_inference'])

    def test_memory_budget(self):
        self.assertTrue(callable(globals().get('memory_budget')), 'memory_budget is not implemented')
        r = memory_budget()
        self.assertEqual(r['weight_bytes'], 2000000000)
        self.assertAlmostEqual(r['weight_gib'], 2000000000 / (1024 ** 3))
        self.assertAlmostEqual(r['total_gib'], (2000000000 / (1024 ** 3) + 2) * 1.2)
        self.assertLess(r['total_gib'], 8)
        with self.assertRaises(ValueError):
            memory_budget(parameters=-1)
        with self.assertRaises(ValueError):
            memory_budget(bytes_per_parameter=0)

    def test_pipeline(self):
        self.assertTrue(callable(globals().get('pipeline')), 'pipeline is not implemented')
        r = pipeline()
        self.assertEqual(r['serial_batches_s'], 12.5)
        self.assertEqual(r['overlap_ideal_batches_s'], 20.0)
        self.assertEqual(r['bottleneck'], 'storage')
        self.assertEqual(pipeline((10, 10, 10))['bottleneck'], 'tie')
        with self.assertRaises(ValueError):
            pipeline((0, 10, 20))

    def test_allreduce(self):
        self.assertTrue(callable(globals().get('allreduce')), 'allreduce is not implemented')
        r = allreduce()
        self.assertEqual(r['sum'], [4.0, 6.0])
        self.assertEqual(r['mean'], [2.0, 3.0])
        self.assertEqual(r['replicas'], [[2.0, 3.0], [2.0, 3.0]])
        with self.assertRaises(ValueError):
            allreduce([])
        with self.assertRaises(ValueError):
            allreduce([[1], [2, 3]])
        with self.assertRaises(ValueError):
            allreduce([[]])

    def test_telemetry(self):
        self.assertTrue(callable(globals().get('telemetry')), 'telemetry is not implemented')
        r = telemetry()
        self.assertEqual(r['gpu-A']['mean_util_pct'], 40.0)
        self.assertEqual(r['gpu-A']['peak_used_mib'], 1200.0)
        self.assertIsNone(r['gpu-B']['mean_util_pct'])
        self.assertEqual(r['gpu-B']['missing_util_samples'], 1)
        self.assertEqual(telemetry('uuid,util_pct,used_mib\n'), {})
        with self.assertRaises(ValueError):
            telemetry('uuid,util_pct,used_mib\nx,nan,100\n')
        with self.assertRaises(ValueError):
            telemetry('uuid,util_pct,used_mib\nx,101,100\n')

    def test_placement(self):
        self.assertTrue(callable(globals().get('placement')), 'placement is not implemented')
        r = placement()
        self.assertEqual(r['assigned'], {'A': 0, 'B': 1, 'D': 0})
        self.assertEqual(r['pending'], ['C'])
        self.assertEqual(r['remaining'], [{'slots': 0, 'memory_gib': 0}, {'slots': 1, 'memory_gib': 2}])
        self.assertEqual(placement(jobs=())['pending'], [])
        with self.assertRaises(ValueError):
            placement(jobs=(('X', -1, 2),))
        with self.assertRaises(ValueError):
            placement(jobs=(('X', 1, 2), ('X', 1, 2)))

    # NEXT_TEST

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lab', nargs='?', default='all', choices=['all'] + [str(i) for i in range(1, 7)])
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    if args.test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(LabTests)
        outcome = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
        sys.exit(0 if outcome.wasSuccessful() else 1)
    print('Python ' + platform.python_version() + ' | CPU-only stdlib | synthetic fixtures')
    for number, name in enumerate(LAB_NAMES, 1):
        if args.lab in ('all', str(number)):
            print('LAB ' + str(number) + ' ' + name)
            print(json.dumps(globals()[name](), ensure_ascii=False, sort_keys=True))
