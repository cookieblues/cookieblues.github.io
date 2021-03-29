---
date: 2021-03-23
title: "Machine learning, notes 3b: Generative classifiers"
categories:
  - Guides
featured_image: https://raw.githubusercontent.com/cookieblues/cookieblues.github.io/33c1f7b6dbd05a952e9c9d381173195dce89fc52/extra/bsmalea-notes-2/prob_linreg.svg
---
As mentioned in <a href="{{ site.url }}/guides/2021/03/23/bsmalea-notes-3a/">notes 3a</a>, generative classifiers model the **joint probability distribution** of the input and target variables $\text{Pr}(\mathbf{x}, t)$. This means, we would end up with a distribution that could generate (hence the name) new input variables with their respective targets, i.e., we can sample new data points with the joint probability distribution, and we will see how to do that in this post.

The models, we will be looking at in this post, are called **Gaussian Discriminant Analysis (GDA)** models. Now is when the nomenclature starts getting tricky! Note that a Gaussian *Discriminant* Analysis model is a *generative* model! It is *not* a discriminative model despite its name.

## Quadratic Discriminant Analysis (QDA)
### Setup and objective
Given a training dataset of $N$ input variables $\mathbf{x} \in \mathbb{R}^D$ with corresponding target variables $t \in \mathcal{C}_c$ where $c \in \\{1, \dots, K\\}$, GDA models assume that the **class-conditional densities** are normally distributed

$$
\text{Pr}(\mathbf{x} \mid t = c, \boldsymbol{\mu}_c, \mathbf{\Sigma}_c) = \mathcal{N} \left( \mathbf{x} \mid \boldsymbol{\mu}_c, \mathbf{\Sigma}_c \right),
$$

where $\boldsymbol{\mu}_c$ is the **class-specific mean vector** and $\mathbf{\Sigma}_c$ is the **class-specific covariance matrix**. Using Bayes' theorem, we can now calculate the class posterior

$$
\overbrace{\text{Pr}(t=c | \mathbf{x}, \boldsymbol{\mu}_c, \mathbf{\Sigma}_c)}^{\text{class posterior}}
= \frac{ \overbrace{\text{Pr}(\mathbf{x} \mid t = c, \boldsymbol{\mu}_c, \mathbf{\Sigma}_c)}^{\text{class-conditional density}} \, \overbrace{\text{Pr}(t=c)}^{\text{class prior}} }{ \sum_{k=1}^K \text{Pr}(\mathbf{x} \mid t = k, \boldsymbol{\mu}_k, \mathbf{\Sigma}_k) \, \text{Pr}(t=k) }.
$$

We will then classify $\mathbf{x}$ into class

$$
\hat{h} (\mathbf{x}) = \underset{c}{\text{argmax }} \text{Pr}(t=c | \mathbf{x}, \boldsymbol{\mu}_c, \mathbf{\Sigma}_c).
$$

### Derivation and training
For each input variable $\mathbf{x}_{n}$, we define $t\_{nk} = 1$ if $\mathbf{x}\_n$ belongs to class $\mathcal{C}\_k$, otherwise $t\_{nk}=0$, i.e., we end up having $k$ binary indicator variables for each input variable. Furthermore, let $\textbf{\textsf{t}} = \left( t_1, \dots, t_N \right)^\intercal$ denote all our target variables, and $\pi_c = \text{Pr}(t=c)$ the prior for class $c$. Assuming the data points are drawn independently, the likelihood function is given by

$$ \begin{aligned}
\text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\mu}_1, \dots, \boldsymbol{\mu}_K, \mathbf{\Sigma}_1, \dots, \mathbf{\Sigma}_K \right)
&= \prod_{n=1}^N \prod_{k=1}^K \text{Pr} \left( t_n=k \right)^{t_{nk}} \text{Pr}\left( \mathbf{x}_n \mid t_n = k, \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right)^{t_{nk}} \\
&= \prod_{n=1}^N \prod_{k=1}^K \pi_k^{t_{nk}} \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right)^{t_{nk}}.
\end{aligned} $$

To simplify notation, let $\boldsymbol{\theta}$ denote all the class priors, class-specific mean vectors, and covariance matrices $\left\\{ \pi_1, \dots, \pi_K, \boldsymbol{\mu}_1, \dots, \boldsymbol{\mu}_K, \mathbf{\Sigma}_1, \dots, \mathbf{\Sigma}_K \right\\}$. As we know, **maximizing the likelihood is equivalent to maximizing the log-likelihood**. The log-likelihood is

$$ \begin{aligned}
\ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right)
&= \ln \prod_{n=1}^N \prod_{k=1}^K \pi_k^{t_{nk}} \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right)^{t_{nk}} \\
&= \sum_{n=1}^N \ln \prod_{k=1}^K \pi_k^{t_{nk}} \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right)^{t_{nk}} \\
&= \sum_{n=1}^N \sum_{k=1}^K \ln \pi_k^{t_{nk}} \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right)^{t_{nk}} \\
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left( \ln \pi_k + \, \ln \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right) \right). \quad \quad (1)
\end{aligned} $$

We have to find the maximum likelihood solution for $\pi\_c$, $\boldsymbol{\mu}\_c$, and $\mathbf{\Sigma}\_c$. Starting with $\pi\_c$, we have to take the derivative of $(1)$, set it equal to 0, and solve for $\pi\_c$, however, we have to maintain the constraint $\sum\_{k=1}^K \pi\_k = 1$. This is done by using a Lagrange multiplier $\lambda$, and instead maximizing

$$ 
\ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right) + \lambda \left( \sum_{k=1}^K \pi_k - 1 \right). \quad \quad (2)
$$

Taking the derivative of $(2)$ with respect to $\pi_c$, setting it equal to 0, and solving for $\pi_c$ gives us 

$$ \begin{aligned}
\frac{\partial}{\partial \pi_c} \left( \ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right) + \lambda \left( \sum_{k=1}^K \pi_k - 1 \right) \right)
&= 0 \\
\frac{\partial}{\partial \pi_c} \left( \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left( \ln \pi_k + \, \ln \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right) \right) + \lambda \left( \sum_{k=1}^K \pi_k - 1 \right) \right)
&= 0 \\
\sum_{n=1}^N \frac{t_{nc}}{\pi_c} + \lambda
&= 0 \\
\pi_c \lambda
&= - N_c, \quad \quad (3)
\end{aligned} $$

where $N_c$ is the number of data points in class $\mathcal{C}\_c$, and since we know that $\sum_{k=1}^K \pi_k = 1$, we can find $\lambda$ 

$$ \begin{aligned}
\sum_{k=1}^K \pi_k \lambda
&= - \sum_{k=1}^K N_k \\
\lambda
&= -N.
\end{aligned} $$

Substituting $\lambda = -N$ back into $(3)$ gives us

$$ \begin{aligned}
-\pi_c N
&= -N_c \\
\pi_c
&= \frac{N_c}{N}. \quad \quad (4)
\end{aligned} $$

$(4)$ tells us that the class prior is simply the proportion of data points that belong to the class, which intuitively makes sense as well. Now we turn to maximizing $(1)$ with respect to $\boldsymbol{\mu}_c$. We take the derivative with respect to $\boldsymbol{\mu}_c$, set it equal to 0, and solve for $\boldsymbol{\mu}_c$

$$ \begin{aligned}
\frac{\partial}{\partial \boldsymbol{\mu}_c} \left(
  \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left( \ln \pi_k + \, \ln \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right) \right)
\right)
&= 0 \\
\sum_{n=1}^N
\frac{\partial}{\partial \boldsymbol{\mu}_c} \left(
  t_{nc} \ln \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_c, \mathbf{\Sigma}_c \right) 
\right)
&= 0 \\
\sum_{n=1}^N
\frac{\partial}{\partial \boldsymbol{\mu}_c} \left(
  t_{nc} \ln \left( 
    \frac{1}{\sqrt{ (2\pi)^D \det{\mathbf{\Sigma}_c} }} \exp{\left( -\frac{1}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right) \right)}
  \right)
\right)
&= 0 \\
\sum_{n=1}^N
\frac{\partial}{\partial \boldsymbol{\mu}_c} \left(
  t_{nc} \ln \left( 
    \frac{1}{\sqrt{ (2\pi)^D \det{\mathbf{\Sigma}_c} }}
  \right)
  -\frac{t_{nc}}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right)
&= 0 \\
-\frac{1}{2} \sum_{n=1}^N
\frac{\partial}{\partial \boldsymbol{\mu}_c} 
  t_{nc} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
&= 0 \\
\sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
&= 0 \\
\sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c^{-1} \mathbf{x}_n
&= \sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c^{-1} \boldsymbol{\mu}_c \\
\sum_{n=1}^N t_{nc} \mathbf{x}_n
&= N_c \boldsymbol{\mu}_c \\
\frac{1}{N_c} \sum_{n=1}^N t_{nc} \mathbf{x}_n
&= \boldsymbol{\mu}_c. \quad \quad (5)
\end{aligned} $$

Let's take a moment to understand what $(5)$ is saying. $t\_{nc}$ is only equal to 1, for the data points that belong to class $\mathcal{C}\_c$. Which means that the sum on the left-hand side of $(5)$ only includes input variables $\mathbf{x}$ that belong to class $\mathcal{C}\_c$. Afterwards we're dividing that sum of vectors with the number of data points in the class $N\_c$, which is the same as taking the average of the vectors. This means that the class-specific mean vector $\boldsymbol{\mu}\_c$ is the average of the input variables $\mathbf{x}_n$ that belong to the class. Once again, this makes intuitive sense as well.

Lastly, we have to maximize $(1)$ with respect to the class-specific covariance matrix $\mathbf{\Sigma}_c$



#### Python implementation


### Model selection


## Naive Bayes

### Setup and objective

### Derivation and training

#### Python implementation

### Model selection


## Linear Discriminant Analysis (LDA)

### Setup and objective

### Derivation and training

#### Python implementation

### Model selection


https://www.eecs189.org/static/notes/n18.pdf
https://stats.stackexchange.com/questions/80507/what-is-a-gaussian-discriminant-analysis-gda
https://web.archive.org/web/20200103035702/http://cs229.stanford.edu/notes/cs229-notes2.pdf
https://stats.stackexchange.com/questions/254963/differences-linear-discriminant-analysis-and-gaussian-mixture-model
https://stats.stackexchange.com/questions/190806/sources-seeming-disagreement-on-linear-quadratic-and-fishers-discriminant-ana/190821#190821
https://stats.stackexchange.com/questions/71489/three-versions-of-discriminant-analysis-differences-and-how-to-use-them
https://www.datascienceblog.net/post/machine-learning/linear-discriminant-analysis/
https://xavierbourretsicotte.github.io/LDA_QDA.html