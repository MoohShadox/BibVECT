

# An ordinal power index build on ordinal preferences 

## Introduction

This article is placed in the theme of preference representation, we assume that we have a set $\mathcal{A}$ of alternatives (objects for instance) and decision maker that express his preferences on the subsets of alternatives with a predicate $\succ$ that means for a pair of subsets $(A,B)$ where $A \succ B$ that "A is preferred to B".

Finding the power indexe in the general case is a NP-Hard problem, here we place ourselfs in a context where we have a set of preferences that is $\theta$-additive for a given $\theta$ ($|\theta|=k$).

This means that we could find a set of weights $U = [u_{s_0}, u_{s_1}, ... , u{s_k}]$ with $s_i \in \theta; \forall i \leq k$ such that the function defined by
$$
f_U(A) = \sum_{S \in \theta} x_S^A u_s
$$
represents the preferences expressed by the users i.e. $\forall A,B \in 2^{\mathcal{A}}, A \succ B \rightarrow f_U(A) > f_U(b) $.

For a given set $R^\succ$ of preferences, the set of $\theta$-additive functions that represents the preferences is noted $U_\theta^{R^\succ}$.

We also extend an ordinal relation from $U_\theta^{R^{\succ}}$that is defined as follow: 
$$
A \succ_\theta B \iff \forall U_i \in U_{\theta}^{R^\succ}; f_{U_i}(A) > f_{U_i}(B)
$$
With the assumption that the preferences are $\theta$-representable, could we determine an order on the alternatives ? which properties this order have ? and how could we use this order to sample qualitative subsets ?

## Benzhaf-like power index with a $\theta$-additive evaluation 

The Benzhaf power index has many variants, the general intuition behind each of them is to evaluate the quality of an alternative by estimating it's mean marginal contribution to the coalitions that does'nt contain it.

Having a valuation function $v$ that gives us for each set $S$ of alternatives it's value $v(S)$ the marginal contribution of the element $a$ to the set $S$ where $S$ does not contain $a$ is given by:
$$
m(a,S) = v(S \cup \{i\}) - v(S)
$$
By noting $S^{-a}$ the set of subsets that does not contain the alternative $a$, the Benzhaf Power Index is given by: 
$$
I(a) = \frac{1}{2^{n-1}} \sum_{S \in S^{-a}} [ v(S \cup \{i\}) - v(S)] 
$$
Now, since we don't have a value function $v$ but a set of preferences that are representable by at least one $\theta$-additive function $f_{U}$, let's see how we the power index define with $f_{U}$ instead of $v$ could be written differently.

We will note $\phi_\theta(a)$ the subset of $\theta$ where each element contain the alternative $a$, for instance with $\theta = \{1,2,3,\{1,3\},\{1,2,3\}\}$ $\phi_\theta(1) = \{1, \{1,3\}, \{1,2,3\}\}$, We will also note $\phi_\theta(a)^{-a}$ the same subset but after removing $a$ from each element $\phi_\theta^{-1}(1) = \{\empty, \{3\}, \{2,3\}\}$.

The first result is that for a subset of alternative $S$ and an alternative $a$ if $\forall S_j \in \phi_\theta(a); S_j \not \subset S$ then $m(a,S) = 0$ and so the marginal contribution of  $m(a,S)$ is null for any $S \in S^{-a}$.

Let S be a subset in $S^{-a}$, the marginal contribution of an alternative $a$ on a subset $S$ depends on the the intersections between $S \cup i$ and $\phi_\theta(a)$
$$
m(a, S) = \sum_{S_i \in \phi_\theta(a)} u_{S_i} x_{S_i}^{S \cup \{i\}} - \sum_{S_i \in \phi_\theta(a)} u_{S_i} x_{S_i}^{S} = \sum_{S_i \in \phi_\theta(a)} u_{S_i} x_{S_i}^{S \cup \{i\}} 
$$
Where $x_{S_i}^S$ is the binary indicator of $S_i \subset S$. Moreover, we can notice that $f_{U}(S \cup \{i\})$ depends on the intersection of $S$ and $\phi_\theta^{-a}(a)$.

We will note $\mathcal{A}^S$ the set of subsets $S_j \in 2^{\mathcal{A}}$ such that $S \subset S_j$, if $|\mathcal{A}| = n$ then $|2^{\mathcal{A}}| = 2^n$; also for any $S$ the size of $\mathcal{A}^{S}$ is given by $2^{n-|S|}$.

For instance if $\phi_\theta^{-1}(1) = \{\empty, \{3\}, \{2,3\}\}$ then

- if $ \{2,3\} \in S$;  $m(a,S) = u_1 + u_{1,3} + u_{1,2,3}$
- if $\{3\} \in S$;  $m(a, S) = u_1 + u_{1,3}$
- if $\{\empty\} \in S$;  $m(a, S) = u_1$

So in other terms, $u_{1,2,3}$ is included in the marginal contribution of all the subsets in $S^{-1}$ that contains $\{2,3\}$, $u_{1,3}$ is contained in the marginal contribution of all the subsets in $S^{-1}$ that contains $\{3\}$ and $u_{1}$ is contained in the marginal contribution of any subset in $S^{-1}$.

For any alternative $a$, and for any subset $S_i \in  \phi_\theta^{-a}(a)$  the number of subsets $S \in S^{-a}$ that have a marginal contribution that contains $u_{S_i}$ is $2^{n-|S_i|}$ and since the size of $S^{-a}$ is $2^{|\mathcal{A}|-1}$ the proportion of them is:
$$
\frac{2^{|\mathcal{A}|-|S_i|-1}}{2^{|\mathcal{A}| - 1}} = \frac{1}{2^{|\mathcal{A}| - 1}.2^{-|\mathcal{A}|+|S_i|+1}} =\frac{1}{2^{|S_i|}}
$$
and so the power index of an alternative $a$ with respect to a cardinal function $U$ in $U_\theta$ could be written as: 
$$
I_{U}(a) = \sum_{S \in \phi_\theta(a)} \frac{1}{2^{|S|}} u_S
$$

## Ordinal relation on the alternatives

As we built an ordinal relation on subsets from different cardinal ones, we could extend this process and define an ordinal relation on the alternatives as follows: 
$$
a \gg_{\theta}^R b \iff \forall U^i \in U_{\theta}^R; I_{U^i}(a) \geq I_{U^i}(b)
$$
 

