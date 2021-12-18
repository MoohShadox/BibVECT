# Liens bibliographiques connexes

- Méthodes d'énumération citée, Galand, L. et Perny, P. (2006). Search for compromise solutions in multiobjective state space graphs
- Méthode UTA, Jacquet-Lagreze, E. et Siskos, J. (1982). Assessing a set of additive utility functions for multicriteria decision-making, the uta method.
- Méthode MACBETH, E Costa, C. A. B. et Vansnick, J.-C. (1995). General overview of the macbeth approach.
- Utilisation d'hypervolume pour comparer des solutions en se basant sur leur polyèdre d'optimalité,  Charnetski, J. R. et Soland, R. M. (1978). Multiple-attribute decision making with partial information : The comparative hypervolume criterion.
- SMAA (Stochastic Multicriteria Acceptability Analysis), Lahdelma, R., Hokkanen, J. et Salminen, P. (1998). SMAA - Stochastic Multiobjective Acceptability Analysis
- Elicitation d'une integrale de choquet, Marichal, J.-L. et Roubens, M. (2000). Determination of weights of interacting criteria from a reference set.
- Méthode online pure pour l'elicitation a partir d'exemples dynamiques, Duchi, J., Hazan, E. et Singer, Y. (2011). Adaptive subgradient methods for online learning and stochastic optimization. 
- STEp Method,  Benayoun, R., De Montgolfier, J., Tergny, J. et Laritchev, O. (1971). Linear programming with multiple objective functions : Step method (stem)
- STEM Amélioré (point d'aspiration), Roy, B. (1976). From optimisation to multicriteria decision aid : three main operational attitudes
- STEM Enrichie, Vincke, P. (1976). Une méthode interactive en programmation linéaire à plusieurs fonc- tions économiques.
- STEM (questions de comparaisons) Geoffrion, A. M., Dyer, J. S. et Feinberg, A. (1972). An interactive approach for multi-criterion optimization, with an application to the operation of an academic department. 
  -STEM (comparaisons + quel objectif améliorer) Vanderpooten, D. et Vincke, P. (1989). Description and analysis of some representa- tive interactive multicriteria procedures.
- Une méthode d'élicitation Robuste Zhou-Kangas, Y. et Miettinen, K. (2019). Decision making in multiobjective optimization problems under uncertainty : balancing between robustness and quality
- Imprecisely Specified Multiattribute Utility Theory White III, C. C., Sage, A. P. et Dozono, S. (1984). A model of multiattribute decision making and trade-off weight determination under uncertainty.
- CSS Current solution strategy, Boutilier, C., Regan, K. et Viappiani, P. (2009). Online feature elicitation in interactive optimization
- CSS Benabbou, N., Perny, P. et Viappiani, P. (2017). Incremental elicitation of choquet capacities for multicriteria choice, ranking and sorting problems.
- CSS dans un domaine combinatoire, Benabbou, N. et Perny, P. (2015b). Incremental weight elicitation for multiobjective state space search
- CSS avec une distribution sur les paramètres, Chajewska, U., Koller, D. et Parr, R. (2000). Making rational decisions using adaptive utility elicitation. 
- CSS avec des distributions elipsoidales, Sauré, D. et Vielma, J. P. (2019). Ellipsoidal methods for adaptive choice-based conjoint analysis. 
- CSS avec des fonctions de croyances, Guillot, P.-L. et Destercke, S. (2019). Preference elicitation with uncertainty : Extending regret based methods with belief functions.
- EVOI et Descente de gradient, Vendrov, I., Lu, T., Huang, Q. et Boutilier, C. (2020). Gradient-based optimization for bayesian preference elicitation. 
- Modélisation de la fonction d'utilité avec un processus Gaussien, Zintgraf, L. M., Roijers, D. M., Linders, S., Jonker, C. M. et Nowé, A. (2018).

# Introduction 

## Difficultés liées à l'elicitation
- Objectifs quadratique (valeurs de performances + pondération de de chaque objectif) 
- On ne cherche pas une solution qui maximise toutes les aggrégations possibles quelque soit leur paramètres mais uniquement celles qui sont compatibles avec les préférences de l'utilisateur
## Que faut il éliciter ?
L'élicitation peut concerner deux aspects de la déterminations d'une solution multi-objective: 
- Eliciter les vecteurs de performances (Méthode UTA, Méthode MACBETH) 
- Eliciter les paramètres de l'aggrégateur Ici deux types d'élicitation existent, l'élicitation a partir d'exemple ou on n'interagit pas avec le décideur si ce n'est pour lui proposer notre recommendation, et l'élicitation incrémentale ou on adapte nos questions au fur et a mesure.

# Elicitation en utilisant des exemples
Cette forme d'élicitation est analogue a la classification d'ailleurs des modèles basés sur des perceptrons ou des SVM ont été proposées, et ces approches se divisent en deux catégories : celles qui ont une bases de données statiques et celle conçu pour permettre l'ajout progressif de nouveaux examples.

## Elicitation en utilisant des exemples statiques
- Charnetski et Soland ont proposé un modèle basé sur le polyèdre d'optimalité d'une solution, i.e le polyèdre de paramètres compatibles avec les préférences de l'utilisateur pour lequel une solution est optimale, et ou on départage les solutions en utilisant l'hyper-volume de ce polyèdre.


- Lahdelma et al ont proposés une variante dans laquelle les solutions sont des variables aléatoires ce qui permet d'introduire la notion de degré de confiance qui modélise la possibilité de se tromper sur les performances des différentes solutions.


- Une integrale de choquet est également élicitable en utilisant de la programmation linéaire (Marechal et Roubens), une regression choquistique est également proposée pour la classification. 

## Elicitation en utilisant des exemples dynamique
Souvent des adaptations des méthodes avec des exemples statiques mais pas uniquement (cf Duchi et Hazan 2011) , l'utilisation d'une mémoire courte est envisageable ce qui permet de gérer les incohérences en oubliant les préférences les plus anciennes,

# Elicitation incrémentale
Ce sont des approches guidée généralement par une fonction d'aggrégation et ou les données préférentielles ne sont plus imposées mais déterminées par les réponse apportées aux questions du décideur.

## Exploration interactive du front de pareto
Le principe consiste a explorer le front de pareto en étant guidé par des interactions avec le decideur, l'exploration du front de pareto se fait généralement en utilisant une somme de tchebychev pondérée augmentée par rapport a un point de référence souhaité.

### Méthode STEM (STEp Method) 
Approche globale: 
- Presenter une solution
- Demander quels critères on pourrait degrader et une borne sur la dégradation acceptable.

Une amélioration a été proposée par Roy ou on peut notamment dégrader plusieurs critère et ou l'utilisateur précise un point d'aspiration.

Une autre amélioration a été proposée par Vinck ou il pose plus de questions : quel critère améliorer ? ou faire les concessions ? de combien ? y'a il des contraintes a relaxer ? de combien ?

### STEM Amélioré
Geoffrion et al considère une version facilitée qui considère a proposer au decideur de choisir entre la solution actuelle et une solution obtenu par transfert de performances d'un critère a l'autre (l'espace de recherche n'est pas restreint c'est juste une question de direction d'optimisation).

Vanderpooten et Vincke [1989] Améliore encore la démarche en proposant deux types de question, les comparaisons précédentes et le décideur peut également préciser quel objectif est a améliorer.

### Autres approches
Lokman et al proposent une approches qui consiste a construire des cones de dominance a partir de comparaison entre es pairs de solutions, ces cones restreignent l'espace de recherche en supprimant les parties dominées.

Zhou-Kangas, Y. et Miettinen, K propose une variante qui gère l'aspect "incertain" des préferences et donc qui élicite le compromis robustesse/performance en posant des questions sur la performance que le décideur est prêt a perdre pour gagner en performances.


## Elicitation des paramètres d'un aggregateur
Contrairement a précédemment, ici, on ne cherche pas directement a proposer des solutions mais a éliciter des jeux de paramètres
Chaque préférence ajoute une contrainte de la forme $$ f_w(x) \geq f_w(y) $$ et ceci étant ça restreint l'espace des paramètres possibles.

### Méthode ISMAUT
On défini w comme étant l'ensemble des paramètres compatible avec les données préférentielles, ensuite l'utilisateur doit choisir dans : $$ ND_w = \\{x; x \succeq y \rightarrow y \succeq_w x\\}$$ une solution et si il n'y arrive pas ajouter une donnée préferentielle pour restreindre w
### Méthode CSS
Pareil que avant mais plus simple car l'utilisateur n'a pas a choisir dans ND une solution unique lui est présentée et c'est la solution qui minimise le maximum de regret
Cette méthode a été etendu au domaine combinatoire ou l'ensemble des solutions n'est pas explicité et ou donc la démarche d'évaluer toutes les questions possibles a poser n'est pas réalisable.
Elle a également été étudiée pour des fonctions non linéaires la difficulté résidant dans le fait que le principe de bellman ne s'applique plus et que par conséquent on ne peut pas déduire l'utilité d'une solution compléte a partir des parties qui la composent.
### Extension de la méthode CSS a la gestion d'incertitudes
Plusieurs méthodes ont été envisagées, la plus basique consiste a relaxer les contraintes des préférences pour en faire un objectif a minimiser puis si il n'atteint pas 0 essayer de supprimer le moins de préférences possibles.

Une autre méthode consiste a considérer une distribution de probabilités sur les paramètres possibles du modèle comme proposée par Chajewska et al, et par Guo et Sanner qui ont proposés une méthode imposant moins de charge cognitive en posant des questions plus facile. Sauré et Vielma utilisent des distributions gaussiennes afin de définir des région élipsoidales de confiance mises a jour a chaque nouvelle préférence.

 Guillot et Destercke proposent une méthode basée sur une fonction de croyance sur les préférences, Vendrov et al proposent quant a eux une méthode basée sur uen relaxation de l'espace des solutions permettant d'utiliser une approche de descente de gradient avec le critère EVOI (Expected Value of Information) pour le choix des questions.

Zintgraf et al proposent une méthode ou la fonction d'utilité est représentée par un processus gaussien avec deux paramètre par solution possible le premier représentant l'utilité espérée et l'autre l'incertitude quant a cette utilité

