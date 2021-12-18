## Liens bibliographiques

- Lex Social Ranking, [Bernardi et al., 2017] Giulia Bernardi, Roberto Lucchetti, and Stefano Moretti. Ranking objects from a preference relation over their subsets.
- Ceteris Paribus Ranking, Adrian Haret, Hossein Khani, Stefano Moretti, and Meltem  Ozturk. Ceteris paribus majority for social ranking.
- Review de sets rankings, [Barbera et al., 2004] Salvador Barbera, Walter Bossert, and Prasanta K Pattanaik. Ranking sets of objects

## Problématique du Social Ranking
Le social ranking est une problématique ou on dispose d'une relation d'ordre sur un power set (sur tout les sous ensembles d'un ensemble d'alternatives) typiquement on pourrait avoir:  $ 1 \sim 3 \succ 123 \succ 13 \sim 12 \succ 23 \succ 2 \sim 3 $ Et on essaye d'en déduire une relation d'ordre sur les éléments ${1, 2, 3}$

## Méhtodes existantes
Cet article décris deux méthodes déja existantes avant d'en proposer une
### Méthode Lexicographique
La première de Haret et Al consiste a comparer deux éléments en comparant lexicographiquement le nombre d'apparitions de ces éléments dans les premières places du classement, par example pour la power relation précédente on aurait $$ 1 : (1, 1, 2, 0,0) $$ $$ 2 :(0,1,1,1,1) $$ $$ 3: (0,1,1,1,1) $$ et donc on en conclu que $$ 1 \succ 2 \sim 3 $$
### Comparaisons Ceteris-paribus
La seconde est basée sur des comparaisons ceteris-paribus ou pour chaque pair d'éléments chaque ensemble ne contenant pas ces éléments vote en effectuant une comparaison ceteris-paribus pour départager chaque pair par exemple l'ensemble 3 est indifferent car  $$ {1,3} \sim {1,2}  $$ alors que l'ensemble vide se prononce en faveur de 1 car $ {1} \succ {2} $

## Méthode proposée
La méthode proposée est une méthode qui peut éventuellement étendre n'importe quel score de la forme 
$$
V_i(u) = P(S_{-i}) \sum_{A \in S_{-i}} u(A \cup {i}) - u(A)
$$
ou $S_{-i}$ représente l'ensemble de tous les subsets ne contenant pas i 

