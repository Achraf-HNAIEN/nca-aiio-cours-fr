"""Regression gates for the integrated course and editable CPU labs."""
from pathlib import Path
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from labs_cpu import memory_budget, pipeline
from quiz import load_bank

@pytest.mark.parametrize('kwargs', [
    {'parameters': float('nan')}, {'parameters': float('inf')},
    {'bytes_per_parameter': float('nan')}, {'extra_gib': float('inf')},
    {'margin': float('nan')}, {'margin': float('inf')},
])
def test_memory_budget_rejects_nonfinite_inputs(kwargs):
    with pytest.raises(ValueError):
        memory_budget(**kwargs)

@pytest.mark.parametrize('stages', [
    (50, float('nan'), 10), (50, float('inf'), 10),
    (float('-inf'), 20, 10),
])
def test_pipeline_rejects_nonfinite_inputs(stages):
    with pytest.raises(ValueError):
        pipeline(stages)

@pytest.mark.parametrize('domain', ['infrastructure', 'operations'])
@pytest.mark.parametrize('exam', ['A', 'B'])
def test_real_bank_has_no_repeating_four_answer_cycle(domain, exam):
    bank, _ = load_bank(ROOT)
    letters = ''.join(q['answer'] for q in bank if q['domain'] == domain and q['exam'] == exam)
    assert len(letters) > 4
    assert not all(letter == letters[i % 4] for i, letter in enumerate(letters))

def test_public_source_excerpts_are_short_and_have_no_private_paths():
    raw = (ROOT / 'sources/ledger.json').read_text(encoding='utf-8')
    assert '/home/' not in raw
    for source in json.loads(raw)['sources']:
        assert sum(len(q['text'].split()) for q in source.get('quotes', [])) <= 200

def test_real_bank_sources_have_evidence():
    bank, sources = load_bank(ROOT)
    assert len(bank) == 100
    assert all(sources[sid].get('quotes') for q in bank for sid in q['source_ids'])
