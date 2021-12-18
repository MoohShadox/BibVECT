## Pourquoi j'ai lu l'article ?

Je cherche un moyen d'éviter la combinatoire liée a l'énumération de tous les sous ensembles d'éléments ne contenant pas un élément en particulier, donc je m'intéresse a cet article ou l'auteur propose un moyen d'éviter cette combinatoire et je m'y intéresse pour deux raisons : 

- Les méthodes qu'il va proposer évidemment dont je vais chercher si elles répondent a mon probléme.
- La façon qu'il va avoir de **formuler** le problème de réduire cette combinatoire.

## Comment il formule le problème ? 

Déja dans l'abstract on sent qu'il a une vision intéressante du calcul des indice de Shapley-Shubik et de Banzhaf, ainsi il les décrit les dynamiques combinatoire de chaque mécanisme comme suit : 

- L'indice de Shapley considère le nombre de permutations dans lesquelles un élément est "pivotal".
- L'indice de Benzhaf considére le nombre de façons avec lesquelles chaque votant peut faire un "swing" c'est a dire changer la préférence entre deux ensembles.

## Jeu coopératif et jeu coopératif simple

### Jeu coopératif

Un jeu coopératif peut se représenter par sa fonction caractéristique qui associe a chaque coalition possible une valeure réelle, $v : 2^N \rightarrow \mathbf{R}$ avec $v(\empty) = 0$, les joueurs sont donc les éléments de $N$ et les coalitions possibles sont tous les sous ensembles possibles de joueurs. 

### Jeu coopératif simple

Un jeu coopératif est dis simple si sa fonction caractéristique est de la forme : $v : 2^N \rightarrow \{0, 1\}$, que $v(N) = 1$ et que v est monotone.

