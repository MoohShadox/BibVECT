# Application d'une approche ordinale a la sélection d'attributs

# Introduction

## Problème de sélection d'attributs

En apprentissage automatique, une problématique cruciale qui se pose durant les phases de conception, de développement de déploiement d'un modèle est celle de la sélection d'attributs, cette problématique consiste a choisir parmi les attributs décrivant les données un sous ensemble d'attributs qui soit le plus apte à les caractériser.

La sélection d'attributs interviens pour plusieurs raisons, limiter le nombre de dimension en éliminant les redondances permet avant tout de faciliter le probléme et donc d'aboutir a des modèles plus efficaces plus rapidement, de plus, avoir des attributs non consistants genère du bruit dans les données ce qui expose à un risque de sur-apprentissage, enfin, un modèle avec moins d'attributs est plus facilement explicable a un utilisateur externe et il est moins couteux cognitivement d'envisager son fonctionnement.

La sélection d'attributs est largement étudiée dans le cadre de la classification et les méthodes utilisées se répartissent en deux types, les filter et les wrapper methods. 

Les filter methodes s'appuient sur des mesures issue de la statistique ou de la théorie de l'information pour évaluer la qualité des attributs sans avoir à entrainer et à évaluer le modèle décisionnel, elles ont pour avantage d'être rapides à éxécuter car elles sont souvent utilisées au sein d'un algorithme, c'est à dire en classant tous les attributs par ordre décroissant de qualité puis en construisant de manière gloutonne le meilleure sous-ensemble d'attributs, mais elles ne prennent généralement pas en compte les synérgies entre les attributs.

Les wrapper methodes quant à elle explorent itérativement l'ensemble des sous-ensembles d'attributs et évalue chaque sous-ensemble en entrainant et en évaluant le modèle avec une base de données restreinte a ce sous-ensemble d'attributs, le mode d'exploration exploite généralement des mécanismes d'intensification et de diversification issue des approches évolutionnaires. Ces méthodes sont couteuses en temps de calcul car il faut entrainer et évaluer le modèle de classification pour chaque combinaison d'attributs, de plus,elles modelisent généralement la préférence entre les sous-ensembles par des mesures cardinales  (précision, rapport de la précision sur la taille du sous ensemble...) ce qui restreint grandement leur expressivité.

## Probléme de subset choice

Sur le plan combinatoire, le probléme de sélection d'attributs appartient au diaspora des problémes de subset choice, ce sont des problémes NP-Complet qui sont très répandus et qui peuvent être très complexes, dans ces problémes on suppose en général qu'un opérateur a une préférence entre chaque couple de sous-ensembles d'alternatives $x_1, x_2$ inclus dans l'ensemble $A$ des alternatives qu'on notera $x_1 \succeq x_2$ et qui signifie que $x_1$ est au moins aussi bien que $x_2$ et l'objectif est de déterminer le meilleur sous-ensemble au sens de cette relation en explorant l'ensemble des sous-ensembles non dominés défini par: 
$$
ND_{\succeq} = \{x \in 2^A; \forall y \in 2^A (y \succeq x) \rightarrow (x \succeq y) \}
$$
Quand cette préférence n'est pas totalement connue, il faut recourir à un processus d'élicitation. Cette elicitation se fait généralement sur une fonction cardinale et consiste à poser une fonction paramétrée $f_\theta$ sensée représenter la préférence du dit utilisateur et définie par:
$$
\forall x,y \in 2^A;  x \succeq y \rightarrow f_\theta(x) \geq f_{\theta}(y)
$$
Ensuite, en interagissant avec l'utilisateur, par exemple en lui demandant de comparer des alternatives, on introduit des contraintes qui représentent ses préférences
$$
x_1 \succeq x_2 \rightarrow f_{\theta}(x_1) \geq f_{\theta}(x_2)
$$
L'ensemble des ces contraintes sera noté $R$ et son extension va restreindre progressivement l'espace des paramètres $\theta_R$ compatibles avec les préférences et donc celui des solution optimale pour au moins un jeu de paramètres $\theta \in \theta_R$ qu'on désignera par la suite par **solution potentiellement optimale**.

L'objectif est d'aboutir rapidement et au prix d'un effort cognitif réduit pour l'opérateur à une solution **nécessairement optimale** c'est a dire une solution qui soit optimale quelque soit $\theta \in \theta_R$ .

## Modélisation du probléme de sélection d'attributs

Si on analyse le probléme de selection d'attributs par le prisme de la théorie de la décision on peut le modéliser comme un problème où chaque sous-ensemble d'attributs est associé a un vecteur décrivant ses performances (taille, précision de classification, ... etc) que l'on peut obtenir au prix d'une interaction avec le modèle de classification, cette interaction consiste à construire et à entrainer le modèle puis à évaluer ses performances, afin de simplifier la suite nous imaginons que la performance d'un modèle est uniquement déterminée par sa précision moyenne sur une 10-fold validation.

Donc notre modèle de classification peut être représenter par un oracle $C$ 
$$
C:
\left|
  \begin{array}{rcl}
    \mathbf{2^A} & \longrightarrow &\mathbf{R} \cross \mathbf{N} \\
    v & \longmapsto & (p_v,|v|) \\
  \end{array}
\right.
$$
Ou $p_v$ represente la précision obtenue en contrsuisant un modèle de classification prennant en paramètres les attributs du sous ensemble $v$, et $|v|$ la taille de ce sous ensemble

La relation $\succeq$  que l'on définira pour le problème de sélection d'attributs pourra contenir les préférences de l'opérateur qui effectue la sélection d'attributs, mais en définissantt: 
$$
x \succeq_{C} y \equiv (p_x \geq p_y) \and (|x| \leq |y|) 
$$
ou plus généralement pour un vecteur quelconque de mesures de performances $x \succeq_C y$ si $C(x)$ domine $C(y)$ au sens de Pareto on a naturellement que $x \succeq_C y \rightarrow x \succ y$ 

Si on reviens sur les deux types de méthodes de sélection d'attributs et qu'on les analyse par le prisme de la théorie de la décision, on s'apperçoit que les méthdoes de ranking font une hypothèse sans la nommer qui est celle que les mesures employées sont des mesures totalement additive qui représentent la relation de préférences $\succeq_{C}$, outre le fait qu'il est impossible de prouver que ce soit tout le temps le cas, cette méthode ne prend pas en compte le fait que les sous-ensembles ont des performances qui varient en fonction du modèle de classification utilisé et ne prend pas non plus en compte les synérgies pouvant exister entre les sous-ensembles d'attributs du fait de la redondance et de la complémentarité pouvant exister entre eux.

Les wrapper methodes en revanche s'appuient sur une exploration de l'ensemble des sous-ensemble d'attributs en utilisant des appels à l'oracle qui servent à évaluer différents sous-ensembles ce qui particularise la selection au modèle et qui permet de prendre en compte les interactions, cependant le nombre d'appels est souvent très grand et contrairement aux rankings methodes il n'y a pas de fonction d'utilité qui guide la recherche.

Le but de ce travail est d'abstraire a ces deux classes de méthodes en utilisant des notions issues de la théorie de la décision, pour se faire on s'inspirera d'une ranking methode a la différence près qu'au lieu d'utiliser une mesure dont on suposera qu'elle est additive on suppose l'existence d'une fonction d'utilité additive $f_\theta$ (2-additive par exemple) et on restreint progressivement l'ensemble $\theta$ en mimant le fonctionnement d'une wrapper methodes, c'est a dire, en évaluant des sous-ensembles d'attributs potentiellement optimaux.

## Notations

- $A = \{a_1, a_2, ..., a_n\}$  Ensemble d'attributs.

- $v \in 2^A$:  Ensemble des sous-ensembles d'attributs.

- C:  Fonction qui associe a chaque sous-ensemble d'attributs une vecteur de performances, ici $p_v$ représente la précision du modèle entrainé en restreingnant les attributs des données a $v$ et $|v|$ le nombre d'attributs.
  $$
  C:
  \left|
    \begin{array}{rcl}
      \mathbf{2^A} & \longrightarrow &\mathbf{R} \cross \mathbf{N} \\
      v & \longmapsto & (p_v,|v|) \\
    \end{array}
  \right.
  $$

- $x \succeq_{C} y$ : Relation ordinale définie par:  $ x \succeq_C y$ si et seulement $C(x)$ domine $C(y)$  au sens de pareto.

- $x \succeq y$ Relation ordinale qui modélise les préférences de l'opérateur qui effectue la sélection d'attributs, elle satisfait naturellement $x \succeq_c y \rightarrow x \succ y$.

- $f_\theta$ Fonction représentant les préférences de l'opérateur paramétrée par le vecteur de paramètres $\theta$, par exemple pour $\theta = \{u_1, u_2\}$ $u(\{1,2\}) = u_1 + u_2$,  et pour $\theta = \{u_1, u_2, u_3, u_4, u_{1,2}, u_{1,4} \}$; $u(\{1,2,3\}) = u_1 + u_2 + u_3 + u_{1,2}$.

- $R$ Ensembles de préférences formulées par l'utilisateur de la forme $x_i \succeq x_j$.
- $\theta_R$ Ensembles de paramètres tel que $\forall \theta \in \theta_R ; \forall (x_i, x_j ) \in R; f_\theta(x_i) \geq f_\theta(x_j)$.
- $S_{-x}$ Ensemble des sous-ensembles ne contenant pas $x$.

# Contribution

Afin d'expliquer notre approche nous allons d'abord expliciter un framework permettant de décrire n'importe quel approche de sélection d'attributs, ce framework se compose de 3 parties: 

- **Un mode d'exploration** : Par exemple les wrapper méthodes explorent en utilisant une métaheuristique, les ranking méthodes n'évaluent que les singletons  et il existe des approches exhaustives qui enumérent tous les sous-ensembles existants.
- **Une fonction d'évaluation** : Dans les méthodes de ranking c'est une mesure statistique de la qualité des attributs et pour les wrapper methodes c'est la précision d'un modèle entrainé avec le sous-ensemble d'attribut qu'on veut évaluer.
- **Condition d'arrêt**: Pour les ranking methodes ça peut être d'atteindre un certain seuil dans le nombre d'attributs ou de sélectionner tous les attributs au dela d'un seuil sur la fonction d'évaluation, pour les wrapper methodes c'est généralement un nombre d'itérations.

A présent on va se servir de ce framework pour décrire la méthode proposée.

## Mode d'exploration

Notre méthode de sélection d'attributs va se baser sur une hypothèse simplificatrice consistant à supposer que la relation $\succeq$ pour laquelle on cherche à explorer l'ensemble $ND_{\succeq}$ est représentable par une fonction $f_\theta$. 

Soit S l'ensemble des sous-ensembles d'attributs déja évalués par l'oracle, nous définissons comme condition à l'évaluation d'un sous-ensemble $v \in 2^A$ qu'il soit potentiellement optimal, chose que l'on peut aisément déterminer en verifiant que $\{ \theta \in \theta_R; \forall x \in S; f_\theta(v) \leq f_\theta(x) \}$ est un ensemble vide.

Ensuite, pour tirer des sous ensembles à évaluer on peut utiliser deux types  d'approches. 

### Tirage par indice de pouvoir

Soit $S_{-x}$ l'ensemble de tous les sous ensemble qui ne contiennent pas $x$, cette approche consiste à définir un indice de pouvoir  $p(i); \forall i \in A$, cet indice de pouvoir est sensé mesurer l'impacte de l'attribut $i$ sur les différents sous-ensembles d'attributs auquel il peut appartenir, ensuite il suffit de décider de la présence de chaque attribut en effectuant un jet aléatoire qui suit la loi: 
$$
P(x \in S) = \frac{p(x)}{\sum_{x \in 2^A} p(x)}
$$
Pour définir cet indice de pouvoir plusieurs méthodes peuvent être envisagées, on peut par exemple penser a une mesure qui quantifie l'écart minimum entre $S$ et $S \cup {i}$ pour chaque $S$ ne contenant pas $i$ comme suit:
$$
p(i) = \sum_{S \in S_{-i}} [min_{\theta}(f_{\theta}(S \cup {i})) - max_\theta(f_{\theta}(S))]
$$
Ou alors en calculant au préalable un $\theta_k \in \theta_R$ particulier, ce $\theta$ peut par exemple être celui qui maximise l'écart entre les éléments qui sont liés par une préférence stricte, ou alors prendre $\theta_k = min_{\theta \in \theta_R}(|\theta|)$ puis en définissant $\forall i \in A$ :
$$
p(i) = \sum_{S \in S_{-i}} [min_{\theta}(f_{\theta}(S \cup {i})) - max_\theta(f_{\theta}(S))]
$$


### Tirage séquentiel

Cette fois on envisages le tirage des attributs comme une opération séquentielle soit  $P(x| S)$ la probabilité d'ajouter $x \notin S$ à S, on pose
$$
P(x | S) = \frac{min_{\theta} f_{\theta}(S \cup x)}{max_{\theta}v(S)}
$$
