---
layout: post
title: Streaming Euclidean Max-Cut
date: 2023-11-25
summary: Resolving the Euclidean Max-Cut problem in the high-dimensional regime and streaming model
categories: my-research

---

<span style="display: none;">
$$
\DeclareMathOperator{\cut}{\text{cut}}
\DeclareMathOperator{\maxcut}{\text{Max-Cut}}
\DeclareMathOperator{\E}{\mathbb{E}}
\DeclareMathOperator{\poly}{\mathrm{poly}}
\DeclareMathOperator{\polylog}{\poly \log}
$$
</span>

## The Euclidean Max-Cut problem

In the classical graph Max-Cut problem, we are given an undirected and weighted graph $G(V,w)$. For all $S \subseteq V$, define $\cut(S) = \sum_{u\in S,v\notin S} w(u,v)$. We want to find $\maxcut(G)=\max_{S \subseteq V} \cut(S)$.

A special case of interest is that $V$ is a subset of a metric space $(T,d)$ and $w=d$.  In particular, if $(T,d) = (\mathbb R^d,\ell_p)$, the problem is called Euclidean Max-Cut.

The Max-Cut problem (even in the Euclidean case) does not admit an [FPTAS](https://en.wikipedia.org/wiki/Fully_polynomial-time_approximation_scheme). Still, a 2-approximation is easy to compute. Let $S$ be a random subset that each $v \in V$ is included with probability $1/2$. Then, $\maxcut(G) \ge \E \cut(S) \ge \frac 1 2 \sum_{\lbrace u,v\rbrace} w(u,v)$.

## The geometric streaming model

There are many different settings in the streaming model. We consider the strongest one here, i.e. the dynamic data streams.

The input $P \subseteq [\Delta]^d \subset \mathbb R^d$ is represented by an arbitrarily long sequence of insertions and deletions of points. The algorithm needs to cope with these updates and outputs $\maxcut(P)$ only for the final point set $P$.

Note that we only need to minimize the space complexity and the running time can be exponential.

Let $\lvert P\rvert = n$. We will present a $\poly(\log \Delta, 1/\varepsilon, d)$ space[^1] streaming algorithm approximating $\maxcut(P)$ to the $(1+\varepsilon)$ ratio. We can think $d = O(\log n / \varepsilon^2)$ because of [JL lemma](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma).  So, this is quite tight.

## Dimension reduction

There is a so-called "[curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality)" phenomenon which states that, most high-dimensional algorithms suffer from an $\exp(d)$ factor. For example, the [quadtree](https://en.wikipedia.org/wiki/Quadtree) will have $2^d$ children when $d$ grows. Recently, the community wants to get rid of this curse. Though we have succeed on Max-Cut, the problem is actually "not so hard" due to the following fact:

**Theorem (Constant-dimensional JL).** Let $P \subset \mathbb R^d$ equipped with $\ell_2$ metric. There exists a randomized map $\pi : \mathbb R^d \to \mathbb R^{d'}$ with $d' = O(\log(\frac{1}{\varepsilon \delta})\varepsilon^{-2})$ such that $\maxcut(\pi(P)) \in (1 \pm \varepsilon) \maxcut(P)$ holds with probability $1-\delta$.

**Proof.** Let $E = \lbrace \lbrace x,y\rbrace:d(\pi(x),\pi(y)) \notin (1 \pm \varepsilon)d(x,y) \rbrace$ be the distorted pairs. For all $S \subseteq P$,
$$
\begin{align*}
\lvert \cut(\pi(S))-\cut(S) \rvert \le & \sum_{x \in S,y \notin S} \lvert d(x,y) - d(\pi(x),\pi(y)) \rvert\\
			  \le &\varepsilon \cut(S) + \sum_{\{x,y\} \in E} \lvert d(x,y) - d(\pi(x),\pi(y))|\\
			  \le &\varepsilon \cut(S) + \sum_{\{x,y\} \in P^2}\max(\lvert d(x,y) - d(\pi(x),\pi(y))\rvert - \varepsilon d(x,y),0)
\end{align*}
$$


It is sufficient to bound the second term. We construct $\pi$ by a $d\times d'$ matrix with i.i.d. $N(0,1/d)$ entries. We use a fact about Gaussians.

**Fact.** For $X \sim N(0,I_{d'}/{d'})$, $\E \max(\lvert \lVert X \rVert - 1 \rvert - \varepsilon,0) \le \exp(-C\varepsilon^2d') \le \varepsilon\delta$.

This implies $\E \max(\lvert d(x,y) - d(\pi(x),\pi(y))\rvert - \varepsilon d(x,y),0) \le \varepsilon \delta d(x,y)$ because we may assume $x - y = e_1$ by rotation and scaling.

Then, by Markov's inequality, the second term is bounded by $\varepsilon \sum_{\lbrace x,y\rbrace\in P^2} d(x,y) \le 2\varepsilon \maxcut(P)$ with probability $1-\delta$. $\square$

Even though, if we directly reduce the dimension and invoke some $\exp(d)$ space algorithm, there is an undesired $\exp(1/\varepsilon^2)$ factor. It is non-trivial to avoid this.

## Randomized tree embedding

If we only want an $O(d \log \Delta)$ approximation, we can work on an edge-weighted tree $(T,w)$ by a randomized embedding $\pi : (\mathbb R^d,\ell_p) \to (T,d)$. The metric is $d(x,y)=\sum_{e\in x \leadsto y} w(e)$ where $x \leadsto y$ is consist of edges on the unique path from $x$ to $y$.

*TODO*

## Importance sampling

There is an importance sampling technique converting the ratio to the complexity. Consider computing $X = \sum_{i=1}^n X_i$ where $X_i \ge 0$. The idea is to sample $i$ with probability approximately proportional to its contribution. If one can construct a random variable $I$ such that $\Pr[I = i] = p_i \ge \frac{X_i}{X \lambda}$, then $\E[X_I/p_I] = X$ and $\E[(X_I/p_I)^2] = \sum_i X_i^2/p_i \le \lambda X^2$. By Chebyshev's inequality, taking $\lambda/\varepsilon^2$ samples of $I$ can estimate $X$ to $(1+\varepsilon)$ approximation.

In case of Max-Cut, since $\maxcut(P)$ is close to $\sum_{\lbrace x,y\rbrace} d(x,y)$, one may want to define the importance of $x$ as $d(x)=\sum_{y} d(x,y)$. This indeed provides good concentration:

**Theorem (Sample Complexity of Max-Cut).**  Let $P$ be a subset of a metric space $(T,d)$, $\mu$ be a distribution over $T$ such that $\mu(p) \ge \frac{d(p)}{\lambda \sum_p d(p)}$ for some $\lambda \ge 1$. If we draw $O(\poly(\lambda/\varepsilon))$ samples $V$ from $\mu$, and build a vertex-weighted graph $G(V,\mu,d)$ where $\cut(S) = \sum_{x\in S,y \notin S} d(x,y)/\mu(x)\mu(y)$, then $\maxcut(G) \in (1 \pm \varepsilon)\maxcut(P)$ w.h.p.

This theorem can be proved by a simple black-box reduction to a classical sampling theorem on unweighted graphs. The idea is discretizing the weighted vertices and edges to many identical copies and then taking limits.

**Theorem (Additive cut sparsification).** Let $G(V,E)$ be an unweighted graph, i.e. $\cut(S) = \lvert \lbrace\lbrace u,v\rbrace \in E : u \in S,v \notin S\rbrace\rvert$. Let $V'$ be an uniformly random subset of size $O(\varepsilon^{-4})$. Then, $\left\lvert \frac{\maxcut(V')}{\lvert V'\rvert^2} - \frac{\maxcut(V)}{\lvert V \rvert^2} \right\rvert \le \varepsilon$ holds w.h.p.

## Quadtree importance sampler

Recall that the tree embedding $\pi$ guarentees $d(x,y) \le d(\pi(x),\pi(y))$ and $\E d(\pi(x),\pi(y)) \le \lambda d(x,y)$ for small $\lambda$. By Markov's inequality, $\sum_p d(\pi(p)) \le \lambda' \sum_p d(p)$ and $\frac{d(\pi(p))}{\sum_pd(\pi(p))} \ge \frac{d(p)}{\lambda' \sum_p(d(p))}$ hold w.h.p. for small $\lambda'$ .

Hence, if we construct a good importance sampler for $\lbrace d(\pi(p))\rbrace_p$, we will get an importance sampler for $\lbrace d(p)\rbrace_p$ automatically. This allows us to focus on implementing the importance sampler in the streaming model efficiently for the quadtree metric from now on.

*TODO*

---

[^1]: One may think $\log \Delta = \polylog n$. And, you cannot hope for too good dependence on $1/\varepsilon$ because, you can recover the input by insert-and-querying each location if you can estimate $\maxcut(P)$ to a $\poly(1/n)$ precision.
