# 06 — Datacenter, énergie, refroidissement et dimensionnement

**Objectifs locaux : I03, I04, I06 ; liens avec I01, I02 et I05.** Vous apprendrez à séparer charge informatique et charge du site, à raisonner sur l'installation réelle et à comparer des modes d'hébergement. Les calculs sont des exemples pédagogiques avec hypothèses explicites, pas des études électriques ou thermiques permettant d'autoriser une installation.

<a id="i06"></a>
## I06 — Une place libre dans un rack n'est pas une capacité disponible

Un serveur accéléré doit entrer dans le rack, être supporté mécaniquement, recevoir l'alimentation adaptée et évacuer sa chaleur. Il faut également pouvoir le transporter, le maintenir et raccorder ses câbles. Le guide de sécurité DGX H100/H200 impose notamment de considérer la stabilité du rack, les charges mécaniques, la circulation d'air, la mise à la terre et le risque de surcharge des circuits.[67]

La **densité de puissance**, ou *power density*, relie une charge électrique à un espace, par exemple un rack. Deux salles possédant le même nombre de positions rack peuvent avoir des capacités d'accueil très différentes. Une infrastructure conçue pour des équipements moins denses peut manquer de puissance distribuée ou de refroidissement local bien avant de manquer d'espace physique. Le guide du Department of Energy relie précisément l'évolution des composants puissants aux besoins de refroidissement des serveurs haute densité.[72]

Commencez par un inventaire : enveloppe mécanique du serveur, poids, profondeur, rails compatibles, largeur de passage, dégagement de maintenance et cheminement des câbles. Faites valider la capacité du sol et les moyens de manutention par les responsables compétents. La documentation NVIDIA recommande l'assistance mécanique adaptée et réserve l'intégration et la maintenance à des personnes techniquement qualifiées. Les contraintes ne disparaissent pas parce que le matériel est livré dans un emballage standard.[67]

Ajoutez la sécurité physique : accès contrôlé, surveillance des accès et procédures d'intervention. Le guide DGX étudié destine l'équipement à un local serveur dont l'accès est restreint et contrôlé. Ce n'est pas seulement une question de confidentialité des modèles ; l'accès physique donne aussi accès aux équipements, aux alimentations et à des composants potentiellement chauds.[67]

<a id="i03"></a>
## I03 — Puissance, énergie et périmètres

La **puissance** est un rythme de consommation ; elle s'exprime ici en watts ou kilowatts. L'**énergie** est une consommation accumulée sur une durée ; elle s'exprime par exemple en kilowattheures. Dans un cas simplifié où la puissance reste constante, l'énergie est le produit de la puissance par la durée. Cette distinction évite de confondre la capacité d'une alimentation, une dépense énergétique et une facture.

Le **TDP**, ou *thermal design power*, est une indication de conception d'un composant selon sa définition constructeur ; ce n'est pas une mesure complète de la consommation du serveur ni du site. Pour une installation, il faut partir des spécifications du système complet et du scénario de charge. Le DGX H100/H200 documenté comporte non seulement des GPU, mais aussi des CPU, de la mémoire, des SSD, des interfaces réseau, des ventilateurs et des alimentations.[16]

La puissance **IT** comprend les équipements informatiques du périmètre retenu : serveurs, stockage, réseau et autres équipements concernés. La puissance ou l'énergie **facility** concerne le site complet, donc aussi les systèmes nécessaires à son fonctionnement. Le refroidissement et les pertes de distribution ne doivent pas être oubliés quand on remonte d'une charge IT au besoin global du datacenter. Les méthodes DOE et ENERGY STAR distinguent explicitement l'énergie IT de l'énergie totale.[72][69]

Une fiche peut indiquer la puissance nominale des blocs d'alimentation et une autre valeur pour la consommation maximale du système. Additionner les capacités des blocs n'est pas nécessairement calculer la consommation attendue : certaines alimentations assurent de la redondance. Le guide DGX H100/H200 décrit six alimentations et une configuration de redondance 4+2 ; il indique séparément la spécification de puissance système. Ces données sont propres à cette plateforme et ne doivent pas être appliquées à tout serveur GPU.[16]

## PUE : un rapport d'énergie, pas un score de performance IA

Le **PUE**, *Power Usage Effectiveness*, compare l'énergie totale du datacenter à l'énergie utilisée par ses équipements IT, sur un périmètre et une période cohérents. Le guide DOE le définit à partir des énergies annuelles et distingue le PUE sur énergie de site d'une variante sur énergie primaire. Le document historique ENERGY STAR utilise justement une approche en énergie source : il faut donc citer la méthode avant de comparer des chiffres provenant de contextes différents.[72][69]

**Formule de référence : PUE = énergie totale du site / énergie IT.** Un PUE plus proche de 1 signifie que les charges non IT sont plus faibles relativement aux charges IT dans le périmètre considéré. Cela ne dit pas combien de modèles ont été entraînés, si les GPU sont utiles, ni si les résultats sont de bonne qualité. Deux sites peuvent donc avoir des PUE différents sans que celui au PUE le plus faible fournisse nécessairement le meilleur travail utile par euro.[72]

Pour une estimation simplifiée, si l'on suppose un rapport constant correspondant au scénario, on peut appliquer ce rapport à la puissance IT moyenne. Ce calcul est une projection, pas une mesure annuelle de PUE ni un moyen de connaître directement le calibre d'un circuit. Les pointes, les scénarios de panne et les exigences locales d'installation restent à traiter séparément.

**Exemple calculé avec hypothèses.** Supposons quatre serveurs à 8 kW moyens chacun, plus 3 kW de stockage et réseau. La charge IT moyenne supposée vaut 35 kW. Avec un rapport facility/IT supposé de 1,4, la puissance moyenne totale estimée vaut 49 kW ; l'écart de 14 kW représente l'ensemble des charges non IT de ce modèle, et non uniquement la climatisation. Sur 10 heures au même régime, l'énergie estimée est de 490 kWh. Ces valeurs sont fictives et ne décrivent aucun modèle DGX particulier.

Ne multipliez pas deux fois la charge serveur par le PUE en ajoutant ensuite de nouveau les mêmes frais de refroidissement. Ne multipliez pas non plus une puissance de GPU isolé par le PUE en prétendant avoir inclus tout le serveur et le réseau. Le périmètre du numérateur et celui du dénominateur doivent rester cohérents, sous peine d'obtenir un résultat numériquement exact mais conceptuellement faux.[72]

## Distribution électrique et continuité

Une **PDU**, *power distribution unit*, distribue l'alimentation aux équipements. Un **UPS**, *uninterruptible power supply*, fournit une continuité temporaire selon sa capacité et sa conception ; il ne constitue pas une source d'énergie infinie. Le guide DOE traite les pertes et rendements des UPS, les systèmes de distribution et leur utilisation à charge partielle. Le dimensionnement doit prendre en compte les équipements réellement alimentés et le niveau de continuité recherché.[72]

Les chemins **A/B** visent une résilience de distribution, mais deux prises ne prouvent pas à elles seules deux chemins indépendants. Demandez quelles dépendances restent communes et ce qui se passe lorsqu'une branche disparaît. Une configuration qui répartit la charge en fonctionnement normal doit également être examinée en mode dégradé. Le guide DGX documente des comportements distincts selon le nombre d'alimentations encore disponibles, ce qui montre pourquoi le scénario de panne compte autant que l'état normal.[16]

Le **power capping**, ou plafonnement de puissance, peut faire partie d'une stratégie d'exploitation sur des plateformes compatibles. Ne le considérez pas comme une permission de dépasser les limites de l'installation : la validation des circuits, protections, câbles et prises relève des spécifications applicables et des professionnels habilités. Les avertissements NVIDIA insistent sur les cordons compatibles, la mise à la terre et les risques de surcharge.[67]

## Refroidir le chemin réel de la chaleur

Pour un système refroidi par air, l'objectif est que l'air à l'entrée des équipements reste dans les conditions autorisées et que l'air chaud ne retourne pas directement vers cette entrée. Les **allées froides et chaudes**, *cold aisle/hot aisle*, organisent les prises d'air et les rejets. Le **confinement**, ou *containment*, limite leur mélange. Le guide DOE décrit le placement des racks et l'obturation des ouvertures comme des moyens de réduire la recirculation.[72]

Mesurer uniquement la température d'une paroi de la salle peut manquer un point chaud à l'entrée d'un serveur. Le guide DOE recommande de placer les mesures de contrôle près de l'avant des équipements pour le schéma d'air concerné. Il faut aussi respecter le sens des flux : un équipement ou un câblage qui perturbe le passage de l'air peut créer un problème local même si la capacité globale de refroidissement semble suffisante.[72][67]

Le **refroidissement liquide direct**, *direct liquid cooling*, transfère la chaleur à un fluide près de son point de production, plutôt que de la transférer d'abord à l'air de la salle. Le guide DOE distingue notamment les plaques froides, l'immersion et les échangeurs air-liquide de porte arrière ; ces derniers ne sont pas exactement le même mécanisme que les deux premiers. Certaines solutions sont hybrides et continuent à nécessiter de l'air pour une partie des composants.[72]

Une **CDU**, *coolant distribution unit*, intervient dans les architectures de distribution et d'échange du circuit de refroidissement liquide. Une conception doit préciser le fluide, la température, le débit, les exigences de qualité, les interfaces avec le site et les procédures de maintenance. L'eau ne doit pas être improvisée dans un serveur prévu autrement : le guide DOE montre des familles de technologies, pas une possibilité de conversion universelle de tout équipement.[72]

Le liquide peut mieux répondre à certaines densités et améliorer l'efficacité, mais il ne supprime ni la chaleur à rejeter ni les contraintes de disponibilité. Les pompes, échangeurs, capacités du site et scénarios de fuite ou de maintenance font partie de l'étude. Ne mémorisez donc pas « tout GPU exige du liquide » : les exigences exactes viennent du système considéré, comme l'illustrent les spécifications environnementales propres au DGX H100/H200.[72][16]

<a id="i04"></a>
## I04 — Comparer on-premises, cloud et colocation

**On-premises**, souvent écrit *on-prem*, désigne ici une infrastructure exploitée sous le contrôle de l'organisation ; la propriété et les responsabilités doivent être précisées contractuellement. Dans la référence SuperPOD étudiée, NVIDIA décrit un modèle où le client possède le matériel, soit dans son datacenter, soit dans une colocation commerciale. La **colocation** ne signifie donc pas nécessairement que le client loue des instances de calcul à la demande.[68]

Pour comparer avec un **cloud**, utilisez une grille de décision plutôt qu'un slogan. Questions à poser : le besoin est-il permanent ou irrégulier ? Quelle capacité peut être obtenue au moment voulu ? Quel réseau relie les GPU proposés ? Où résident les données ? Qui maintient le matériel et qui configure les services ? Quelle est la politique de sortie des données ? Les réponses dépendent du fournisseur, de l'offre et du contrat : aucun prix ni niveau de disponibilité universel n'est affirmé ici. NVIDIA recommande de considérer les approches cloud, on-premises et hybrides en les reliant aux besoins et au coût sur la durée.[74]

Le cloud peut être pertinent pour une expérimentation courte ou une augmentation temporaire si l'offre répond aux exigences. L'on-prem peut être pertinent lorsqu'un besoin durable, des contraintes de contrôle ou une intégration locale justifient l'investissement et l'exploitation. Ce sont des hypothèses de décision à vérifier, pas des garanties économiques. Une bonne comparaison inclut aussi le temps d'approvisionnement et le risque que les ressources souhaitées ne soient pas disponibles.

Le **coût total**, *total cost of ownership* ou **TCO**, doit inclure les catégories pertinentes au cas étudié : acquisition ou location, énergie, refroidissement, réseau, stockage, support, personnel, transfert des données, sauvegarde et sous-utilisation. Pour le cloud, vérifiez les modalités réelles de réservation, d'interruption et de transfert ; pour l'on-prem, vérifiez les travaux du site et les délais. Le prix facial d'un GPU ou d'une heure d'instance ne suffit pas à représenter le service complet. Le guide NVIDIA pour les responsables IT cite notamment calcul, stockage et maintenance dans l'évaluation du TCO.[74]

**Cas comparatif.** Une équipe veut essayer un modèle pendant deux semaines sans facility prête. Un service cloud compatible peut éviter un investissement immédiat, sous réserve de disponibilité et d'autorisation d'y placer les données. Une autre équipe dispose d'une charge stable et d'une salle validée : elle doit comparer les coûts sur sa durée réelle d'utilisation. La conclusion peut être différente sans contradiction ; ce sont les contraintes qui changent.

Une approche **hybride** répartit les usages entre plusieurs environnements. Elle doit traiter le mouvement des données, la cohérence des versions et les droits d'accès. Ne supposez pas qu'une image logicielle portable donne automatiquement des performances réseau identiques partout : les chemins GPU-adaptateurs et les capacités de communication dépendent de la plateforme, comme le rappellent les restrictions GPUDirect.[55]

## Méthode de dimensionnement en six décisions

1. **Définir le résultat attendu.** Décrivez la charge, le délai et les contraintes de données, sans choisir immédiatement un matériel.
2. **Estimer puis mesurer les ressources.** Distinguez VRAM, RAM, calcul, lectures, écritures et communications ; repérez le facteur qui limite le résultat.
3. **Choisir une unité cohérente.** Vérifiez ensemble serveur, interconnexion, adaptateurs, stockage et logiciels, à l'image de l'approche équilibrée des architectures de référence.[68]
4. **Valider le site.** Place, poids, manutention, alimentation, conditions d'entrée, évacuation de chaleur, accès et maintenance doivent être acceptés par les responsables compétents.[67][72]
5. **Étudier la croissance et les pannes.** Prévoyez ports, câbles, stockage et procédures avant de remplir toute la capacité disponible ; la référence B200 anticipe notamment la croissance des fabrics.[66]
6. **Comparer l'exploitation.** Documentez le coût et les responsabilités du mode d'hébergement retenu, puis testez les hypothèses qui pourraient inverser la décision.

Cette méthode produit un dossier de décision vérifiable : besoin, hypothèses, résultat des essais, architecture proposée et limites connues. Ce dossier est plus utile qu'une liste de références commerciales sans relation avec la charge.

## Pièges, récapitulatif et auto-évaluation

**Pièges :** confondre kW et kWh ; assimiler TDP GPU et puissance du site ; prendre la somme des alimentations redondantes pour une consommation mesurée ; traiter PUE comme un score de performance IA ; confondre place libre et capacité thermique disponible ; déclarer le cloud toujours moins cher ; appliquer une température de fonctionnement d'un modèle à tous les serveurs.[16][72]

**Récapitulatif :** le besoin IT doit être relié à une installation sûre, à des chemins d'énergie et de refroidissement cohérents et à un mode d'exploitation viable. La bonne infrastructure est celle dont les hypothèses ont été explicitées et vérifiées, pas celle dont le nom est le plus récent.

1. **Le rack peut recevoir physiquement un serveur. Est-il prêt ?** Pas nécessairement : charge mécanique, alimentation, refroidissement, câblage et maintenance restent à valider.[67]
2. **Un PUE plus faible prouve-t-il un entraînement plus rapide ?** Non. Il porte sur un rapport d'énergie facility/IT, pas sur le travail utile produit.[72]
3. **Pourquoi contrôler la température à l'entrée du serveur ?** Pour détecter les conditions réellement reçues par l'équipement, y compris les points chauds locaux.[72]
4. **Le liquide élimine-t-il le besoin de rejeter la chaleur ?** Non. Il change le chemin de transfert ; le système doit toujours évacuer cette chaleur.[72]
5. **Peut-on choisir cloud ou on-prem avec le seul prix horaire d'un GPU ?** Non. Il faut intégrer durée d'usage, données, disponibilité, réseau, exploitation et responsabilités du cas concret.

## Sources

[16] https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html — Introduction to NVIDIA DGX H100/H200 Systems — NVIDIA DGX H100/H200 User Guide
[55] https://docs.nvidia.com/cuda/gpudirect-rdma/index.html — 1. Overview — GPUDirect RDMA 13.4 documentation
[66] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/network-fabrics.html — Network Fabrics — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[67] https://docs.nvidia.com/dgx/dgxh100-user-guide/safety.html — Safety — NVIDIA DGX H100/H200 User Guide
[68] https://docs.nvidia.com/dgx-superpod/reference-architecture-scalable-infrastructure-b200/latest/dgx-superpod-components.html — Key Components of the DGX SuperPOD — NVIDIA DGX SuperPOD: Next Generation Scalable Infrastructure for AI Leadership Reference Architecture Featuring NVDIA DGX B200
[69] https://www.energystar.gov/ia/partners/prod_development/downloads/DataCenterRating_General.pdf — ENERGY STAR for Data Centers — PUE metric
[72] https://www.energy.gov/sites/default/files/2024-07/best-practice-guide-data-center-design.pdf — DOE Best Practices Guide for Energy-Efficient Data Center Design (2024)
[74] https://images.nvidia.com/aem-dam/Solutions/documents/bus-leader-industry-brief-evolving-for-ai-3150350.pdf — NVIDIA Evolving Your Infrastructure for AI: Considerations for IT Leaders
