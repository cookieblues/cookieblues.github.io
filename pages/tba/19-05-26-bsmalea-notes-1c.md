---
title: "BSMALEA, notes 1c: Frequentism and Bayesianism"
layout: post
tags: BSMALEA
excerpt_separator: <!--more-->
---
As mentioned in <a href="{{ site.url }}/pages/bsmalea-notes-1a">notes 1a</a>, machine learning is mainly concerned with prediction, and as you can imagine, prediction is very much concerned with probability. In this post we are going to look at the two main [interpretations of probability](https://en.wikipedia.org/wiki/Probability_interpretations){:target="_blank"}: Frequentism and Bayesianism.

While the adjective "Bayesian" first appeared around the 1950s by R. A. Fisher[^1], the concept was properly formalized long before by P. S. Laplace and known as "inverse probability"[^2]. So while the gist of the Bayesian approach has been known for a while, it hasn't gained much popularity until recently, perhaps mostly due to computational complexity.

The philosophical difference between the frequentist and Bayesian interpretation of probability is their definitions of probability: the frequentist (or classical) definition of probability is based on **frequencies of events**, whereas the Bayesian definition of probability is based on **our knowledge of events**. In the context of machine learning, the difference can be interpreted as: what the data says versus what we know from the data.

To understand what this means, I like [this analogy](https://stats.stackexchange.com/a/56){:target="_blank"}: imagine you've lost your phone somewhere in your home. You use your friend's phone to call your phone - as it's calling, your phone starts ringing (it's not on vibrate). How do you decide, where to look for your phone in your home? The frequentist would use their ears to identify the most likely area from which the sound is coming, which would be where the phone is located. The Bayesian would also use their ears, but in addition they would recall which areas of their home they've previously lost their phone and take it into account, when inferring where to look for the phone.

<!--more-->

It's important to note that there's nothing stopping the frequentist from incorporating the prior knowledge in some way. Dependent on the problem at hand though, it might be easier or it might be more difficult. The frequentist is really at a loss though, if the event hasn't happened before and there's no way to repeat it numerous times. A classic example is predicting if the Arctic ice pack will have melted by some year, which will happen either once or never. Even though it's not possible to repeat the event numerous times, we do have prior knowledge about the ice cap, and it would be unscientific not to include it.

### Bayes' theorem
Hopefully, these last paragraphs haven't confused you more than they've enlightened, because now we turn to formalizing the Bayesian approach - and to do this, we need to talk about **Bayes' theorem**. Let's say we have two sets of outcomes $\mathcal{A}$ and $\mathcal{B}$, also called events. We denote the probabilities of each event $p(\mathcal{A})$ and $p(\mathcal{B})$ respectively. The probability of both events is denoted with the joint probability $p(\mathcal{A},\mathcal{B})$, and we can expand this with conditional probabilities

$$
p(\mathcal{A},\mathcal{B}) = p(\mathcal{A}|\mathcal{B}) p(\mathcal{B}), \quad \quad (1)
$$

i.e. the conditional probability of $\mathcal{A}$ given $\mathcal{B}$ and the probability of $\mathcal{B}$ gives us the joint probability of $\mathcal{A}$ and $\mathcal{B}$. This works the other way around too

$$
p(\mathcal{A},\mathcal{B}) = p(\mathcal{B}|\mathcal{A}) p(\mathcal{A}). \quad \quad (2)
$$

Since the left-hand sides of $(1)$ and $(2)$ are the same, we can see that the right-hand sides are equal

$$ \begin{aligned}
p(\mathcal{A}|\mathcal{B}) p(\mathcal{B}) &= p(\mathcal{B}|\mathcal{A}) p(\mathcal{A}) \\
p(\mathcal{A} | \mathcal{B}) &= \frac{p(\mathcal{B} | \mathcal{A}) p(\mathcal{A})}{p(\mathcal{B})},
\end{aligned} $$

which is Bayes' theorem and should seem familiar if you're taking this course. We're calculating the conditional probability of $\mathcal{A}$ given $\mathcal{B}$ from the conditional probability of $\mathcal{B}$ given $\mathcal{A}$ and the respective probabilities of $\mathcal{A}$ and $\mathcal{B}$. However, it might not be clear-cut, why this is so important in machine learning, so let's write Bayes' theorem in a different way instead

$$
\overbrace{p(\mathcal{\text{hypothesis}} | \mathcal{\text{data}})}^{\text{posterior}}
= \frac{ \overbrace{p(\mathcal{\text{data}} | \mathcal{\text{hypothesis}})}^{\text{likelihood}} \, \overbrace{p(\mathcal{\text{hypothesis}})}^{\text{prior}} }{ \underbrace{p(\mathcal{\text{data}})}_{\text{evidence}} }.
$$

The evidence ensures that the posterior distribution on the left-hand side is a valid probability density and is called the normalization constant. Since it's just a normalization constant though, we often state the theorem in words as

$$
\text{posterior} \propto \text{likelihood} \times \text{prior},
$$

where $\propto$ means "proportional to". Note that if we assume what's called a *flat* prior, i.e., a prior that is ambivalent towards the hypothesis, then the posterior is proportional to the likelihood, and we end up with the frequentist approach; maximum likelihood.

<!--
### Example: coin flipping
We'll start with [a simple example](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html){:target="_blank"} that I think nicely illustrates the difference between the frequentist and Bayesian approach. Consider the following problem:

*A coin flips heads up with probability $\alpha$ and tails with probability $1-\alpha$ ($\alpha$ is unknown). You flip the coin 35 times, and it ends up head 25 times. Now, would you bet for or against the event that the next two tosses turn up heads?*

For our sake let's define these variables:\\
$\mathcal{H}$ : two heads in a row\\
$\mathcal{D}$ : observed data, i.e. $\mathcal{D} = (n_{\text{head}}, n_{\text{tail}}) = (25, 10)$.

#### Frequentist approach
As the frequentist, we ask the question: what's the probability that we got $\mathcal{D}$ given $\alpha$? More formally, what is $p(\mathcal{D}|\alpha)$? We can consider the experiment as a binomial distribution. We have $n=35$ trials, $k=25$ successes, and $\alpha$ is our probability of succes; using the likelihood of a binomial distribution, we can find the value of $\alpha$ that maximizes the probability of the data. We therefore want to find the value of $\alpha$ that maximizes

$$
\mathcal{L}(\alpha | \mathcal{D}) = \begin{pmatrix} 35\\25 \end{pmatrix} \alpha^{25} (1-\alpha)^{35-25}. \quad \quad (3)
$$

Note that $(3)$ expresses the *likelihood* of $\alpha$ given $\mathcal{D}$, which is not the same as saying the probability of $\alpha$ given $\mathcal{D}$ - we can apply Bayes' theorem to answer that question, but we'll get to that later on. Unsurprisingly the value of $\alpha$ that maximizes $\mathcal{L}$ is $\frac{k}{n}$, i.e. the proportion of successes in the trials. We've derived this result in a <a href="{{ site.url }}/pages/bslialo-notes-9b">different post</a>. This is also called the [maximum likelihood estimate](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation){:target="_blank"} for $\alpha$. 

The maximum likelihood estimate for $\alpha$ is therefore $\frac{k}{n} = \frac{25}{35} \approx 0.71$, which in turn gives us the answer to our question:

$$
p(\mathcal{H}) = \alpha^2 = \left( \frac{25}{35} \right)^2 \approx 0.51.
$$

Since we find, there's a higher probability that the event happens than not, then we would bet for the event!


#### Bayesian approach
As the bayesian, we ask the question: what's the probability of $\alpha$ given $\mathcal{D}$? Now we treat $\alpha$ as a distribution. To answer the question, we use Bayes' theorem

$$
\overbrace{p(\alpha | \mathcal{D})}^{\text{posterior}}
= \frac{ \overbrace{p(\mathcal{D}|\alpha)}^{\text{likelihood}} \, \overbrace{p(\alpha)}^{\text{prior}}}
{ \underbrace{p(\mathcal{D})}_{\text{evidence}} }.
$$

$$ \begin{aligned}
p(\mathcal{H}, \alpha | \mathcal{D})
&= \int_0^1 p(\mathcal{H}, \alpha | \mathcal{D}) \mathrm{d}\alpha \\
&= \int_0^1 p(\mathcal{H} | \alpha, \mathcal{D}) p(\alpha | \mathcal{D}) \mathrm{d}\alpha \\
&= \int_0^1 p(\mathcal{H} | \alpha, \mathcal{D}) \frac{p(\mathcal{D}|\alpha) p(\alpha)}{p(\mathcal{D})} \mathrm{d}\alpha \\
&=  \frac{ \int_0^1 p(\mathcal{H} | \alpha, \mathcal{D}) p(\mathcal{D}|\alpha) p(\alpha) \mathrm{d}\alpha}{\int_0^1 p(\mathcal{D}|\alpha) p(\alpha) \mathrm{d}\alpha}
\end{aligned} $$

$$
p(\mathcal{D}) = \int_0^1 p(\mathcal{D}|\alpha) \mathrm{d}\alpha
$$
-->


### Example: polynomial regression
Let's continue with the example from <a href="{{ site.url }}/pages/bsmalea-notes-1a">notes 1a</a> and look at it from a probabilistic perspective. We'll start with the frequentist perspective and then gradually move on to the fully Bayesian perspective.

To quickly refresh our memory: we had a dataset $\mathcal{D} = \{ (x_1, t_1), \dots, (x_N, t_N) \}$ of $N$ input and target variable pairs. Our objective was to fit a polynomial to the data. We can think about this from a probabilistic perspective by introducing an error term

$$
h(x, \mathbf{w}) = w_0 + w_1 x + w_2 x^2 + \dots + w_M x^M + \epsilon = \sum_{m=0}^M w_m x^m + \epsilon, \quad \quad (3)
$$

where $\epsilon \sim \mathcal{N}\left(\mu, \alpha^{-1} \right)$, and usually we assume the Gaussian has zero mean. What $(3)$ means is that we assume the polynomial we create $h$ 


We can simplify this a bit by defining $\mathbf{w} = \left( w_0, w_1, w_2, \dots, w_M \right)^\intercal$ and $\mathbf{x}_i = \left( 1, x_i, x_i^2, \dots, x_i^M  \right)^\intercal$ such that

$$
h(x, \mathbf{w}) = \mathbf{w}^\intercal \mathbf{x} + \epsilon.
$$

The probability distribution of $t$ given the input variable $\mathbf{x}$, the parameters $\mathbf{w}$, and the precision (inverse variance) $\alpha$ is thus

$$
p(t | x, \mathbf{w}, \alpha) = \mathcal{N} \left(t | h(x, \mathbf{w}), \alpha^{-1} \right).
$$

For the sake of simplicity, let $\textbf{\textsf{x}} = \left\\{ x_1, \dots, x_N \right\\}$ and $\textbf{\textsf{t}} = \left\\{ t_1, \dots, t_N \right\\}$ denote all our input and target variables respectively.

#### Frequentist approach
Assuming the points are independent and identically distributed, we can write up the likelihood function, which is a function of $\mathbf{w}$ and $\alpha$, as

$$
p( \textbf{\textsf{t}} | \textbf{\textsf{x}}, \mathbf{w}, \alpha)
= \prod_{n=1}^N \mathcal{N} \left( t_n | \mathbf{w}^\intercal \mathbf{x}_n, \alpha^{-1} \right).
$$

We want to find the values of $\mathbf{w}$ and $\alpha$ that **maximizes the likelihood**, and as is common in [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation){:target="_blank"} mainly due to computational reasons, we find the maximum of the log-likelihood instead. The log-likelihood is

$$ \begin{aligned}
\ln \left( p( \textbf{\textsf{t}} | \textbf{\textsf{x}}, \mathbf{w}, \alpha) \right)
&= \ln \left( \prod_{n=1}^N \mathcal{N} \left( t_n | \mathbf{w}^\intercal \mathbf{x}_n, \alpha^{-1} \right) \right) \\
&= \sum_{n=1}^N \ln \left( \frac{1}{\sqrt{2\pi\alpha^{-1}}} \exp \left( -\frac{\left(t_n - \mathbf{w}^\intercal \mathbf{x}_n \right)^2}{2\alpha^{-1}} \right) \right) \\
&= \sum_{n=1}^N \left( \ln \frac{1}{\sqrt{2\pi\alpha^{-1}}} - \frac{\left(t_n - \mathbf{w}^\intercal \mathbf{x}_n \right)^2}{2\alpha^{-1}} \right) \\
&= - N \ln \sqrt{2\pi\alpha^{-1}} - \frac{\alpha}{2} \sum_{n=1}^N \left( t_n - \mathbf{w}^\intercal \mathbf{x}_n \right)^2. \quad \quad (4)
\end{aligned} $$

Note that the sum in $(4)$ is equivalent to the objective function we used in <a href="{{ site.url }}/pages/bsmalea-notes-1a">notes 1a</a>, the sum of squared errors (SSE) function, since the left term in $(4)$ is constant with respect to $\mathbf{w}$ - so the solution to $\mathbf{w}$ is the same as in the last post. If we maximize $(4)$ with respect to $\alpha$, we get

$$
\alpha^{-1}_{\text{ML}} = \frac{1}{N} \sum_{n=1}^N \left( t_n - \mathbf{w}_{\text{ML}}^\intercal \mathbf{x}_n \right)^2.
$$

Now that we have determined the maximum likelihood solution for $\mathbf{w}$ and $\alpha$, we can make predictions for new values of $x$ expressed in terms of the **predictive distribution**

$$
p(t|x, \mathbf{w}_\text{ML}, \alpha_\text{ML}) = \mathcal{N} \left( t| h(x, \mathbf{w}_\text{ML}), \alpha^{-1}_\text{ML} \right).
$$

#### Bayesian approach
If we introduce a **prior distribution** over our parameters (the polynomial coefficients) $\mathbf{w}$, we can go from the frequentist perspective to the Bayesian. Remember that the prior is a way for us to incorporate our knowledege about the parameters. Note that it is in this 'subjective' choice, frequentists object to the Bayesian approach. Let's assume a Gaussian prior distribution

$$
p(\mathbf{w} | \beta)
= \mathcal{N} \left( \mathbf{w} | \mathbf{0}, \beta^{-1} \mathbf{I} \right),
$$

where $\beta$ is the precision (inverse variance) of the distribution, $\mathbf{0}$ is the $M+1 \times M+1$ [zero matrix](https://en.wikipedia.org/wiki/Zero_matrix){:target="_blank"}, and $\mathbf{I}$ is the $M+1 \times M+1$ [identity matrix](https://en.wikipedia.org/wiki/Identity_matrix){:target="_blank"}. We can rewrite it by using the [density of the multivariate Gaussian](https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Properties){:target="_blank"}

$$ \begin{aligned}
\mathcal{N} \left( \mathbf{w} | \mathbf{0}, \beta^{-1} \mathbf{I} \right)
&= \frac{1}{\sqrt{(2\pi)^{M+1} |\beta^{-1}\mathbf{I}| }} \exp \left( -\frac{(\mathbf{w}-\mathbf{0})^\intercal (\beta^{-1} \mathbf{I})^{-1} (\mathbf{w}-\mathbf{0})}{2} \right) \\
&= \frac{1}{\left( 2\pi\beta^{-1} \right)^{\frac{M+1}{2}}} \exp \left( -\frac{\mathbf{w}^\intercal (\beta \mathbf{I}) \mathbf{w}}{2} \right) \\
&= \left( \frac{\beta}{2\pi} \right)^{\frac{M+1}{2}} \exp \left( -\frac{\beta}{2} \mathbf{w}^\intercal \mathbf{w} \right). \quad \quad (5)
\end{aligned} $$


Using Bayes' theorem as described above, the posterior distribution of our parameters is proportional to the product of the likelihood function and prior distribution

$$
\overbrace{p(\mathbf{w} | \textbf{\textsf{x}}, \textbf{\textsf{t}}, \alpha, \beta)}^{\text{posterior}}
\propto \overbrace{p(\textbf{\textsf{t}} | \textbf{\textsf{x}}, \mathbf{w}, \alpha)}^{\text{likelihood}} \, \overbrace{p(\mathbf{w}|\beta)}^{\text{prior}}. \quad \quad (6)
$$

By maximizing the posterior distribution we can find the most probable values of $\mathbf{w}$ given the data. This is called the **maximum a posteriori** (MAP) estimate. Note that we're trying to find estimate a point (the maximum) on the posterior distribution, so we don't have to normalize it by dividing by the evidence as mentioned earlier. By taking the logarithm of $(6)$ and substituting $(4)$ and $(5)$ in, we see that maximizing the posterior is given by maximizing

$$ \begin{aligned}
\ln \left( p(\mathbf{w} | \textbf{\textsf{x}}, \textbf{\textsf{t}}, \alpha, \beta) \right)
&\propto \ln \left( p(\textbf{\textsf{t}} | \textbf{\textsf{x}}, \mathbf{w}, \alpha) p(\mathbf{w}|\beta) \right) \\
&= \ln p(\textbf{\textsf{t}} | \textbf{\textsf{x}}, \mathbf{w}, \alpha) + \ln p(\mathbf{w}|\beta) \\
&\propto -\frac{\alpha}{2} \sum_{n=1}^N \left( t_n - \mathbf{w}^\intercal \mathbf{x}_n \right)^2 \underbrace{-\frac{\beta}{2} \mathbf{w}^\intercal \mathbf{w}}_{\text{regularization}}, \quad \quad (7)
\end{aligned} $$

where we have dropped constant terms, since they don't impact the maximum. $(7)$ is almost the same as the sum of squared errors function, but we have the extra term $\frac{\beta}{2} \mathbf{w}^\intercal \mathbf{w}$, which is a **regularization** term. We will discuss regularization further in <a href="{{ site.url }}/pages/bsmalea-notes-2">notes 2</a>, but for now it suffices to say that **regularization is a technique of preventing overfitting**.

#### Fully Bayesian approach
While we've included a prior distribution, we're still calculating what is called a point estimate, i.e. we're finding the maximum of the posterior distribution, but to complete a fully Bayesian approach we would have to find the entire posterior distribution. 


https://m-clark.github.io/bayesian-basics/intro.html
https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html
https://github.com/jsantarc/Bayesian-regression-with-Infinitely-Broad-Prior-Gaussian-Parameter-Distribution-
http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/
https://www.ics.uci.edu/~smyth/courses/cs274/readings/bayesian_regression_overview.pdf



[^1]: S. E. Fienberg, "When did Bayesian inference become "Bayesian"?," 2006. 
[^2]: S. M. Stigler, "The History of Statistics: The Measurement of Uncertainty Before 1900," ch. 3, 1986.