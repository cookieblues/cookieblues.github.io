---
title: "A look at Machine Learning"
layout: post
tags: BSMALEA
excerpt_separator: <!--more-->
---
This hopefully won't take as long as my notes on <a href="{{ site.url }}/pages/cats/bslialo">Linear Algebra and Optimization</a>, but I will start writing up my notes for the course "[Machine Learning](https://mit.itu.dk/ucs/cb_www/course.sml?course_id=2013612&mode=search&lang=en&print_friendly_p=t&goto=1542111182.000){:target="_blank"}" at the [IT University of Copenhangen](https://www.itu.dk/){:target="_blank"}. My goal is as always to explain the intuition behind the introduced concepts, making it easier to understand and engage with. I believe this can help the few who struggle to understand the concepts, as well as found the concepts for those who know how to employ them but lack the why.

### Overview
If you click the link above, you'll see that there are four intended learning outcomes for the course; the student should be able to:

- **Discuss**, clearly **explain**, and **reflect** upon central machine learning concepts and algorithms.
- **Choose among** and **make use** of the most important machine learning approaches in order to apply (match) them to practical problems.
- **Implement** abstractly specified machine learning methods in an imperative programming language.
- **Combine** and **modify** machine learning methods to **analyse** practical dataset and **convey** the results.

<!--more-->

I believe, these can be summarized in a one-liner: the student should be able to **comprehend**, **apply**, and **tweak** machine learning methods, along with **interpret** the results to **examine** data. To elaborate on this a bit, the course is about understanding mathematical formulations of machine learning methods and programming them, which is why I'll try to incorporate code snippets into these notes. It's important to stress that the course is not a course in any specific machine learning library like TensorFlow, it's not about deep learning, and it's not about deriving models mathematically.

Both statistics and linear algebra are prerequisites for machine learning. Not every little theorem is important, but the overall understanding and ability to use tools from statistics and linear algebra will be immensely helpful. Luckily, the course starts out with an introductory week, where the basics of machine learning are explained and a bit of probability theory is revised.\\
Underneath is an overview of the notes, I'll be writing. They more or less follow the structure of the course.

1. Introduction to machine learning:\\
    (a) <a href="{{ site.url }}/pages/bsmalea-notes-1a">What is machine learning?</a>\\
    (b) <a href="{{ site.url }}/pages/bsmalea-notes-1b">Model selection and validation, the "no free lunch" theorem, and the curse of dimensionality</a>\\
    (c) Frequentism and Bayesianism\\
    (d) Decision and information theory
2. <a href="{{ site.url }}/pages/bsmalea-notes-2">Linear models for regression</a>
3. Linear models for classification:\\
    (a) Overview of linear classifiers\\
    (b) Discriminant functions\\
    (c) Discriminative models (logistic regression)\\
    (d) Generative models
4. Neural networks (feed-forward, backprop)
5. Kernel methods
6. Graphical models
7. Mixture models and expectation-maximization (EM)
8. Sequential data (HMM)
9. Continuous latent variables (PCA)
10. Combining models (ensemble methods, AdaBoost)
