---
date: 2021-03-23
title: "Machine learning, notes 3a: Classification"
categories:
  - Guides
featured_image: https://raw.githubusercontent.com/cookieblues/cookieblues.github.io/33c1f7b6dbd05a952e9c9d381173195dce89fc52/extra/bsmalea-notes-2/prob_linreg.svg
---
As mentioned in <a href="{{ site.url }}/guides/2021/03/08/bsmalea-notes-1a">notes 1a</a>, in classification the possible values for the target variables are discrete, and we call these possible values "classes". In <a href="{{ site.url }}/guides/2021/03/22/bsmalea-notes-2">notes 2</a> we went through regression, which in short refers to constructing a function $h( \mathbf{x} )$ from a dataset $\mathbf{X} = \left( (\mathbf{x}_1, t_1), \dots, (\mathbf{x}_N, t_N) \right)$ that yields prediction values $t$ for new values of $\mathbf{x}$. The objective in classification is the same, except the values of $t$ are discrete.

We are going to cover 3 different approaches or types of classifiers:

- **Generative classifiers** that model the joint probability distribution of the input and target variables $p(\mathbf{x}, t)$.
- **Discriminative classifiers** that model the conditional probability distribution of the target given an input variable $p(t \| \mathbf{x})$.
- **Distribution-free classifiers** that do not use a probability model but directly assign input to target variables.

A quick disclaimer for this topic: **the terminology will be very confusing**, but we'll deal with that when we cross those bridges.


## Generative vs discriminative
Here's the list of classifiers that we will go over: for **generative classifiers** it's **quadratic discriminant analysis (QDA)**, **linear discriminant analysis (LDA)**, and (Gaussian) **naive Bayes**, which are all special cases of the same model; for **discriminative classiferis** it's **logistic regression**; and for **distribution-free classifiers** we will take a look at the **perceptron** but also the **support vector machine (SVM)**.

So, they all do the same thing (classification). Which one is the best? Which one should you use? Well, let's recall <a href="{{ site.url }}/guides/2021/03/11/bsmalea-notes-1b/">the "no free lunch" theorem</a>, which broadly states that there isn't one model that is always better than another. It always depends on your data. That being said, there are some things we can generally say about generative and discriminative classifiers. Ng and Jordan (2002) found that repeating the experiment of applying naive Bayes and logistic regression on binary classification tasks, **naive Bayes (generative) performed better with less data, but logistic regression tended to perform better in general**<span class="sidenote-number"></span><span class="sidenote">Andrew Y. Ng and Michael I. Jordan, "On Discriminative vs. Generative classifiers: A comparison of logistic regression and naive Bayes," 2001.</span>. However, Ulusoy and Bishop (2006) notes that **this is only the case, when the data follow the assumptions of the generative model**<span class="sidenote-number"></span><span class="sidenote">Ilkay Ulusoy and Christopher Bishop, "Comparison of Generative and Discriminative Techniques for Object Detection and Classification," 2006.</span>, which means that logistic regression (discriminative) is generally better than naive Bayes (generative).

**The general consensus is that discriminative models outperform generative models in most cases**. The reason for this is that generative models in some way has a more difficult job, as they try to model the joint distribution instead of just the posterior. They also often times make unrealistic assumptions about the data. Yet, it cannot be stressed enough though that is not always the case, and **you should not disregard generative models**. As an example, generative adversarial networks (GANs) are generative models that have proved extremely useful in a variety of tasks. There are a few other reasons why you shouldn't disregard generative models, e.g. they tend to be easier to fit. Regardless, we're not here to figure out, which model to use, but to learn about both.

## Important tools
### Multivariate Gaussian distribution
In the following posts, we are going to rely heavily on the multivariate Gaussian (normal) distribution, and it's very important that you grasp it. The multivariate Gaussian distribution is denoted $\mathcal{N} (\boldsymbol{\mu}, \mathbf{\Sigma})$, where $\boldsymbol{\mu}$ is the mean vector and $\mathbf{\Sigma}$ is the covariance matrix.


### Bayes' theorem
Another important tool we are going to use is Bayes' theorem. If you haven't read the <a href="{{ site.url }}/guides/2021/03/15/bsmalea-notes-1c/">post on frequentism and Bayesianism</a>, then here's a quick recap on Bayes' theorem. Given 2 events $\mathcal{A}$ and $\mathcal{B}$, we can expand their joint probability with conditional probabilities

$$
\text{Pr} (\mathcal{A}, \mathcal{B}) = \text{Pr} (\mathcal{A} | \mathcal{B}) \text{Pr} (\mathcal{B}) = \text{Pr} (\mathcal{B} | \mathcal{A}) \text{Pr} (\mathcal{A}).
$$

Using the equation on the right, we can rewrite it and get Bayes' theorem

$$ \begin{aligned}
\text{Pr} (\mathcal{A} | \mathcal{B}) \text{Pr} (\mathcal{B})
&= \text{Pr} (\mathcal{B} | \mathcal{A}) \text{Pr} (\mathcal{A}) \\
\text{Pr} (\mathcal{A} | \mathcal{B})
&= \frac{\text{Pr} (\mathcal{B} | \mathcal{A}) \text{Pr} (\mathcal{A})}{\text{Pr} (\mathcal{B})}.
\end{aligned} $$

In terms of a hypothesis and data, we often use the words posterior, likelihood, prior, and evidence to refer to the parts of Bayes' theorem

$$
\overbrace{\text{Pr}(\mathcal{\text{hypothesis}} | \mathcal{\text{data}})}^{\text{posterior}}
= \frac{ \overbrace{\text{Pr}(\mathcal{\text{data}} | \mathcal{\text{hypothesis}})}^{\text{likelihood}} \, \overbrace{\text{Pr}(\mathcal{\text{hypothesis}})}^{\text{prior}} }{ \underbrace{\text{Pr}(\mathcal{\text{data}})}_{\text{evidence}} }.
$$

We often write this as

$$
\text{posterior} \propto \text{likelihood} \times \text{prior},
$$

where $\propto$ means "proportional to".

