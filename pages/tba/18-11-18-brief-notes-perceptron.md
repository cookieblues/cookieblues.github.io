---
title: "Brief notes about the perceptron algorithm"
layout: post
tags: General
excerpt_separator: <!--more-->
---
Because a few people requested an introduction to the perceptron algorithm, I'll write up some refined notes, from when I was introduced to the algorithm. For linear algebra and elementary calculus not to be prerequisites, we will consider the most basic interpretation of the perceptron with limited math rigour. \\
[Artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network){:target="_blank"} are attempts at imitating the brain in the sense of a bunch of connected neurons. The artificial neuron in a neural network is called a perceptron, and the perceptron in machine learning lingo is a binary classifier. Binary classification is the task of grouping elements into two groups. An example of a classification task could be to determine the region of origin of wine given the percentage of alcohol and acid, or determining whether a patient has a disease or not given certain symptoms.
<!--more-->

### Classification
Let's say you have a $D$-dimensional input vector $\left( x_1, \dots, x_D \right)^\intercal$, and you want the perceptron to classify this into one of two classes: $\mathcal{C}_1$ and $\mathcal{C}_2$. To classify this input vector, the first step of the perceptron is to scale the elements of the vector by some learned weights $\left( w_1,\dots,w_D \right)^\intercal$. We'll come back to how these weights are learned later on, but for now we'll assume they're given. So, the input vector is scaled by the weight vector, which is the same thing as taking the dot product

$$
\begin{pmatrix}
w_1 \\
\vdots \\
w_D
\end{pmatrix}
\cdot
\begin{pmatrix}
x_1 \\
\vdots \\
x_D
\end{pmatrix}
=
w_1 x_1 + \cdots + w_D x_D = \sum_{d=1}^D w_d x_d. \quad \quad (1)
$$

The second step is to introduce an offset term or the *bias* $b$ that we add to the sum in $(1)$, giving us

$$
b+\sum_{d=1}^D w_d x_d. \quad \quad (2)
$$

Typically, we define variables $w_0 = b$ and $x_0 = 1$, so that we can talk about the vectors

$$
\mathbf{w} = 
\begin{pmatrix}
b \\
w_1 \\
\vdots \\
w_D
\end{pmatrix}
\quad \text{and} \quad
\mathbf{x} =
\begin{pmatrix}
1 \\
x_1 \\
\vdots \\
x_D
\end{pmatrix},
$$

as well as rewrite the sum in $(2)$ as

$$
\mathbf{w} \cdot \mathbf{x} = \sum_{d=0}^D w_d x_d. \quad \quad (3)
$$

The third and final step is to turn the sum $(3)$ into an output that will represent one of the two classes in the problem. This is done by feeding $(3)$ into a function called the *activation* function. Usually, to mimic a neuron, the activation function either outputs a $1$ or $-1$ depending on the value of $(3)$

$$
f(\mathbf{x}) = 
\begin{cases}
1 & \text{if} \quad \mathbf{w} \cdot \mathbf{x} \geq 0, \\
-1 & \text{otherwise},
\end{cases}
\quad \quad (4)
$$

where $1$ and $-1$ correspond to the two classes $\mathcal{C}_1$ and $\mathcal{C}_2$ respectively.

### Learning
Now that we understand, how the perceptron works, let's look at how the perceptron *learns* to work, i.e., how the weights $\mathbf{w}$ are derived. Firstly, to train the perceptron we need a bunch of input that we know the output for - let $\mathbf{x}_n$ be the $n$th input vector, and $t_n$ its corresponding target value (either $1$ or $-1$ corresponding to class $\mathcal{C}_1$ and $\mathcal{C}_2$ respectively). Secondly, we want to define an error function to get us closer and closer to the best value of $\mathbf{w}$. From $(4)$ we know, $\mathbf{w}$ should satisfy $\mathbf{w} \cdot \mathbf{x}_n > 0$ for input vectors $\mathbf{x}_n$ in class $\mathcal{C}_1$ with target value $t_n = 1$, and $\mathbf{w} \cdot \mathbf{x}_n < 0$ for input vectors $\mathbf{x}_n$ in class $\mathcal{C}_2$ with target value $t_n = -1$. Combining these gives us that $\mathbf{w}$ should satisfy $\mathbf{w} \cdot \mathbf{x}_n t_n > 0$ for all input vectors $\mathbf{x}_n$. The error function we define is

$$
E(\mathbf{w}) = - \sum_{n \in \mathcal{M}} \mathbf{w} \cdot \mathbf{x}_n t_n, \quad \quad (5)
$$

where $\mathcal{M}$ is the set of all misclassified input vectors. Finally, we can use the [stochastic gradient descent algorithm](https://en.wikipedia.org/wiki/Stochastic_gradient_descent){:target="_blank"} to minimize $E$. The change in $\mathbf{w}$ is given by

$$ \begin{aligned}
\mathbf{w}_{k+1}
&= \mathbf{w}_k + \Delta \mathbf{w} \\
&= \mathbf{w}_k - \eta \nabla E(\mathbf{w}) \\
&= \mathbf{w}_k + \eta t_i \mathbf{x}_i,
\end{aligned} $$

where $\eta$ is the learning rate that is essentially irrelevant, and we can just set it equal to $1$.


### Interpretations
A geometric interpretation is to think of the perceptron as a linear discriminator (or separator), i.e., the perceptron is a hyperplane in the space of the inputs that separate the inputs in two groups.\\
I've tried my best to illustrate this below in two and three dimensions.



A biological interpretation is obviously the neuron. More specifically: given some input, the perceptron will either activate and send an output (think of this as outputting $1$), or it won't do anything (output is $-1$). The activation happens if the sum is larger than zero.


