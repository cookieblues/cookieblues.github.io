---
date: 2021-03-08
title: "Machine learning, notes 1a: What is machine learning?"
categories:
  - Guides
featured_image: https://raw.githubusercontent.com/cookieblues/cookieblues.github.io/f1b1ba6d4669131256419c6e57a2c9527150135d/extra/bsmalea-notes-2/test.svg
---
It seems, most people derive their definition of machine learning from a quote from Arthur Lee Samuel in 1959: "Programming computers to learn from experience should eventually eliminate the need for much of this detailed programming effort." The interpretation to take away from this is that "machine learning is the field of study that gives computers the ability to learn without being explicitly programmed."

While Arthur Lee Samuel first coined the term "machine learning" in 1959<span class="sidenote-number"></span><span class="sidenote">R. Kohavi and F. Provost, "Glossary of terms," Machine Learning, vol. 30, no. 2–3, pp. 271–274, 1998.</span>,  and machine learning ['took off' after the 1970s](https://en.wikipedia.org/wiki/AI_winter), the underlying theory applied in machine learning have existed long before. For example, the method of least-squares was first published by Adrien-Marie Legendre in 1805<span class="sidenote-number"></span><span class="sidenote">A. M. Legendre, "Nouvelles méthodes pour la détermination des orbites des comètes," 1805.</span>, and Bayes' theorem, which is the cornerstone of Bayesian statistics that has taken off in the 21st century, was first underpinned by Thomas Bayes in 1763<span class="sidenote-number"></span><span class="sidenote">T. Bayes and R. Price, "An essay towards solving a problem in the doctrine of chances," in a letter to J. Canton, 1763.</span>.

<!---
INSERT TIMELINE
-->

Machine learning draws a lot of its methods from statistics, but there is a distinctive difference between the two areas: **statistics is mainly concerned with estimation**, whereas **machine learning is mainly concerned with prediction**. This distinction makes for great differences, as we will see soon enough.

### Categories of machine learning
There are many different machine learning methods that solve different tasks and putting them all in rigid categories can be quite a task on its own. My posts will cover 2 fundamental ones; **supervised** learning and **unsupervised** learning, which can further be divided into smaller categories ash shown in the image underneath.

<!---
INSERT ANIMATION
-->
<img src="{{ site.url }}/extra/bsmalea-notes-1a/categories_of_ml_2.svg">

It's important to note that these categories are not strict, e.g. dimensionality reduction isn't always unsupervised, and you can use density estimation for clustering and classification.

#### Supervised learning
Supervised learning refers to a subset of machine learning tasks, where we're given a dataset $\mathcal{D} = \left\\{ (\mathbf{x}_1,\mathbf{t}_1), \dots, (\mathbf{x}_N,\mathbf{t}_N) \right\\}$ of $N$ input-output pairs, and our goal is to come up with a function $h$ from the inputs $\mathbf{x}$ to the outputs $\mathbf{t}$. In more layman's terms: we are given a dataset with predetermined labels that we want to predict - hence the learning is *supervised*, i.e. we are handed some data that tells us, what we want to predict. Each input-output pair refers to observations, where we want to predict the output from the input. Each input variable $\mathbf{x}$ is a $D_1$-dimensional vector (or a scalar), representing the observation with numerical values. The different dimensions of the input variable are commonly called **features** or **attributes**. Likewise, each output or **target** variable $\mathbf{t}$ is a $D_2$-dimensional vector (but most often just a scalar).

In **classification** the possible values for the target variables form a finite number of discrete categories $t \in \\{ C_1, \dots, C_k \\}$ commonly called **classes**. An example of this could be trying to classify olive oil into geographical regions (our classes) based on various aspects (our features) of the olive oils<span class="sidenote-number"></span><span class="sidenote">J. Gromadzka and W. Wardencki, "Trends in Edible Vegetable Oils Analysis. Part B. Application of Different Analytical Techniques," 2011.</span>. The features could be concentrations of acids in the olive oils, and the classes could be northern and southern France. Another classic example is recognizing handwritten digits<span class="sidenote-number"></span>. Given an image of $28 \times 28$ pixels,<span class="sidenote">Y. LeCun et al., "Gradient-based learning applied to document recognition," 1998.</span> we can represent each image as a $784$-dimensional vector, which will be our input variable, and our target variables will be scalars from $0$ to $9$ each representing a distinct digit.

You might've heard of **regression** before. Like classification, we are given a target variable, but in regression it is continuous instead of discrete, i.e. $t \in \mathbb{R}$. An example of regression that I'm fairly interested in is forecasting election results from polling. In this case, your features would obviously be the polls, but it could also include other data like days until the election or perhaps the parties' media attention. The target variables are naturally the share of the votes for each party. Another example of regression could be predicting how much a house will be sold for. In this case, the features could be any measurements about the house, the location, and what other similar houses have been sold for recently - the target variable is the selling price of the house.

#### Unsupervised learning
Another subset of machine learning tasks fall under unsupervised learning, where we're only given a dataset $\mathcal{D} = \left\\{ \mathbf{x}_1, \dots, \mathbf{x}_N \right\\}$ of $N$ input variables. In contrast to supervised learning, we're not told what we want to predict, i.e., we're not given any target variables. The goal of unsupervised learning is then to find patterns in the data.

The image of categories above divides unsupervised learning into 3 subtasks, the first one being **clustering**, which, as the name suggests, refers to the task of discovering 'clusters' in the data. We can define a cluster to be **a group of observations that are more similar to each other than to observations in other clusters**. Let's say we had to come up with clusters for a basketball, a carrot, and an apple. Firstly, we could create clusters based on shapes, in which case the basketball and the apple are both round, but the carrot isn't. Secondly, we could also cluster by use, in which case the carrot and apple are foods, but the basketball isn't. Finally, we might cluster by colour, in which case the basketball and the carrot are both orange, but the apple isn't. All three are examples are valid clusters, but they're clustering different things.

Then we have **density estimation**, which is the task of fitting probability density functions to the data. It's important to note that density estimation is often done in conjunction to other tasks like classification, e.g. based on the given classes of our observations, we can use density estimation to find the distributions of each class and thereby (based on the class distributions) classify new observations. An example of density estimation could be finding extreme outliers in data, i.e., finding data that are highly unlikely to be generated from the density function you fit to the data.

Finally, **dimensionality reduction**, as the name suggests, reduces the number of features of the data that we're dealing with. Just like density estimation, this is often done in conjunction with other tasks. Let's say, we were going to do a classification task, and our input variables have 50 features - if we could do the same task equally well after reducing the number of features to 5, we could save a lot of time on computation. Having a high number of dimensions in our input variables can also cause unwanted behaviour in our model, known as the curse of dimensionality, but that's a tale for another time.

### Example: polynomial regression
Let's go through an example of machine learning. This is also to get familiar with the machine learning terminology. We're going to implement a model called *polynomial regression*, where we try and fit a polynomial to our data. Given a training dataset of $N$ input variables $x \in \mathbb{R}$ (notice the input variables are one-dimensional) with corresponding target variables $t \in \mathbb{R}$, our objective is to fit a polynomial that yields values $\hat{t}$ of target variables for new values $\hat{x}$ of the input variable. We'll do this by estimating the coefficients of the polynomial

$$
h(x, \mathbf{w}) = w_0 + w_1 x + w_2 x^2 + \dots + w_M x^M = \sum_{m=0}^M w_m x^m, \quad \quad (1)
$$

which we refer to as the **parameters** or **weights** of our model. $M$ is the order of our polynomial, and $\mathbf{w} = \left( w_0, w_1, \dots, w_M \right)^\intercal$ denotes all our parameters, i.e. we have $M+1$ parameters for our $M$th order polynomial.

<span class="marginnote">In the next post we'll discuss exactly what we mean by 'best' values.</span>
Now, the objective is to estimate the 'best' values for our parameters. To do this, we define what is called an **objective function** (also sometimes called **error** or **loss** function). We construct our objective function such that it outputs a value that tells us how our model is performing. For this task, we define the objective function as the sum of the squared differences between the predictions of our polynomial and the corresponding target variables, i.e.

$$
E(\mathbf{w}) = \sum_{n=1}^N \left( t_n - h(x_n, \mathbf{w}) \right)^2, \quad \quad (2)
$$

and if we substitute $h(x_n, \mathbf{w})$ with the right-hand side of $(1)$, we get

$$
E(\mathbf{w}) =  \sum_{n=1}^N \left( t_n - \sum_{m=0}^M w_m x^m \right)^2.
$$

Let's take a minute to understand what $(2)$ is saying. The term in the parantheses on the right-hand side is commonly called the $n$th residual and is denoted $r_n = t_n - h(x_n, \mathbf{w})$. It's the difference between the output of our polynomial for input variable $x_n$ and the corresponding target variable $t_n$. The difference can be both negative and positive depending on whether the output of our polynomial is lower or higher than the target.<span class="marginnote">Note that since we're squaring all the differences, the value of the objective function $E$ cannot be lower than 0 - and if it's exactly 0, then our model is making no mistakes, i.e., it is predicting the exact value of the target every time.</span> We therefore square these differences and add them all up in order to get a value that tells us how our polynomial is performing.

This objective function is called the [residual sum of squares or sum of the squared residuals](https://en.wikipedia.org/wiki/Residual_sum_of_squares) and is often used as a way to measure the performance of regression models in machine learnig. The image below shows the differences between the polynomium that we're estimating and the data we're given. These differences are the errors (or residuals) that the objective function is taking the square of and summing.

<img src="{{ site.url }}/extra/bsmalea-notes-1a/residuals.svg">

So far, so good! Since the objective function tells us how well we're doing, and the lower it is, the better we're doing, we will try and find the minimum of the objective function. That is, we want to find the values for our parameters $\mathbf{w}$ that give us the lowest value for $E$. The process of determining the values for our parameters is called the **training** or **learning** process.

<!-- Recall from the <a href="{{ site.url }}/bslialo-notes-9b">notes about extrema</a> that-->
To find the minimum of a function, we take the derivative, set it equal to 0, and solve for our parameters $\mathbf{w}$. Since we have a lot of parameters, we'll take the partial derivative of $E$ with respect to the $i$th parameter $w_i$, set it equal to 0, and solve for it. This will give us a linear system of $M+1$ equations with $M+1$ unknowns (our parameters $\mathbf{w}$). We'll go over the derivation of the solution to this problem in the next post, but for now we'll just have it given. The solution to the system of equations is

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

To sum up: we're given $N$ pairs of input and target variables $\left\\{ (x_1, t_1), \dots, (x_N, t_N) \right\\}$, and we want to fit a polynomial to the data of the form $(1)$ such that the value of our polynomium $h(x_i, \mathbf{w})$ is as close to $t_i$ as possible. We do this by finding values for the parameters $\mathbf{w}$ that minimize the objective function defined in $(2)$, and the solution to this is given in $(3)$.

#### Python implementation of polynomial regression
Let's try and implement our model! We'll start with the dataset shown underneath, where `x` is our input variables and `t` is our target variables.

{% highlight python %}
import numpy as np

x = np.array([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
t = np.array([-4.9, -3.5, -2.8, 0.8, 0.3, -1.6, -1.3, 0.5, 2.1, 2.9, 5.6])
{% endhighlight %}

To begin with we can define the order of our polynomial, find the number of data points, and then set up our design matrix.

{% highlight python %}
M = 4
N = len(x)
X = np.zeros((N, M+1))
{% endhighlight %}

If we look at the definition of the design matrix in $(4)$, we can fill out the columns of our design matrix with the following for-loop.

{% highlight python %}
for m in range(M+1):
    X[:, m] = x**m
{% endhighlight %}

Now we can find the parameters with the solution in $(3)$.

<span class="marginnote">The `@` performs matrix multiplication.</span>
{% highlight python %}
w = np.linalg.inv(X.T @ X) @ X.T @ t
{% endhighlight %}


Using NumPy's [`poly1d` function](https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html) we can generate outputs for our polynomial.
<!--
MAYBE SHOW SMALL TEST OF poly1d FUNCTION
-->

<span class="marginnote">We flip the weights to accommodate the input of the `poly1d` function.</span>
{% highlight python %}
h = np.poly1d(np.flip(w, 0))
x_ = np.linspace(0, 10, 100)
t_ = h(x_)
{% endhighlight %}

Now we can plot our estimated polynomial with our data points. I've also plotted the true function that the points were generated from.

<img src="{{ site.url }}/extra/bsmalea-notes-1a/poly_reg.svg">


### Summary
* Machine learning studies **how to make computers learn on their own** with the goal of **predicting the future**.
* **Supervised learning** refers to machine learning tasks, where we are given **labeled data**, and we want to predict those labels.
* **Unsupervised learning**, as it suggests, refers to tasks, where we are *not* provided with labels for our data.
* **Features** refer to the **attributes** (usually columns) of our data e.g. height, weight, shoe size, etc., if our observations are humans.
* **Classification and regression are supervised** tasks, **clustering, density estimation, and dimensionality reduction are unsupervised** tasks.
* **Parameters** refer to the values, **we want to estimate** in a machine learning model.
* The **process of estimating the values of the parameters** is called the **training or learning** process.
* An **objective function** is a **measure of the performance** of our model.
