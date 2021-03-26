---
title: "BSMALEA, notes 3b: Generative classifiers"
layout: post
category: Machine Learning
tags: BSMALEA
excerpt_separator: <!--more-->
---
As mentioned in <a href="{{ site.url }}/bsmalea-notes-3a">notes 3a</a>, generative classifiers model the **joint probability distribution** of the input and target variables $p(\mathbf{x}, t)$. This means, we would end up with a distribution that could generate (hence the name) new input variables with their respective targets, i.e. we can sample new data points with the joint probability distribution, and we will see how to do that in this post.

The model, we will be looking at in this post, is the **Gaussian Discriminant Analysis (GDA)**. Now is when the nomenclature starts getting tricky! Note that the Gaussian *Discriminant* Analysis model is a *generative* model! It is *not* a discriminative model despite its name.
<!--more-->

### Setup and objective
Given a training dataset of $N$ input variables $\mathbf{x} \in \mathbb{R}^D$ with corresponding target variables $t \in \mathcal{C}_c$ where $c \in \\{1, \dots, C\\}$, GDA assumes that the class conditional distributions are normally distributed

$$
p(\mathbf{x} \mid t = c, \bm{\theta}) = \mathcal{N} \left( \mathbf{x} \mid \bm{\mu}_c, \mathbf{\Sigma}_c \right),
$$

and uses Bayes' theorem to model the 


the objective of GDA is to assume that 
 the class conditional distributions is distributed by Gaussian distributions, i.e.

$$
p
$$




### Derivation and training


### Model selection







Naive bayes, LDA, QDA


https://www.eecs189.org/static/notes/n18.pdf
https://stats.stackexchange.com/questions/80507/what-is-a-gaussian-discriminant-analysis-gda
https://web.archive.org/web/20200103035702/http://cs229.stanford.edu/notes/cs229-notes2.pdf
https://stats.stackexchange.com/questions/254963/differences-linear-discriminant-analysis-and-gaussian-mixture-model
https://stats.stackexchange.com/questions/190806/sources-seeming-disagreement-on-linear-quadratic-and-fishers-discriminant-ana/190821#190821
https://stats.stackexchange.com/questions/71489/three-versions-of-discriminant-analysis-differences-and-how-to-use-them
https://www.datascienceblog.net/post/machine-learning/linear-discriminant-analysis/