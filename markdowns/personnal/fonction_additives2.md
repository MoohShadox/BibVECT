# Ordinal relation derived from a general additive cardinal relation

## Introduction

Subset choice problems are tasks of choosing a subset among a set $\mathcal{A}$ of alternatives. It arises in many application cases and can be challenging since the number of subsets grows exponentially with the size of the alternatives set.
In addition to the combinatorial difficulty, solving these problems requires making assumptions on the decision maker's preferences towards the subsets. Moreover, since the preferences cannot be all known beforehand, we may need to build an interactive approach to query new preferences from the user by using the known ones to select the best subset of items. This process is called Elicitation or Active Learning.

## Decision-maker's preferences representation

There are different possibilities to represent the decision maker's preferences. The choice of a method often depends on the cognitive effort that the elicitation process will require.
In this article, we suppose that the decision-maker gives us a bunch of preferences of the form "I prefer The subset A to the subset B" and that we will note $A \succ B$; we will also note $R^{\succ} $ the set of the pairs $(A, B)$ where $A, B \in 2^\mathcal{A}$ and $A \succ B$.

From this predicate we could define two other predicates 
$$
A \sim B \equiv \neg (A \succ B) \and \neg (B \succ A) \\
A \succeq B \equiv (A \succ B) \or (A \sim B)
$$
And so we will note
$$
R^{\sim} \equiv \{(A,B) | A ,B \in 2^\mathcal{A}; A \sim B \} \\
R^{\succ} \equiv \{(A,B) | A ,B \in 2^\mathcal{A}; A \succ B \}
$$

## Cardinal models and additive functions

In the literature, many models assume that we could associate a value to each subset such that these values reflect the preference of the decision-maker (DM); these models are said to be cardinal since they suppose the existence of a cardinal function f that represents the preferences of the DM i.e 
$$
\forall (A,B) \in R^{\succ}; f(A) > f(B)
$$
One of the most used cardinal models is the 1-additive model; this model makes the strong assumption that we could find a utility for each item $u_a$ with $a \in A$ such that if we note $x_a^A$ the binary indicator of $a \in A$ we have:
$$
f(A) = \sum_{a \in A} x_a^A u_a
$$
With $f$ a function that represents the preferences of the user.

Although, there are many 1-additive functions that could represent the same set of preferences $R^\succ$; we define $U^i$ as the vector of $(u^i_a \in \mathbb{R})_{a \in A} $ that characterizes a 1-additive function and we note $f^i(A) = \sum_{a \in A} x_a^A u^i_a$.

and so we define as follows the set of the 1-additive functions that represent the preferences $R^\succ$
$$
U_{R^\succ} = \{U^i | \forall (A,B) \in R^\succ; f^i(A) > f^i(B)\}
$$
And the traditionnal cardinal models seeks for a particular 1-additive function and then uses it for the recommendation and for the elicitation.

This assumption is very strong because it supposes that there is not any possible interaction between items, another assumption is the 2-additivity assumption where we suppose that each vector $U^i$ contains a value for each alternative and a value for each pair of alternatives.

This could be generalized to $n$, a function that is $n$-additive where $n$ is the number of alternatives is a function that assigns a utility $u_S \in \mathbb{R}$ for each subset of alternatives such that the value of a subset $A$ is given by
$$
f^{U_i}(A) = \sum_{S \in 2^\mathcal{A}} u_S x_S^A
$$


Now again a particular vector of $(u^i_S)_{S \in 2^\mathcal{A}}$ is noted $U^i$ and the set of all the $U^i$ that represents a specific set $R^\succ$ of preferences is noted $U_{R^\succ}$.

At this point you should notice that any 1-additive function is a 2-additive function provided that we extend $U^i$ by adding a utility of 0 for each pair; for the same reason eack $k$-additive function is a $m$-additive function for $m \geq k$ and thus any additive function is a $n$-additive function.

## $\theta$-additive function

Since any function is an additive function and some classes of additive functions such as the $k$-additive functions imposes the nullity of the $u_S$ for $s$ that are bigger than $k$ we introduce a new notion that allows us to represent any additive function with the same framework. 

This notion require defining a set $\theta$ that contains the subsets $S$ of $\mathcal{A}$ where dont impose the nullity of $u_S$, $\theta = \{S | S \in 2^\mathcal{A}\}$; and so a $\theta$-additive function is a $n$-additive function where $\forall S \not \in \theta$ we have $u_S = 0$.

A $\theta$-additive function is characterized by it's vector of utilities $U^i$ where $U^i \in U^\theta$ means that $U^i$ does not contain a non nul coefficient for an element not in $\theta$, and it's expression is written in the following compact form:
$$
f^{U_i}(A) = \sum_{S \in \theta} u^i_S x_S^A
$$
As in the precedent part we define $U_{R^\succ}^\theta$ the set of $\theta$-addtive functions that represent a set of preferences $R^\succ$.

A 1-additive function is a $\theta$-addtive function where $\theta$-contains all the singletons, in general, any $\theta$-additive function could be seen as a k-additive function with $k=max_{S \in \theta}(|S|)$.

## Stability of a cardinal model

Finding a function $U^i \in U^{\theta}_{R^{\succ}}$ that represents the preferences set $R^\succ$ allows us to define a new comparison relation that extends $\succ$ as follows:
$$
A \succ_i B \equiv f^{U_i}(A) > f^{U_i}(B) \equiv  \sum_{S \in \theta} u^i_S x_S^A > \sum_{S \in \theta} u^i_S x_S^B
$$
Having $U^i \in U_{R^\succ}^\theta$ implies that $A \succ B \rightarrow A \succ_i B$ but what about the pairs $(A,B)$ that are not in $R^\succ$ ?

Fishburn [?] shows for a 2-additive model that from the same set $R^\succ$ we could have two 2-additive functions $U^1, U^2 \in U_{R^\succ}^\theta$ such that $A \succ_1 B$ but $B \succ_2 A$ for $(A,B) \in R^\succ$.

It's also true for 2 1-additive functions, for instance, let's say we have the following set of preferences and $\theta=\{a,b\}$:
$$
ab \succ b \\
ab \succ a
$$
Provided that we choose $u_a$ and $u_b$ positive we have a 1-additive function  $U^i \in U_{R^\succ}^\theta$ but the result of the comparison $a \succ_i b$ depends on whether we took $u_a  > u_b$ or not.

From this we could say that taking a specitif $U^i$ creates "artificial" comparisons between the elements, but the problem is that these comparisons could be contradictory from a $U^i$ to another.

In other terms, if the initial relation $\succ$ has specific properties, for example if it's a weak order (non symetric and negatively transitive) then this properties may not be preserved in $R^{\succ'} = \cup_{i} R^{\succ_i} $.

## An ordinal model derived from a cardinal one

In the same article Fishburn [??] extends an ordinal model from the 2-additive cardinal model, in this part, we extend his reasoning to a general $\theta$-additive cardinal model.

For a given $\theta$, the ordinal model is independant from the choice of a specific $U^i \in U_{R^\succ}^\theta$ and is defined as : 
$$
A \succ_{\theta}^R B \equiv \forall U^i \in U_{R^\succ}^\theta; A \succ_i B
$$
And so we could also define $A \sim_\theta^R B $ as follows
$$
A \sim_\theta^R B \equiv \exists U^i, U^j \in U_{R^\succ}^\theta;  (A \succ_i B \and B \succ_j A)
$$
In an unambiguous context we will omit $R$ and note the relations by $\succ_\theta$ and $\sim_\theta$

However the existence of this relation is under the condition that $U^\theta_{R^\succ}$ is not empty; nevertheless, this is not necessarily the case for any $\theta$.

For instance, suppose we have the following set of preferences:
$$
a \succ \empty \\
b \succ \empty \\
\empty \succ \{a,b\}
$$
Then for any $\theta$ such that $\forall S \in \theta; |S| \leq 1$, $U_{R^\succ}^\theta$ is empty.

The reason behind this is that since $a \succ \empty$ and $b \succ \empty$ then $a,b \in \theta$ and moreover $u_a > 0 $ and $u_b > 0$, so the utility of $\{a,b\}$ should be $u_a + u_b$ and since $\empty \succ \{a,b\}$ this utility must be negative which is impossible since $u_a > 0$ and $u_b > 0$.

So we will define $\Theta_{R^\succ}$ as: 
$$
\Theta_{R^\succ} = \{\theta | U_{R^\succ}^\theta \neq \empty \}
$$
 Since each element  $U^i \in U_{R^\succ}^{\theta_1}$ belongs to any $U_{R^\succ}^{\theta_2}$ provided that $\theta_1 \subset \theta_2$, we have that if $U_{R^\succ}^{\theta_1}$ is not empty then $U_{R^\succ}^{\theta_2}$ is not empty for each $\theta_2$ where $\theta_1 \subset \theta_2$, we will then define $\Theta_{R^\succ}^{min}$ as a subset of $\Theta_{R^\succ}$ such that
$$
\Theta_{R^\succ}^{min} = \{\theta | \forall \theta_2 \in \Theta_{R^\succ}; |\theta_2|\geq \theta \}
$$

## Robustness of a $\theta$-ordinal model with respect to $\theta$

In this part we study the stability of the comparisons inferred by a $\theta$-ordinal model.

**Proposition 1**: If $\succ$ is  a weak order then so is $\succ_\theta$ $\forall \theta \in \Theta_{R^{\succ}}$.

**Proof** Trivial.

**Proposition** $\forall \theta_1 \in \Theta_R$ and $\forall \theta_2 \subset \theta_1$;
$$
A \succ_{\theta_2} B \rightarrow \neg (B \succ_{\theta_1} A)
$$
**Proof**: Suppose that $A \succ_{\theta_2} B \and  B \succ_{\theta_1} A$

Since $\theta_2 \in \Theta_{R^\succ}$, $\exists U_1 \in U_{R^\succ}^{\theta_2}$, and by setting $u_S = 0$ for each $S$ in $\theta_2$ and not in $\theta_1$ we obtain a $U_2 \in U_{R^\succ}^{\theta_1}$ such that $A \succ_1 B \iff A \succ_2 B$.

Because of $A \succ_{\theta_2} B$ we should have $A \succ_i B$ $ \forall U^i \in U_{R^\succ}^{\theta_2}$ and thus $A \succ_1 B$, but we also have $B \succ_{\theta_1} A$ and so we should have  $B \succ_i A$ $ \forall U^i \in U_{R^\succ}^{\theta_1}$ and despite of that we have $U_2 \in U_{R^\succ}^{\theta_1}$ such that $A \succ_2 B$ and thus $\neg (B \succ_2 A)$ which leads us to a contradiction.

**Proposition 2** $\forall \theta_1 \in \Theta_R$ and $\forall \theta_2 \subset \theta_1$; 
$$
A \sim_{\theta_2} B \rightarrow A \sim_{\theta_1} B
$$
**Proof**: same proof.

**Corollary** $\forall \theta_1 \in \Theta_R$ and $\forall \theta_2 \subset \theta_1$; 
$$
A \succ_{\theta_1} B \rightarrow  A \succ_{\theta_2} B
$$
**Proof** From the proposition 1 we have $ A \succ_{\theta_1} B \rightarrow \neg (B \succ_{\theta_2} A)$ and since $\neg (B \succ_{\theta_2} A) \equiv (A \succ_{\theta_2} B) \or (A \sim_{\theta_2} B)$ we have:
$$
A \succ_{\theta_1} B \rightarrow (A \succ_{\theta_2} B) \or (A \sim_{\theta_2} B)
$$
However, by the contrapositive of proposition 2 we have
$$
\neg (A \sim_{\theta_1} B) \rightarrow \neg (A \sim_{\theta_2} B)
$$
Moreover $A \succ_{\theta_1} B \rightarrow \neg (A \sim_{\theta_1} B)$ so we have by transitivity of $\rightarrow$:
$$
A \succ_{\theta_1} B \rightarrow  \neg (A \sim_{\theta_2} B)
$$
And so we conclude that
$$
A \succ_{\theta_1} B \rightarrow  A \succ_{\theta_2} B
$$

**Proposition 3** $\forall \theta \in \Theta_R$, $\forall R' \subset R$ $\theta \in \Theta_{R'}$

**Proof** Trivial since if $U_i$ represents $R$ it will also represent $R'$ and thus $\theta \in \Theta_R$ is equivalent to $U_\theta^R \neq \empty$ and so $U_\theta^{R'} \neq \empty$ and $\theta \in \Theta_{R'}$

**Proposition 4** $\forall \theta \in \Theta_R$, $ \forall R' \subset R$, $R' \neq \empty$
$$
A \succ_{\theta}^{R'} B \rightarrow \neg (B \succ_{\theta}^{R} A)
$$
**Proof**

Let's suppose that we could have $A \succ_{\theta}^{R'} B $ and $B \succ_{\theta}^R A$.

We have $A \succ_\theta^{R'} B \iff \forall U_i \in U_{\theta}^{R'} f_{U_i}(A) > f_{U_i}(B)$ and since $\theta \in \Theta_R$ we have that $\theta \in \Theta_{R'}$ and thus $U_{\theta}^{R'} \neq \empty$, and so $\exists U_0 \in U_{\theta}^{R'}$ such that $f_{U_0}(A) > f_{U_0}(B)$.

As we said before, since $U_{\theta}^{R'} \subset U_{\theta}^R$ we have that $U_0 \in U_\theta^R$.

But on the other side $B \succ_{\theta}^R A \iff \forall U_i \in U_{\theta}^R; f_{U_i}(B) > f_{U_i}(A)$ which creates a contradiction with $U_0$.

**Proposition 4** $\forall \theta \in \Theta^{min}_R$,  $\forall \theta' \subset \theta$, $\exists R' \subset R$ such that $U_{\theta'}^{R'} \neq \empty$

**Proof**: 

The first thing we must notice is that we cannot have that each element in $\theta'$ is not neither in $A_i$ nor in $B_i$ $\forall (A_i, B_i) \in R$  because $\theta \in \Theta_R^{min}$  and if it was the case $\theta'' = (\theta / \theta') \in \Theta_R$ which is impossible since $|\theta''| \leq |\theta|$ because $\theta \in \Theta_R^{min}$ .

From this we could conclude that there is at least one inequality in $R$ that could be represented by $\theta'$ whatever $\theta' \subset \theta$ is considered.

To see that we recall the fact that if $U_{\theta'}^R = \empty$ means that we have a subset of lines $\overline{R} \subset R, |\overline{R}|\geq 2$ from which we can build two sets of subsets $\{A_0, A_1, ... , A_n\}$ and $\{B_0, B_1, ..., B_n\}$ such that $\forall i \leq n, (A_i, B_i) \in R^\succ$ and $\{A_0, A_1, ... , A_n\} \approx_\theta \{B_0, B_1, ..., B_n\}$ with $\approx_\theta$ a relation defined on the sets of subsets where 
$$
\{A_0, A_1, ... , A_n\} \approx_\theta \{B_0, B_1, ..., B_n\} \equiv \forall S \in \theta ; \sum_{i=0}^n x_S^{A_i} = \sum_{i=0}^n x_S^{B_i}
$$
This subset $\overline{R}$ is called connivent subset of preferences.

So by removing one element of $\overline{R}$ each time we find a connivent subset we obtain a subset of elements that are at least a singleton and that are not connivant.

**Proposition 5** $\forall \theta_1, \theta_2 \in \Theta^{min}_R$, such that $\theta_{12} = \theta_1 \cap \theta_2 \neq \empty$.
$$
A \succ_{\theta_1}^R B \rightarrow \neg(B \succ_{\theta_2}^R A)
$$
**Proof**

Since $\theta_{12} \subset \theta_1$, $\exists R' \subset R$, $U_{\theta_{12}}^{R'} \neq \empty$

Since $R' \subset R$  $ A \succ_{\theta_1}^R B \rightarrow A \succ_{\theta_1}^{R'} B$ and thus by the corrolary $A \succ_{\theta_{12}}^{R'} B$

Now since we have $A \succ_{\theta_{12}}^{R'} B$ we have $\neg (B \succ_{\theta_{2}}^{R'} A)$ by the first proposition, and finally $\neg (B \succ_{\theta_{2}}^{R} A)$ by the last one.

## Conclusion

If the general cardinal model that relies on a specific addition function $U_i$ is not reliable since two different functions may give us contradictory results, the generic ordinal model depends only on the set of subsets whose utility is not necessarily zero $\theta$ and even if choosing different $\theta$ may lead to different comparisons these comparisons will not be contradictory.
