Ce document résume les points les plus intéressant de la section 5 de la review des méthode de ranking sur des ensemble d'objets, cette section concerne une sémantique d'ensemble ou un ensemble d'alternatives représente une issue jointe et pas un ensemble de possibilités dont une se réalise au hasard et pas non plus un ensemble de possibilités parmi le décideur choisit a la fin.

## Notations

$X$ est un ensemble d'issues possibles, $\mathbf{X}$ l'ensemble des sous ensemble d'issues possibles, et $\mathbf{X}_n = \{X \in \mathbf{X}; |X| = n\}$.

On considère également une relation $R$ sur les alternatives dans $X$ ou $xRy$ signifie que x est au moins aussi bon que x dont nous définissons une partie strict comme $xPy = xRy \and \neg yRx$, une relation d'indifférence définie comme $xIy  = xRy \and yRx$ et une partie "indéterminée" définie par $xNy = \neg xRy \and \neg yRx$.

## Context général

Cette section aborde le probléme de rangement d'un ensemble a partir d'un ordre sur les alternatives, et plus précisement elle concerne des rangements d'ensembles de même taille.

Dans ce qui suit la relaiton $\succeq_q$ est une relatino sur $\mathbf{X}_q$ et on suppose que $X$ contient au moins 2q+1 éléments.

## Axiomes

Cette partie présente un certain nombre d'axiomes défini pour la realtion $\succeq_q$

### Responsiveness

Cet axiome signifie que si on prend un ensemble d'alternatives $X$ et qu'on remplace un élément $x$ par un élément $y$ alors le rangement de l'ensemble obtenu par rapport à $X$ par $\succeq_q$  dépendra du rangement de $x$ par rapport à $y$ pat $R$ ce qui signifie qu'on a:
$$
A \succeq_q (A / \{x\}) \cup y \equiv xRy
$$
et qu'on a également: 
$$
(A / \{x\}) \cup y  \succeq_q A \equiv yRx  
$$

### Fixed Cardinality Neutrality

Supposons qu'on définisse une bijection qui va renommer chaque élément de $X$ comme suit : 
$$
xRy \equiv \psi(x) R \psi(y) \and yRx \equiv \psi(y)R\psi(x)
$$
Ce renommage n'affecte pas les relations des ensembles, 
$$
A \succeq_q B \equiv \psi(A) \succeq_q \psi(B) \and  B \succeq_q A \equiv \psi(B) \succeq_q \psi(A) 
$$
Du moment qu'on estime $\psi(X) = \{\psi(x_0), ... , \psi(x_n)\}$

## Caractérisation

Soit $ q \in \mathbf{N}$ R un ordre linéaire sur $X$ et $\succeq_q$ un ordre sur $\mathbf{X}_q$ on  a $\succeq_q$ satisfait les deux axiomes de responsiveness et de fixed carinality neutrality si et seulement si c'est un ordre lexicographique.

## Additivté et séparabilité

Le chapitre reviens sur plusieurs définitions relatives aux utilités additive, plusieurs références a des travaux qui cherche une représentation additive du problème sont proposées notamment : 

- Fishburn, P.C., “Methods of estimating additive utilities,” Management Science 13, 1967, 435–453.
- Fishburn, P.C., “Failure of cancellation conditions for additive linear orders,” Journal of Combina-
  torial Design 5, 1997, 353–365

- Fishburn, P.C. and Roberts, F.S., “Unique finite conjoint measurement,” Mathematical Social Sci-
  ences 16, 1988, 107–143.
- Fishburn, P.C. and Roberts, F.S., “Uniqueness in finite measurement,” in: Roberts, F. (ed.), Appli-
  cations of Combinatorics and Graph Theory to the Biological and Social Sciences, Springer, New
  York, 1989, pp. 103–137.
- Krantz, D.H., Luce, R.D., Suppes, P., and Tversky, A., Foundations of Measurement, Vol. 1, Aca-
  demic Press, New York, 1971
- Roberts, F.S., Measurement Theory, with Applications to Decisionmaking, Utility, and the Social
  Sciences, Addison-Wesley, Reading, 1979
- Scott, D., “Measurement structures and linear inequalities,” Journal of Mathematical Psychology
  1, 1964, 233-247.
- Scott, D. and Suppes, P., “Foundational aspects of theories of measurement,” Journal of Symbolic
  Logic 23, 1958, 113–128

### Relation additivement représentable

Une relation est additivement représentable si il existe une fonction  $U : X \rightarrow R$ tel que $\forall A,B \in X$ on ait
$$
A \succeq B \equiv \sum_{x \in A}U(x) \geq \sum_{x \in B}U(x) 
$$

### Conditions nécessaires pour qu'une relation soit additivement représentable

#### Nonnégativité 

$$
\forall A \in \mathbf{X}_0 A \succeq \empty
$$

#### Nontrivialité

$$
X \succ \empty
$$

#### Indépendance forte

$\forall A,B \in \mathbf{X}_0$ et $\forall C \subseteq X \not (A \cup B)$ on a 
$$
A \succ B \equiv A \cup C \succ B \cup C
$$

### Séparabilité

La séparabilité est une relaxation de la representabilité additive, elle se défini comme: 
$$
\forall A \in \mathbf{X}; \forall x \in X / A \\ A\cup \{x\} \succ A \equiv \{x\} \succ \empty
$$

## Ordres signées

Ces ordres ont pour particularité qu'il existe pour chaque élément $ x \in X$ un élément $x^* \in X^*$ qui représente l'alternative inverse de celle réalisée quand on prend $x$ dans l'ensemble.

Par exemple si on prend l'information $x^*R^*y$ ça veut dire qu'il est préférable de ne pas avoir $x$ plûtot que d'avoir y.

### Self-reflection 

Cette propriété se définit comme suit : 
$$
a R^*b \equiv b^*R^*a^*
$$

### Ensemble désirables, non désirables et indfférents

On défini un élément par désirable si l'avoir est mieux que ne pas l'avoir $x P^* x^*$ et inversement pour un élément indésirable $x^*P^*x$, un élément indifférent quant a lui est défini par $x I^* x^*$.

La section se termine par une caractérisation de $\mathbf{X}^d$ $\mathbf{X}^u$ et de $\mathbf{X}^i$ 
