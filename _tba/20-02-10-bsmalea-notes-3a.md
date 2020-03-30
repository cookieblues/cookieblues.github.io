---
title: "BSMALEA, notes 3a: Classification"
layout: post
category: Machine Learning
tags: BSMALEA
excerpt_separator: <!--more-->
---
As mentioned in <a href="{{ site.url }}/bsmalea-notes-1a">notes 1a</a>, in classification the possible values for the target variables are discrete, and we call these possible values "classes". In <a href="{{ site.url }}/bsmalea-notes-2">notes 2</a> we went through regression, which in short refers to constructing a function $h( \mathbf{x} )$ from a dataset $\mathbf{X} = \left( (\mathbf{x}_1, t_1), \dots, (\mathbf{x}_N, t_N) \right)$ that yields prediction values $t$ for new values of $\mathbf{x}$. The objective in classification is the same, except the values of $t$ are discrete.



We are going to cover $3$ different approaches or types of classifiers:

- **Generative classifiers** that model the joint probability distribution of the input and target variables $p(\mathbf{x}, t)$.
- **Discriminative classifiers** that model the conditional probability distribution of the target given an input variable $p(t \| \mathbf{x})$.
- **Distribution-free classifiers** that do not use a probability model but directly assign input to target variables.

A quick disclaimer for this topic: **the nomenclature will be very confusing**, but we'll deal with that when we cross those bridges.



Class conditional distribution.

Bayes theorem.