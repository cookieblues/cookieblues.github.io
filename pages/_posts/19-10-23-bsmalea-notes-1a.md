---
title: "BSMALEA, notes 1a: What is machine learning?"
layout: post
tags: BSMALEA
excerpt_separator: <!--more-->
---
It seems, most people derive their definition of machine learning from a quote from Arthur Lee Samuel in 1959: "Programming computers to learn from experience should eventually eliminate the need for much of this detailed programming effort." The interpretation to take away from this is that "machine learning is the field of study that gives computers the ability to learn without being explicitly programmed."

While Arthur Lee Samuel first coined the term "machine learning" in 1959[^1], the methods applied in machine learning come way before, e.g. the method of least-squares was first published by A. M. Legendre in 1805[^2], and Bayes' theorem, which is the cornerstone of Bayesian statistics, was first underpinned by Thomas Bayes in 1763[^3]. In the next post, we'll see the importance of Bayes' theorem in machine learning, when we dive into frequentism and Bayesianism.

<!---
INSERT TIMELINE
-->

Machine learning draws a lot of its methods from statistics, but there is a distinctive difference between the two areas: **statistics is mainly concerned with estimation**, whereas **machine learning is mainly concerned with prediction**. This distinction makes for great differences, as we will see soon enough.

### Categories of machine learning
<!--
WRITE OUT THAT CLASSIFICATION/REGRESSION ARE SUPERVISED AND CLUSTERING/DENSITY ESTIMATION ARE UNSUPERVISED
-->
There are many different machine learning methods that solve different tasks. This course presupposes two fundamental ones; **supervised** learning and **unsupervised** learning. These are further divided into two smaller categories as shown in the image underneath.

<!---
INSERT ANIMATION
-->
<img src="{{ site.url }}/pages/extra/bsmalea-notes-1a/categories_of_ml.svg">

<!--more-->

#### Supervised learning
<!--
MORE EXPLICIT THAT THERE ARE TARGET VALUES
MAYBE MORE EXPLICIT THAT THERE ARE ONE TARGET FOR EACH INPUT
-->
Supervised learning refers to a subset of machine learning tasks, where we're given a dataset $\mathcal{D} = \left\\{ (\mathbf{x}_1,\mathbf{t}_1), \dots, (\mathbf{x}_N,\mathbf{t}_N) \right\\}$ of $N$ input-output pairs, and our goal is to come up with a function $h$ from the inputs $\mathbf{x}$ to the outputs $\mathbf{t}$. Each input-output pair refers to observations, where we want to predict the output from the input. Each input variable $\mathbf{x}$ is a $D_1$-dimensional vector (or a scalar), representing the observation with numerical values; these are commonly called **features** or **attributes**. Likewise, each output or **target** variable $\mathbf{t}$ is a $D_2$-dimensional vector (but most often just a scalar).

In **classification** the possible values for the target variables form a finite number of discrete categories $t \in \\{ C_1, \dots, C_k \\}$ commonly called **classes**. An example of this could be trying to classify olive oil into geographical regions (our classes) based on various aspects (our features) of the olive oils[^4]. The features could be concentrations of acids in the olive oils, and the classes could be northern and southern France. Another classic example is recognizing handwritten digits[^5]; given an image of $28 \times 28$ pixels, we can represent each image as a $784$-dimensional vector, which will be our input variable, and our targets will be scalars from $0$ to $9$ each representing a distinct digit. A third example could be predicting whether students are in risk of dropping out or not. In this case, we have two classes (in risk and not in risk), which we can predict based on data about the student e.g. grades or attendance. This is actually something I implemented once!

You might've heard of **regression** before. It's the same as classification, except the target variable now is continuous $\mathbf{t} \in \mathbb{R}^{D_2}$ where $D_2 \geq 1$. So, given an input variable, we want to predict some continuous target variable. **EXAMPLES**

#### Unsupervised learning
Another subset of machine learning tasks falls under unsupervised learning, where we're only given a dataset $\mathcal{D} = \left\\{ \mathbf{x}_1, \dots, \mathbf{x}_N \right\\}$ of $N$ input variables. In contrast to supervised learning, we're not told what we want to predict, i.e., we're not given any target variables. The goal of unsupervised learning is then to find patterns in the data.

The image above divides unsupervised learning into two subtasks; the first one being **clustering**, which, as the name suggests, refers to the task of discovering 'clusters' in the data. We can define a cluster to be **a group of observations that are more similar to each other than to observations in other clusters**. Notice that the definition of similarity can vary depending on what data you're dealing with, e.g. disco balls and tennis balls are more similar in shape than compared to hockey pucks, but hockey pucks and tennis balls are more similar in their activity and usage. **EXAMPLES**

<!--
REWRITE, PERHAPS EXAMPLE FIRST
-->
The second subtask is **density estimation**, which is the task of fitting probability density functions to the data. It's important to note that density estimation is often done in conjunction to other tasks like classification, e.g. based on the given classes of our observations, we can use density estimation to find the distributions of each class and thereby (based on the class distributions) classify new observations. **EXAMPLES**

### Example: polynomial regression
Let's go through an example of machine learning. This is also to get familiar with the machine learning vernacular. We're going to implement a model called *polynomial regression*, which is where we try and fit a polynomial to our data. Given a training dataset of $N$ input variables $x \in \mathbb{R}$ (notice we assume our input variables are one-dimensional) with corresponding target variables $t \in \mathbb{R}$, our objective is to fit a polynomial that yields values $\hat{t}$ of target variables for new values $\hat{x}$ of the input variable. We'll do this by estimating the coefficients of the polynomial

$$
h(x, \mathbf{w}) = w_0 + w_1 x + w_2 x^2 + \dots + w_M x^M = \sum_{m=0}^M w_m x^m, \quad \quad (1)
$$

which we refer to as the **parameters** or **weights** of our model. $M$ is the order of our polynomial, and $\mathbf{w} = \left( w_0, w_1, \dots, w_M \right)^\intercal$ denotes all our parameters, i.e. we have $M+1$ parameters for our $M$th order polynomial. Now, the objective is to estimate the 'best' values for our parameters. In the <a href="{{ site.url }}/pages/bsmalea-notes-1b">next post</a> we'll discuss exactly how we define and find the 'best' values, but for now we'll go over it briefly. We define what is called an **objective function** (also called **error** or **loss** function). We construct our objective function such that it outputs a value that tells us how our model is performing. For this task we define the objective function as the sum of the squared differences between the predictions of our polynomial given input variables and the corresponding target variables, i.e.

$$
E(\mathbf{w}) = \sum_{n=1}^N \left( h(x_n, \mathbf{w}) - t_n \right)^2, \quad \quad (2)
$$

and if we substitute $h(x_n, \mathbf{w})$ with the sum on the right-hand side of $(1)$, we get

$$
E(\mathbf{w}) =  \sum_{n=1}^N \left( \sum_{m=0}^M w_m x^m - t_n \right)^2.
$$

Let's take a minute to understand what $(2)$ is saying. The term on the right-hand side between the paranthesis is commonly called the $n$th residual and is denoted $r_n = h(x_n, \mathbf{w}) - t_n$. It's the difference between the output of our polynomial for input variable $x_n$ and the corresponding target variable $t_n$. The difference can be both negative and positive depending on whether the output of our polynomial is lower or higher than the target - we therefore square these differences and add them all up in order to get a value that tells us how our polynomial is performing. Note that since we're squaring all the differences, the value of the objective function $E$ cannot be lower than zero, and if it's zero, then our model is making no mistakes; it is predicting the exact value of the target every time.

<!---
INSERT PICTURE/ANIMATION OF RESIDUALS
-->

So far, so good! Since the objective function tells us how well we're doing, and the lower it is, the better we're doing, we will try and find the minimum of the objective function. That is we want to find the values for our parameters $\mathbf{w}$ that give us the lowest value for $E$. The process of determining the values for our parameters is called the **training** or **learning** process. Recall from the <a href="{{ site.url }}/pages/bslialo-notes-9b">notes about extrema</a> that to find the minimum of a function, we take the derivative, set it equal to zero, and solve for our parameters $\mathbf{w}$. Since we have a lot of parameters, we'll take the partial derivative of $E$ with respect to the $i$th parameter $w_i$, set it equal to zero, and solve for it. This will give us a linear system of $M+1$ equations with $M+1$ unknowns (our parameters $\mathbf{w}$). We'll go over the derivation of the solution to this problem in the next post, but for now we'll just have it given; the solution is

$$
\hat{\mathbf{w}} = \left( \mathbf{X}^\intercal \mathbf{X} \right)^{-1} \mathbf{X}^\intercal \textbf{\textsf{t}}, \quad \quad (3)
$$

where $\textbf{\textsf{t}}$ denotes all our target variables as a column vector $\textbf{\textsf{t}} = \left( t_1, t_2, \dots, t_N \right)^\intercal$, and $\mathbf{X}$ is called the **design matrix** and is defined as

$$
\mathbf{X} = \begin{pmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^M \\
1 & x_2 & x_2^2 & \cdots & x_2^M \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_N & x_N^2 & \cdots & x_N^M \\
\end{pmatrix}. \quad \quad (4)
$$

To sum up: we're given $N$ pairs of input and target variables $\left\\{ (x_1, t_1), \dots, (x_N, t_N) \right\\}$, and we want to fit a polynomial to the data of the form $(1)$ such that the value of $h(x_i, \mathbf{w})$ is as close to $t_i$ as possible. We do this by finding values for the parameters that minimizes the objective function defined in $(2)$, and the solution is given by $(3)$.

#### Python implementation of polynomial regression
Let's try and implement our model - let's start with the dataset shown underneath, where `x` is our input variables and `t` is our target variables.

{% highlight python %}
import numpy as np

x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
t = np.array([1.15, 0.84, 0.39, 0.14, 0, 0.56, 1.16, 1.05, 1.45, 2.39, 1.86])
{% endhighlight %}

To begin with we can define the order of our polynomial, find the number of data points, and then set up our design matrix.

{% highlight python %}
M = 3
N = len(x)
X = np.zeros((N, M+1))
{% endhighlight %}

If we look at the definition of the design matrix in $(4)$, we can fill out the columns of our design matrix with a for loop.

{% highlight python %}
for m in range(M+1):
    X[:, m] = x**m
{% endhighlight %}

Now we can find the parameters with the solution in $(3)$ (note that `@` performs matrix multiplication).

{% highlight python %}
w = np.linalg.inv(X.T @ X) @ X.T @ t
{% endhighlight %}

Using NumPy's [`poly1d` function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html){:target="_blank"} we can generate outputs for our polynomial (note that our weights have to be flipped to fit the function).
<!--
MAYBE SHOW SMALL TEST OF poly1d FUNCTION
-->
{% highlight python %}
h = np.poly1d(np.flip(w, 0))
x_ = np.linspace(0, 10, 100)
t_ = h(x_)
{% endhighlight %}

Now we can plot our estimated polynomial with our data points. I've also plotted the true function that the points were generated from.

<img src="{{ site.url }}/pages/extra/bsmalea-notes-1a/poly_reg.svg">





[^1]: R. Kohavi and F. Provost, "Glossary of terms," Machine Learning, vol. 30, no. 2–3, pp. 271–274, 1998.
[^2]: A. M. Legendre, "Nouvelles méthodes pour la détermination des orbites des comètes," 1805.
[^3]: T. Bayes and R. Price, "An essay towards solving a problem in the doctrine of chances," in a letter to J. Canton, 1763.
[^4]: J. Gromadzka and W. Wardencki, "Trends in Edible Vegetable Oils Analysis. Part B. Application of Different Analytical Techniques," 2011.
[^5]: Y. LeCun, L. Bottou, Y. Bengio, P. Haffner, "Gradient-based learning applied to document recognition," 1998.
