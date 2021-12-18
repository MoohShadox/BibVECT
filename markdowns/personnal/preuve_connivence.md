# Détection de Connivence

## Description du problème

Soit $A$ un ensemble d'objets, $\succeq$ une relation ordinale sur les sous-ensembles d'objects  et $f_\theta$ une fonction qui modèlise cette préférence  $ x \succeq y \equiv f_\theta(x) \geq f_\theta(y)$.

L'objectif de cette partie est de déterminer pour un ensemble $R$ de préférences si il est représentable par une fonction additive et si non de produire un certificat prouvant cette impossibilité.

Pour se faire commençant par définir le probléme ADDITIVE-1 comme suit: 

### ADDITIVE-1: 

- **Données: ** Un ensemble $R$ de préférences de la forme $x \succeq y$.
- **Question**: $R$ est-il representable par une fonction ADDITIVE-1 ?

Cette définition peut donc se généraliser a ADDITIVE-n.

### ADDITIVE-n: 

- **Données: ** Un ensemble $R$ de préférences de la forme $x \succeq y$.
- **Question**: $R$ est-il representable par une fonction ADDITIVE-n ?

De même on peut imaginer une troisième variante du problème qui au lieu de supposer un niveau d'additivté de la fonction prendrait prendrait également en entrée les coefficients d'interactions qu'elle peut manipuler $\theta$, donc si $\theta$ est fixé a tout les singletons on se ramenerait a ADDITIVE-1, si $\theta$ contenant les singletons et les paires on serait sur ADDITIVE-2 etc..

### ADDITIVE-$\theta$: 

- **Données: ** Un ensemble $R$ de préférences de la forme $x \succeq y$, un ensemble de sous ensembles $\theta$.
- **Question**: $R$ est-il representable par une fonction n-additive qui assigne des coefficient nul à toutes les interactions sauf celles présentes dans $\theta$  ?

## Proposition de Fishburn

Le premier élément de réponse à exploiter pour formaliser une solution aux problémes précédent est une proposition de Fishburn qui nécessite au préalable de définir la relation $\approx_1$.

Soit $(A_1, A_2, ... , A_j), (B_1, B_2,...,B_j)$ deux ensembles de sous-ensembles d'alternatives, on écrit $(A_1, A_2, ... , A_j) \approx_1 (B_1, B_2,...,B_j)$ si pour chaque singletons le nombre de sous ensembles d'attributs le contenant est le même dans $(A_1, A_2, ... , A_j)$ que dans $(B_1, B_2,...,B_j)$.

La proposition de Fishburn affirme que si les préférences ne sont pas représentables par une fonction 1-additive alors on devrait pouvoir trouver deux ensembles $(A_1, A_2, ... , A_j), (B_1, B_2,...,B_j)$ avec $j \geq 2$, tel que $(A_1, A_2, ... , A_j) \approx_1 (B_1, B_2,...,B_j)$ et pourtant $\forall i; A_i \succeq B_i$  ces sous ensembles de préférences sont alors désignés par **préférences 1-connivantes**.

Cette propositon nous permet d'envisager la problème complémentaire a ADDITIVE-1 et de proposer une définition au probléme CONNIVENCE-1

### CONNIVENCE-1: 

- **Données: ** Un ensemble $R$ de préférences de la forme $x \succeq y$.
- **Question**: $R$ contient-il un ensemble 1-connivent de préférences ?

On peut également proposer une définition de CONNIVENCE-2 qui se base sur la relation $\approx_2$ définie par $(A_1, A_2, ... , A_j) \approx_2 (B_1, B_2,...,B_j)$ si  $(A_1, A_2, ... , A_j) \approx_1 (B_1, B_2,...,B_j)$ et que pour chaque paire le nombre de sous ensembles d'attributs la contenant est le même dans $(A_1, A_2, ... , A_j)$ que dans $(B_1, B_2,...,B_j)$.

De même on peut définir CONNIVENCE-$\theta$ en définissant $\approx_\theta$  par le fait que $(A_1, A_2, ... , A_j) \approx_\theta (B_1, B_2,...,B_j)$ si chaque coefficient présent dans $\theta$ est présent autant de fois  dans $(A_1, A_2, ... , A_j)$ que dans $(B_1, B_2,...,B_j)$. 

## Complexité du probléme CONNIVENCE-1

Le problème CONNIVENCE-1 est NP-Complet.

### Preuve:

$\rightarrow$ CONNIVENCE-1 est NP car étant donné un certificat étant le sous-ensemble connivant de taille $j$  on peut vérifier en que $ \forall i; A_i \succeq B_i$  en $O(|R|.j)$ et ensuite on peut vérifier que le compte de chaque singleton est le même de chaque coté en un temps $O(|A|)$ avec $|A|$ l'ensemble des alternatives.

$\rightarrow$ Maintenant nous allons montrer que le problème CONNIVENCE-1 se réduit polynomialement vers le probléme SUBSET-SUM défini par 

### SUBSET-SUM

- **Données:** Un ensemble d'entiers $\{a_0, a_1, ... , a_n\}$
- **Question**: Existe un sous-ensemble A tel que $\sum_{a_i \in A} a_i = 0$ 

Pour se faire il suffit de transformer chaque préférence $A \succeq B$  en lui associant un vecteur contenant 1 valeur par singleton tel que pour chaque singleton $x \in A$
$$
v(x) = \left\{
     \begin{array}{@{}l@{\thinspace}l}
       1  &: x \in A \and x \notin B\\
       0 &: x \notin A \and x \notin B \or x \in A \and x \in B \\
       -1 &: x \notin A \and x \in B\\
     \end{array}
   \right.
$$
Une fois qu'on a représenté l'ensembles des préférences par des vecteurs le problème reviens a trouver un sous-ensemble $X$ tel que $\sum_{x \in X} v(x) = [0, 0, ..., 0]$.

Partant de la pour réduire le problème au probléme de subset-sum il suffit de remarquer qu'en représentant chaque nombre entier par un vecteur binaire et en représentant les nombre négatifs par des nombres binaires avec des -1  a la place des 1