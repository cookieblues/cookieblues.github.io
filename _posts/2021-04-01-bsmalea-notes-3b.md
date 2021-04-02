---
date: 2021-04-01
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
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left( \ln \pi_k + \, \ln \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right) \right) \\
&= \sum_{n=1}^N \sum_{k=1}^K \left(
  t_{nk} \ln \pi_k + t_{nk} \ln \mathcal{N} \left( \mathbf{x}_n \mid \boldsymbol{\mu}_k, \mathbf{\Sigma}_k \right)
\right). \quad \quad (1)
\end{aligned} $$

Expanding $(1)$ will greatly help us in the upcoming derivations:

$$ \begin{aligned}
\ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right)
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left(
  \ln \pi_k +
  \ln \left(
    \frac{1}{\sqrt{ (2\pi)^D \det{\mathbf{\Sigma}_c} }} \exp{\left( -\frac{1}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right) \right)}
  \right)
\right) \\
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left(
  \ln \pi_k +
  \ln \frac{1}{\sqrt{ (2\pi)^D \det{\mathbf{\Sigma}_c} }}
  -\frac{1}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right) \\
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left(
  \ln \pi_k
  -\frac{1}{2} \ln \left( (2\pi)^D \det{\mathbf{\Sigma}_c} \right)
  -\frac{1}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right) \\
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left(
  \ln \pi_k
  -\frac{1}{2} \left(
    D \ln 2\pi + \ln \det{\mathbf{\Sigma}_c}
  \right)
  -\frac{1}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right) \\
&= \sum_{n=1}^N \sum_{k=1}^K t_{nk} \left(
  \ln \pi_k
  -\frac{D}{2} \ln 2\pi
  +\frac{1}{2} \ln \det{\mathbf{\Sigma}_c^{-1}}
  -\frac{1}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right). \quad \quad (2)
\end{aligned} $$

We have to find the maximum likelihood solution for $\pi\_c$, $\boldsymbol{\mu}\_c$, and $\mathbf{\Sigma}\_c$. Starting with $\pi\_c$, we have to take the derivative of $(2)$, set it equal to 0, and solve for $\pi\_c$, however, we have to maintain the constraint $\sum\_{k=1}^K \pi\_k = 1$. This is done by using a Lagrange multiplier $\lambda$, and instead maximizing

$$ 
\ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right) + \lambda \left( \sum_{k=1}^K \pi_k - 1 \right). \quad \quad (3)
$$

Using the result from $(2)$, we then take the derivative of $(3)$ with respect to $\pi_c$, set it equal to 0, and solve for $\pi_c$

$$ \begin{aligned}
\frac{\partial}{\partial \pi_c} \left( \ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right) + \lambda \left( \sum_{k=1}^K \pi_k - 1 \right) \right)
&= 0 \\
\sum_{n=1}^N \frac{\partial}{\partial \pi_c} \left(
  t_{nc} \ln \pi_k 
\right) +
\lambda \frac{\partial}{\partial \pi_c} \left(
  \pi_c - 1
\right)
&= 0 \\
\sum_{n=1}^N \frac{t_{nc}}{\pi_c} + \lambda
&= 0 \\
\pi_c \lambda
&= - N_c, \quad \quad (4)
\end{aligned} $$

where $N_c$ is the number of data points in class $\mathcal{C}\_c$, and since we know that $\sum_{k=1}^K \pi_k = 1$, we can find $\lambda$ 

$$ \begin{aligned}
\sum_{k=1}^K \pi_k \lambda
&= - \sum_{k=1}^K N_k \\
\lambda
&= -N.
\end{aligned} $$

Substituting $\lambda = -N$ back into $(4)$ gives us

$$ \begin{aligned}
-\pi_c N
&= -N_c \\
\pi_c
&= \frac{N_c}{N}. \quad \quad (5)
\end{aligned} $$

$(5)$ tells us that the class prior is simply the proportion of data points that belong to the class, which intuitively makes sense as well. Now we turn to maximizing the log-likelihood with respect to $\boldsymbol{\mu}_c$. Again, using the result from $(2)$, makes it easy for us to take the derivative with respect to $\boldsymbol{\mu}_c$, set it equal to 0, and solve for $\boldsymbol{\mu}_c$

$$ \begin{aligned}
\frac{\partial}{\partial \boldsymbol{\mu}_c} \left(
  \ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right)
\right)
&= 0 \\
\sum_{n=1}^N
\frac{\partial}{\partial \boldsymbol{\mu}_c} 
  -\frac{t_{nc}}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
&= 0.
\end{aligned} $$

To evaluate this derivative, we use the following [matrix calculus identity](https://en.wikipedia.org/wiki/Matrix_calculus#Scalar-by-vector_identities):

> *If $\mathbf{A}$ is not a function of $\mathbf{u}$, and $\mathbf{A}$ is symmetric, then $\frac{\partial \mathbf{u}^\intercal \mathbf{A} \mathbf{u}}{\partial \mathbf{u}} = 2 \mathbf{A} \mathbf{u}$.*

Since covariances matrices are always symmetric, and the inverse of a symmetric matrix is also symmetric, we can use this identity to get

$$ \begin{aligned}
\sum_{n=1}^N
\frac{\partial}{\partial \boldsymbol{\mu}_c} 
  -\frac{t_{nc}}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
&= 0 \\
\sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
&= 0 \\
\sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c^{-1} \mathbf{x}_n
&= \sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c^{-1} \boldsymbol{\mu}_c \\
\sum_{n=1}^N t_{nc} \mathbf{x}_n
&= N_c \boldsymbol{\mu}_c \\
\frac{1}{N_c} \sum_{n=1}^N t_{nc} \mathbf{x}_n
&= \boldsymbol{\mu}_c. \quad \quad (6)
\end{aligned} $$

Let's take a moment to understand what $(6)$ is saying. $t\_{nc}$ is only equal to 1, for the data points that belong to class $\mathcal{C}\_c$. Which means that the sum on the left-hand side of $(6)$ only includes input variables $\mathbf{x}$ that belong to class $\mathcal{C}\_c$. Afterwards we're dividing that sum of vectors with the number of data points in the class $N\_c$, which is the same as taking the average of the vectors. This means that the class-specific mean vector $\boldsymbol{\mu}\_c$ is the average of the input variables $\mathbf{x}_n$ that belong to the class, i.e., **the class-specific mean vector is just the mean of the vectors of the class**. Once again, this makes intuitive sense as well.

Lastly, we have to maximize the log-likelihood with respect to the class-specific covariance matrix $\mathbf{\Sigma}_c$. Again, we take the derivative with respect to $\mathbf{\Sigma}_c$ using the result from $(2)$, set it equal to 0, and solve

$$ \begin{aligned}
\frac{\partial}{\partial \mathbf{\Sigma}_c} \left(
  \ln \text{Pr} \left( \textbf{\textsf{t}} | \boldsymbol{\phi} \right)
\right)
&= 0 \\
\sum_{n=1}^N
\frac{\partial}{\partial \mathbf{\Sigma}_c} \left(
  \frac{t_{nc}}{2} \ln \det{\mathbf{\Sigma}_c^{-1}}
  -\frac{t_{nc}}{2} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right)
&= 0 \\
\sum_{n=1}^N
\frac{t_{nc}}{2}
\frac{\partial}{\partial \mathbf{\Sigma}_c} \left(
  \ln \det{\mathbf{\Sigma}_c^{-1}}
  -\left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right)
&= 0.
\end{aligned} $$

This derivative requires a bit more work. Firstly, we can use the following [identity](https://en.wikipedia.org/wiki/Matrix_calculus#Scalar-by-vector_identities):

> *If $a$ is not a function of $\mathbf{A}$, then $\frac{\partial \ln \det a\mathbf{A}}{\partial \mathbf{A}} = \mathbf{A}^{-1}$.*

This takes care of the first part. Secondly, we use a [property of the trace of a product](https://en.wikipedia.org/wiki/Trace_(linear_algebra)#Trace_of_a_product):

> *If $\mathbf{u}$ is a column vector, then $\mathbf{u}^\intercal \mathbf{A} \mathbf{u} = \text{tr} \left( \mathbf{u}^\intercal \mathbf{u} \mathbf{A} \right)$.*

Finally, we use another [matrix calculus identity](https://en.wikipedia.org/wiki/Matrix_calculus#Scalar-by-vector_identities):

> *If $\mathbf{B}$ is not a function of $\mathbf{A}$, then $\frac{\partial \text{tr}\left( \mathbf{B} \mathbf{A} \right)}{\partial \mathbf{A}} = \mathbf{B}^\intercal$.*

This now gives us

$$ \begin{aligned}
\sum_{n=1}^N
\frac{t_{nc}}{2}
\frac{\partial}{\partial \mathbf{\Sigma}_c} \left(
  \ln \det{\mathbf{\Sigma}_c^{-1}}
  -\left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)
\right)
&= 0 \\
\sum_{n=1}^N
t_{nc}
\left(
  \mathbf{\Sigma}_c
  -\frac{\partial}{\partial \mathbf{\Sigma}_c} \left(
    \text{tr} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right) \mathbf{\Sigma}_c^{-1}
  \right)
\right)
&= 0 \\
\sum_{n=1}^N
t_{nc}
\left(
  \mathbf{\Sigma}_c
  -\left( \mathbf{x}_n - \boldsymbol{\mu}_c \right) \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal
\right)
&= 0 \\
\sum_{n=1}^N t_{nc} \mathbf{\Sigma}_c
&= \sum_{n=1}^N t_{nc} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right) \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal \\
\mathbf{\Sigma}_c
&= \frac{1}{N_c} \sum_{n=1}^N t_{nc} \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right) \left( \mathbf{x}_n - \boldsymbol{\mu}_c \right)^\intercal. \quad \quad (7)
\end{aligned} $$

Just like the class-specific mean vector is just the mean of the vectors of the class, **the class-specific covariance matrix is just the covariance of the vectors of the class**, and we end up with our maximum likelihood solutions $(5)$, $(6)$, and $(7)$. Thus, we can classify using the following

$$
\hat{h} (\mathbf{x}) = \underset{c}{\text{argmax }} \ln \pi_c +\frac{1}{2} \ln \det{\mathbf{\Sigma}_c^{-1}} -\frac{1}{2} \left( \mathbf{x} - \boldsymbol{\mu}_c \right)^\intercal \mathbf{\Sigma}_c^{-1} \left( \mathbf{x} - \boldsymbol{\mu}_c \right). \quad \quad (8)
$$


### Python implementation
Let's start with some data - you can see it in the plot underneath. You can download the data [here](https://github.com/cookieblues/cookieblues.github.io/raw/master/extra/bsmalea-notes-3b/data.csv).

<img src="{{ site.url }}/extra/bsmalea-notes-3b/data.svg">
{: style="text-align: center"}

The code underneath is a simple implementation of QDA that we just went over.

{% highlight python %}
import numpy

class QDA:
    def fit(self, X, t):
        self.priors = dict()
        self.means = dict()
        self.covs = dict()
        
        self.classes = np.unique(t)

        for c in self.classes:
            X_c = X[t == c]
            self.priors[c] = X_c.shape[0] / X.shape[0]
            self.means[c] = np.mean(X_c, axis=0)
            self.covs[c] = np.cov(X_c, rowvar=False)

    def predict(self, X):
        preds = list()
        for x in X:
            posts = list()
            for c in self.classes:
                prior = np.log(self.priors[c])
                inv_cov = np.linalg.inv(self.covs[c])
                inv_cov_det = np.linalg.det(inv_cov)
                diff = x-self.means[c]
                likelihood = 0.5*np.log(inv_cov_det) - 0.5*diff.T @ inv_cov @ diff
                post = prior + likelihood
                posts.append(post)
            pred = self.classes[np.argmax(posts)]
            preds.append(pred)
        return np.array(preds)
{% endhighlight %}

We can now make predictions with the following code.

{% highlight python %}
data = np.loadtxt("../data.csv", delimiter=",", skiprows=1)

X = data[:, 0:2]
t = data[:, 2]

qda = QDA()
qda.fit(X, t)
preds = qda.predict(X)
{% endhighlight %}

This gives us the Gaussian distributions along with predictions.

<img src="{{ site.url }}/extra/bsmalea-notes-3b/qda/preds.svg">
{: style="text-align: center"}

To make it easier for us to illustrate, how QDA works and how well it works, we can chart the original classes of the data points over the decision boundaries. This is shown underneath.

<img src="{{ site.url }}/extra/bsmalea-notes-3b/qda/decision_boundary.svg">
{: style="text-align: center"}

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