---
date: 2021-03-15
title: "Machine learning, notes 1c: Frequentism and Bayesianism"
categories:
  - Guides
featured_image: https://raw.githubusercontent.com/cookieblues/cookieblues.github.io/master/extra/bsmalea-notes-1c/test.png
---
As mentioned in <a href="{{ site.url }}/guides/2021/03/08/bsmalea-notes-1a/">notes 1a</a>, machine learning is mainly concerned with prediction, and as you can imagine, prediction is very much concerned with probability. In this post we are going to look at the two main [interpretations of probability](https://en.wikipedia.org/wiki/Probability_interpretations){:target="_blank"}: frequentism and Bayesianism.

While the adjective "Bayesian" first appeared around the 1950s by R. A. Fisher<span class="sidenote-number"></span><span class="sidenote">S. E. Fienberg, "When did Bayesian inference become "Bayesian"?," 2006.</span>, the concept was properly formalized long before by P. S. Laplace in the 18th century, but known as "inverse probability"<span class="sidenote-number"></span><span class="sidenote">S. M. Stigler, "The History of Statistics: The Measurement of Uncertainty Before 1900," ch. 3, 1986.</span>. So while the gist of the Bayesian approach has been known for a while, it hasn't gained much popularity until recently (last few decades), perhaps mostly due to computational complexity.

The philosophical difference between the frequentist and Bayesian interpretation of probability is their definitions of probability: **the frequentist (or classical) definition of probability is based on frequencies of events**, whereas **the Bayesian definition of probability is based on our knowledge of events**. In the context of machine learning, we can interpret this difference as: what the data says versus what we know from the data.

To understand what this means, I like to use [this analogy](https://stats.stackexchange.com/a/56){:target="_blank"}. Imagine you've lost your phone somewhere in your home. You use your friend's phone to call your phone - as it's calling, your phone starts ringing (it's not on vibrate). How do you decide, where to look for your phone in your home? **The frequentist would use their ears to identify the most likely area from which the sound is coming**. However, **the Bayesian would also use their ears, but in addition they would recall which areas of their home they've previously lost their phone and take it into account**, when inferring where to look for the phone. Both the frequentist and the Bayesian use their ears when inferring, where to look for the phone, but the Bayesian also incorporates **prior knowledge** about the lost phone into their inference.

It's important to note that there's nothing stopping the frequentist from also incorporating the prior knowledge in some way. It's usually more difficult though. The frequentist is really at a loss though, if the event hasn't happened before and there's no way to repeat it numerous times. A classic example is predicting if the Arctic ice pack will have melted by some year, which will happen either once or never. Even though it's not possible to repeat the event numerous times, we do have prior knowledge about the ice cap, and it would be unscientific not to include it.

### Bayes' theorem
Hopefully, these last paragraphs haven't confused you more than they've enlightened, because now we turn to formalizing the Bayesian approach - and to do this, we need to talk about **Bayes' theorem**. Let's say we have two sets of outcomes $\mathcal{A}$ and $\mathcal{B}$ (also called events). We denote the probabilities of each event $\text{Pr}(\mathcal{A})$ and $\text{Pr}(\mathcal{B})$ respectively. The probability of both events is denoted with the joint probability $\text{Pr}(\mathcal{A},\mathcal{B})$, and we can expand this with conditional probabilities

$$
\text{Pr}(\mathcal{A},\mathcal{B}) = \text{Pr}(\mathcal{A}|\mathcal{B}) \text{Pr}(\mathcal{B}), \quad \quad (1)
$$

i.e., the conditional probability of $\mathcal{A}$ given $\mathcal{B}$ and the probability of $\mathcal{B}$ gives us the joint probability of $\mathcal{A}$ and $\mathcal{B}$. It follows that

$$
\text{Pr}(\mathcal{A},\mathcal{B}) = \text{Pr}(\mathcal{B}|\mathcal{A}) \text{Pr}(\mathcal{A}) \quad \quad (2)
$$

as well. Since the left-hand sides of $(1)$ and $(2)$ are the same, we can see that the right-hand sides are equal

$$ \begin{aligned}
\text{Pr}(\mathcal{A}|\mathcal{B}) \text{Pr}(\mathcal{B}) &= \text{Pr}(\mathcal{B}|\mathcal{A}) \text{Pr}(\mathcal{A}) \\
\text{Pr}(\mathcal{A} | \mathcal{B}) &= \frac{\text{Pr}(\mathcal{B} | \mathcal{A}) \text{Pr}(\mathcal{A})}{\text{Pr}(\mathcal{B})},
\end{aligned} $$

which is Bayes' theorem. This should seem familiar to you - if not, I'd recommend reading up on some basics of probability theory before moving on.

We're calculating the conditional probability of $\mathcal{A}$ given $\mathcal{B}$ from the conditional probability of $\mathcal{B}$ given $\mathcal{A}$ and the respective probabilities of $\mathcal{A}$ and $\mathcal{B}$. However, it might not be clear-cut, why this is so important in machine learning, so let's write Bayes' theorem in a more 'data sciencey' way:

$$
\overbrace{\text{Pr}(\mathcal{\text{hypothesis}} | \mathcal{\text{data}})}^{\text{posterior}}
= \frac{ \overbrace{\text{Pr}(\mathcal{\text{data}} | \mathcal{\text{hypothesis}})}^{\text{likelihood}} \, \overbrace{\text{Pr}(\mathcal{\text{hypothesis}})}^{\text{prior}} }{ \underbrace{\text{Pr}(\mathcal{\text{data}})}_{\text{evidence}} }.
$$

Usually, we're not just dealing with probabilities but probability distributions, and the evidence (the denominator above) ensures that the posterior distribution on the left-hand side is a valid probability density and is called the [normalizing constant](https://en.wikipedia.org/wiki/Normalizing_constant)<span class="marginnote">A normalizing constant just ensures that any probability function is a probability density function with total probability of 1.</span>. Since it's just a normalizing constant though, we often state the theorem in words as

$$
\text{posterior} \propto \text{likelihood} \times \text{prior},
$$

where $\propto$ means "proportional to".
<!-- Note that if we assume what's called a *flat* prior, i.e., a prior that is ambivalent towards the hypothesis, then the posterior is proportional to the likelihood, and we end up with the frequentist approach; maximum likelihood. -->

### Example: coin flipping
We'll start with [a simple example](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html){:target="_blank"} that I think nicely illustrates the difference between the frequentist and Bayesian approach. Consider the following problem:

*A coin flips heads up with probability $\theta$ and tails with probability $1-\theta$ ($\theta$ is unknown). You flip the coin 11 times, and it ends up heads 8 times. Now, would you bet for or against the event that the next two tosses turn up heads?*

For our sake, let's define some variables. Let $X$ be a random variable representing the coin, where $X=1$ is heads and $X=0$ is tails such that $\text{Pr}(X=1) = \theta$ and $\text{Pr}(X=0) = 1-\theta$. Furthermore, let $\mathcal{D}$ denote our observed data (8 heads, 3 tails). Now, we want to estimate the value of the parameter $\theta$, so that we can calculate the probability of seeing 2 heads in a row. If the probability is less than 0.5, we will bet against seeing 2 heads in a row, but if it's above 0.5, then we bet for. So let's look at how the frequentist and Bayesian would estimate $\theta$!

#### Frequentist approach
**As the frequentist, we want to maximize the likelihood**, which is to ask the question: what value of $\theta$ will maximize the probability that we got $\mathcal{D}$ given $\theta$, or more formally, we want to find

$$
\hat{\theta}_{\text{MLE}} = \underset{\theta}{\arg\max} \text{Pr}(\mathcal{D} | \theta).
$$

This is called [maximum likelihood estimation (MLE)](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation). The experiment of flipping the coin 11 times follows a binomial distribution with $n=11$ trials, $k=8$ successes, and $\theta$ the probability of succes. Using the likelihood of a binomial distribution, we can find the value of $\theta$ that maximizes the probability of the data. We therefore want to find the value of $\theta$ that maximizes

$$
\text{Pr}(\mathcal{D} | \theta) = \mathcal{L}(\theta | \mathcal{D}) = \begin{pmatrix} 11\\8 \end{pmatrix} \theta^{8} (1-\theta)^{11-8}. \quad \quad (3)
$$

Note that $(3)$ expresses the *likelihood* of $\theta$ given $\mathcal{D}$, which is not the same as saying the probability of $\theta$ given $\mathcal{D}$. The image underneath shows our likelihood function $\text{Pr}(\mathcal{D} \| \theta)$ (as a function of $\theta$) and the maximum likelihood estimate $\hat{\theta}_{\mathrm{MLE}}$.

<img src="{{ site.url }}/extra/bsmalea-notes-1c/frequentist_likelihood.svg">
{: style="text-align: center"}

Unsurprisingly, the value of $\theta$ that maximizes the likelihood is $\frac{k}{n}$, i.e., the proportion of successes in the trials.
<!--
We've derived this result in a <a href="{{ site.url }}/pages/bslialo-notes-9b">different post</a>. This is also called the [maximum likelihood estimate](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation){:target="_blank"} for $\theta$. 
-->
The maximum likelihood estimate $\hat{\theta}_{\text{MLE}}$ is therefore $\frac{k}{n} = \frac{8}{11} \approx 0.73$. Assuming the coin flips are independent, we can calculate the probability of seeing 2 heads in a row:

$$
\text{Pr}(X=1) \times \text{Pr}(X=1) = \hat{\theta}_{\text{MLE}}^2 = \left( \frac{8}{11} \right)^2 \approx 0.53.
$$

Since the probability of seeing 2 heads in a row is larger than 0.5, we would bet for!

#### Bayesian approach
**As the Bayesian, we want to maximize the posterior**, so we ask the question: what value of $\theta$ will maximize the probability of $\theta$ given $\mathcal{D}$? Formally, we get

$$
\hat{\theta}_{\text{MAP}} = \underset{\theta}{\arg\max} \text{Pr}(\theta | \mathcal{D}),
$$

which is called [maximum a posteriori (MAP) estimation](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation). To answer the question, we use Bayes' theorem

$$ \begin{aligned}
\hat{\theta}_{\text{MAP}}
&= \underset{\theta}{\arg\max} \overbrace{\text{Pr}(\theta | \mathcal{D})}^{\text{posterior}} \\
&= \underset{\theta}{\arg\max} \frac{
  \overbrace{\text{Pr}(\mathcal{D} | \theta)}^{\text{likelihood}} \, \overbrace{\text{Pr}(\theta)}^{\text{prior}}
}{
  \underbrace{\text{Pr}(\mathcal{D})}_{\text{evidence}}
}.
\end{aligned} $$

Since the evidence $\text{Pr}(\mathcal{D})$ is a normalizing constant not dependent on $\theta$, we can ignore it.  This now gives us

$$
\hat{\theta}_{\text{MAP}} = \underset{\theta}{\arg\max} \text{Pr}(\mathcal{D}|\theta) \, \text{Pr}(\theta).
$$

During the frequentist approach, we already found the likelihood $(3)$

$$
\text{Pr}(\mathcal{D}|\theta) = \begin{pmatrix} 11\\8 \end{pmatrix} \theta^{8} (1-\theta)^{3},
$$

where we can drop the binomial coefficient, since it's not dependent on $\theta$. The only thing left is the prior distribution $\text{Pr}(\theta)$. This distribution describes our initial (prior) knowledge of $\theta$. A convenient distribution to choose is the [Beta distribution](https://en.wikipedia.org/wiki/Beta_distribution), because it's defined on the interval [0, 1], and $\theta$ is a probability, which has to be between 0 and 1. <span class=marginnote>Additionally, the Beta distribution is the [conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior) for the binomial distribution, which broadly means that if the posterior and prior distributions are in the same family, then the prior is the conjugate prior for the likelihood. This is often times a desired property.</span> This gives us

$$
\text{Pr}(\theta) = \frac{\Gamma (\alpha) \Gamma (\beta)}{\Gamma (\alpha+\beta)} \theta^{\alpha-1} (1-\theta)^{\beta-1},
$$

where $\Gamma$ is the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function)<span class="marginnote">The Gamma function is defined as $\Gamma (n) = (n-1)!$ for any positive integer $n$.</span>. Since the fraction is not dependent on $\theta$, we can ignore it, which gives us

$$ \begin{aligned}
\text{Pr}(\theta | \mathcal{D})
&\propto \theta^{8} (1-\theta)^{3} \theta^{\alpha-1} (1-\theta)^{\beta-1} \\
&\propto \theta^{\alpha+7} (1-\theta)^{\beta+2}. \quad \quad (4)
\end{aligned} $$

Note that we end up with another beta distribution (without the normalizing constant). 

It is now our job to set the prior distribution in such a way that we incorporate, what we know about $\theta$ *prior* to seeing the data. Now, we know that coins are usually pretty fair, and if we choose $\alpha = \beta = 2$, we get a beta distribution that favors $\theta=0.5$ more than $\theta = 0$ or $\theta =1$. The illustration below shows this prior $\mathrm{Beta}(2, 2)$, the normalized likelihood, and the resulting posterior distribution.

<img src="{{ site.url }}/extra/bsmalea-notes-1c/prior_a_b_2.svg">
{: style="text-align: center"}

We can see that the posterior distribution ends up being dragged a little more towards the prior distribution, which makes the MAP estimate a little different the MLE estimate. In fact, we get

$$
\hat{\theta}_{\text{MAP}} = \frac{\alpha + k - 1}{\alpha + \beta + n - 2} = \frac{2+8-1}{2+2+11-2} = \frac{9}{13} \approx 0.69,
$$

which is a little lower than the MLE estimate - and if we now use the MAP estimate to calculate the probability of seeing 2 heads in a row, we find that we will **bet against** it

$$
\text{Pr}(X=1) \times \text{Pr}(X=1) = \hat{\theta}_{\text{MAP}}^2 = \left( \frac{9}{13} \right)^2 \approx 0.48.
$$

Furthermore, if we were to choose $\alpha=\beta=1$, we get the special case where the beta distribution is a uniform distribution. In this case, our MAP and MLE estimates are the same, and we make the same bet. The image underneath shows the prior, likelihood, and posterior for different values of $\alpha$ and $\beta$, i.e., for different prior distributions.

<img src="{{ site.url }}/extra/bsmalea-notes-1c/different_priors.svg">
{: style="text-align: center"}


#### Fully Bayesian approach
While we did include a prior distribution in the previous approach, we're still collapsing the distribution into a point estimate and using that estimate to calculate the probability of 2 heads in a row. However, in a truly Bayesian approach, we wouldn't do this, as we don't just have a single estimate of $\theta$ but a whole distribution (the posterior). Let $\mathcal{H}$ denote the event of seeing 2 heads in a row - then we ask: what is the probability of seeing 2 heads given the data, i.e., $\text{Pr}(\mathcal{H} \| \mathcal{D})$? To answer this question, we first need to find the normalizing constant for the posterior distribution in $(4)$. Since it's a beta distribution, we can look at $(4)$ and see that it must be $\frac{\Gamma(\alpha+\beta+11)}{\Gamma(\alpha+8)\Gamma(\beta+3)}$. Like earlier, we'll also assume that the coin tosses are independent, which means that the probability of seeing 2 heads in a row (given $\theta$ and the data) is just equal to the probability of seeing heads squared, i.e, $\mathrm{Pr} (\mathcal{H} | \theta, \mathcal{D}) = \theta^2$.

We can now answer this question by 'integrating out' $\theta$ as

$$ \begin{aligned}
\mathrm{Pr}(\mathcal{H} | \mathcal{D})
&= \int_{\theta} \mathrm{Pr} (\mathcal{H}, \theta | \mathcal{D}) \, \mathrm{d}\theta \\
&= \int_{\theta} \mathrm{Pr} (\mathcal{H} | \theta, \mathcal{D}) \, \overbrace{\mathrm{Pr} (\theta | \mathcal{D})}^{\mathrm{posterior}} \, \mathrm{d}\theta \\
&= \int_0^1 \theta^2 \, \overbrace{\frac{\Gamma(\alpha+\beta+11)}{\Gamma(\alpha+8)\Gamma(\beta+3)}}^{\text{normalizing constant}} \, \theta^{\alpha+7} (1-\theta)^{\beta+2} \, \mathrm{d}\theta \\
&= \frac{\Gamma(\alpha+\beta+11)}{\Gamma(\alpha+8)\Gamma(\beta+3)} \int_0^1 \theta^{\alpha+9} (1-\theta)^{\beta+2} \, \mathrm{d}\theta \\
&= \frac{\Gamma(\alpha+\beta+11)}{\Gamma(\alpha+8)\Gamma(\beta+3)} \frac{\Gamma(\alpha+10)\Gamma(\beta+3)}{\Gamma(\alpha+\beta+13)} \\
&= \frac{(\alpha+8)(\alpha+9)}{(\alpha+\beta+11)(\alpha+\beta+12)}.
\end{aligned} $$

In this case, if we choose a uniform prior, i.e., $\alpha=\beta=1$, we actually get $\frac{45}{91} \approx 0.49$, so we would bet against. The reason for this is more complicated and has to do with the uniform prior not being completely agnostic<span class="marginnote">A better choice of prior would be [Haldane's prior](https://en.wikipedia.org/wiki/Beta_distribution#Haldane's_prior_probability_(Beta(0,0))), which is the $\mathrm{Beta}(0, 0)$ distribution.</span>. Furthermore, we've also made the implicit decision not to update our posterior distribution between the 2 tosses, we're predicting. You can imagine, we would gain knowledge about the fairness of the coin (i.e., about $\theta$) after tossing the coin the first time, which we could use to update our posterior distribution. However, to simplify the calculations we haven't done that.


### Example: polynomial regression (TBA)
<!--
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
-->

<!--
https://m-clark.github.io/bayesian-basics/intro.html
https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html
https://github.com/jsantarc/Bayesian-regression-with-Infinitely-Broad-Prior-Gaussian-Parameter-Distribution-
http://jakevdp.github.io/blog/2014/06/14/frequentism-and-bayesianism-4-bayesian-in-python/
https://www.ics.uci.edu/~smyth/courses/cs274/readings/bayesian_regression_overview.pdf
-->

