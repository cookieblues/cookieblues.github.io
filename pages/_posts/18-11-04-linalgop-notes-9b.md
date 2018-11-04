---
title: "LinAlgOp, notes 9b: The chain rule, derivatives of logarithmic functions, extrema, and optimisation"
layout: post
tags: LinAlgOp
---
Differentiation is commonly taught through rote learning, which I'm not a fan of. Therefore I'll allow myself to skip the basic rules of differentiation, and what the derivative of every little function is. Instead, I want to focus on the useful and interesting, namely, the chain rule and logarithmic derivatives, both of which are important in machine learning. At the end, we'll talk about optimisation, where we'll try and combine, what we've learned.

### The chain rule
There are many rules of differentiation, e.g. let $u,v$ be functions, then the sum rule tells us how to take the derivative of a sum of functions

$$
\frac{d}{dx} (u + v) = \frac{du}{dx} + \frac{dv}{dx},
$$

the product rule tells us how to take the derivative of a product of functions

$$
\frac{d}{dx} (u \cdot v) = \frac{du}{dx} \cdot v + u \cdot \frac{dv}{dx},
$$

and the chain rule tells us how to take the derivative of a *composition* of functions. A function composition can be thought of as putting one function into another. Say we have two functions $f(x) = \sin (x)$ and $g(x) = x^2$. We can make two compositions from these two functions: $(f \circ g) (x) = f(g(x)) = \sin \left( x^2 \right)$ and $(g \circ f) (x) = g(f(x)) = \sin^2(x)$. The $\circ$ symbol represents a function composition. \\
Let's choose $(f \circ g) (x) = \sin \left( x^2 \right)$ and try to reason our way to its derivative. From <a href="{{ site.url }}/pages/linalgop-notes-9a">notes 9a</a> we know, the derivative of a function is the oxymoron *instantaneous* rate of *change*. If we call this change $dx$, then we can write the derivative as

$$
\frac{du}{dx} = \lim_{ dx \to 0} \frac{u(x+ dx)-u(x)}{ dx}. \quad \quad (1)
$$

We can also phrase this as: a slight change in the function's output divided by a slight change in its input. In our example of function composition, $(f \circ g) (x) = \sin \left( x^2 \right)$, we have to think about this in two steps:

Firstly, we have to consider, what happens to $g(x)$, when a slight change in $x$ occurs. Since $g(x) = x^2$, a slight change $dx$ will equal $g(x + dx) - g(x)$ or rather

$$ \begin{aligned}
g(x + dx) - g(x)
&= (x+dx)^2 - x^2 \\
&= x^2 + 2xdx + (dx)^2 - x^2 \\
&= 2xdx + ( dx )^2.
\end{aligned} $$

If we divide both sides by the slight change $dx$ and compare it to equation $(1)$, we see, we've calculated the derivative of $g$

$$
\frac{dg}{dx} = \frac{g(x + dx) - g(x)}{dx} = 2x + dx, \quad \quad (2)
$$

which is $2x$, plus a slight change that will be negligible, when $dx \to 0$.


Secondly, we have to consider, what happens to $f(g(x))$, when a slight change in $g(x)$ occurs. Using the same reasoning as before, and knowing that the derivative of $\sin(x)$ is $\cos(x)$, we can say

$$
\frac{df}{dg} = \cos(g) \quad \quad (3)
$$

as $dg \to 0$, i.e. the derivative of $\sin(g)$ with respect to $g$ is $\cos(g)$. Multiplying $(2)$ and $(3)$ yields

$$ \begin{aligned}
\frac{df}{dg} \cdot \frac{dg}{dx} &= \cos(g) 2x \\
\frac{df}{dx} &= \cos( x^2 ) 2x,
\end{aligned} $$

which is the derivative of $(f \circ g)(x) = \sin \left( x^2 \right)$ with respect to $x$. This result is the derivative of $f$ with respect to $g$ times the derivative of $g$ with respect to $x$, or rather the derivative of the "outer" function $(f)$ times the derivative of the "inner" function $(g)$. That's the chain rule[^1]. \\
More formally, if $g$ is a function differentiable at $a$, and $f$ is a function differentiable at $g(a)$, then the composite function $h = f \circ g$ is differentiable at $a$, and the derivative is

$$
h'(a) = (f \circ g)'(a) = f'(g(a)) g'(a).
$$

#### Example:
Let's try and find the derivative of $f(x) = \sqrt[3]{7-3x}$. We start by rewriting the root as a power $f(x) = (7-3x)^{1/3}$. Then we let the inner function equal $g(x)=7-3x$, and the outer function $h(g) = g^{1/3}$. The derivative of $g$ with respect to $x$ is $-3$, and the derivative of $h(g)$ with respect to $g$ is $\frac{1}{3} g^{-2/3}$. The product of these gives us the derivative

$$ \begin{aligned}
\frac{df}{dx}
&= -3 \cdot \frac{1}{3} (7-3x)^{-\frac{2}{3}} \\
&= -\frac{1}{(7-3x)^{\frac{2}{3}}}.
\end{aligned} $$

### Derivatives of logarithmic functions
It's tempting to dive into the relationship between derivatives, exponential, and logarithmic functions[^2]. Instead we will briefly talk about logarithms, some of their properties, and then look at the usefulness of logarithms, when we get to optimisation, which is also an appetizer for [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation){:target="_blank"} in machine learning[^3][^4]. However, before we get into the derivative of logarithms, let's refresh logarithms, shall we? \\
Firstly, a logarithm is the inverse function to an exponential function, i.e. $x$ is the base-$b$ logarithm of $y$ if and only if $b^x = y$. This is written

$$
\log_b y = x \iff b^x = y.
$$

Logarithms are used to solve questions like: what exponent should 3 be raised to equal 27?

$$ \begin{aligned}
3^x &= 81 \\
x &= \log_3 81 \\
x &= 4.
\end{aligned} $$

The *common* logarithm is the logarithm to base $10$ denoted $\log(x)$. The *natural* logarithm, which is the one we'll be using the most, has Euler's number[^5] $e$ as its base and is denoted $\ln(x)$. Logarithms are useful for their special properties - the most common being

$$ \begin{aligned}
\log_b x + \log_b y &= \log_b (xy) \\
\log_b x - \log_b y &= \log_b \left( \frac{x}{y} \right) \\
\log_b x^y &= y \log x,
\end{aligned} $$

and many more, but these are the important ones for our purposes. The derivative of a logarithm is

$$
\frac{d}{dx} (\log_b x) = \frac{1}{x \ln b},
$$

which makes the derivative of the natural logarithm

$$
\frac{d}{dx} (\ln x) = \frac{1}{x}.
$$

#### Example:
Let's try and find the derivative with respect to $z$ of $\ln \left( 17 + z^{3/2} \right)$. We notice that this function is composite, and the outer function is the natural logarithm with derivative $\frac{1}{x}$. Therefore, using the chain rule and the derivative of the natural logarithm, we have

$$ \begin{aligned}
\frac{d}{dz} \ln \left( 17 + z^\frac{3}{2} \right)
&= \frac{1}{17 + z^\frac{3}{2}} \frac{d}{dz} \left( 17 + z^\frac{3}{2} \right) \\
&= \frac{1}{17 + z^\frac{3}{2}} \frac{3}{2}z^\frac{1}{2} \\
&= \frac{3 \sqrt{z}}{34 + 2z^\frac{3}{2}}.
\end{aligned} $$


### Extrema
Extrema is the collective term for maxima and minima, which are the largest and smallest values of a function. Usually we distinguish between a *local* or *relative* extremum and a *global* or *absolute* extremum, where local and relative refers to a specific interval, and global and absolute refers to the domain of the function.\\
A point $x$ is an absolute maximum or minimum of a function $f$ in the interval $\left[ a,b \right]$, if

$$
f(x) \geq f(x') \text{ or } f(x) \leq f(x') \text{ for all } x' \in \left[ a,b \right],
$$

and $x$ is a relative maximum or minimum, if it's the absolute maximum or minimum value in a tiny interval around $x$, i.e. the interval $(x-c,x+c)$ for some small value $c$. While there are a couple of exceptions, we can in general find the extrema of a function by calculating its derivative and setting it equal to zero. This is because, as one might intuitively reason, the curve of the function "changes direction" at an extremum as illustrated below with the slope.

<video width="500" height="310" loop muted autoplay>
    <source src="../extra/linalgop-notes-9b/fig_01.mp4" type="video/mp4">
</video>

We can also think of the extrema of a function is where the derivative changes sign before and after. This is also known as the *first derivative test*.

#### Example:
Let's try and find the extrema of $f(x) = x^4-6x^3+12x^2-8x$. The derivative can be factorized as

$$ \begin{aligned}
\frac{df}{dx}
&= \frac{d}{dx} \left( x^4-6x^3+12x^2-8x \right) \\
&= 4x^3-18x^2+24x-8 \\
&= 2(x-2)^2 (2x-1).
\end{aligned} $$

Setting this equal to zero gives us two values for $x$, $2$ and $\frac{1}{2}$. To check if these points are extrema, we use the first derivative test and check the value of the derivative before and after each point. We see

$$ \begin{aligned}
f'(x) &< 0 \quad \text{for} \quad  x < \frac{1}{2}, \\
f'(x) &> 0 \quad \text{for} \quad \frac{1}{2} < x < 2, \\
f'(x) &> 0 \quad \text{for} \quad 2 < x.
\end{aligned} $$

This implies that $f(x)$ has a minimum at $x=\frac{1}{2}$, but neither a maximum or a minimum at $x=2$. By plotting $f$ we can see, what goes on at $x=2$:

<video width="500" height="310" loop muted autoplay>
    <source src="../extra/linalgop-notes-9b/fig_03.mp4" type="video/mp4">
</video>

We can interpret this as, if we're coming from the left, then $x=2$ is a maximum, but coming from the right it's a minimum. Therefore it can neither be a maximum or minimum.

### Optimisation example (putting it all together)
Now, let's take everything we've learned, put it together, and use it! Optimisation problems often aim to find the extrema of a specifically constructed function. In most literature this function is called the *objective* function, and the aim is to find its maximum or minimum. The objective function can be interpreted as the error or accuracy of a model, and our goal is to minimize or maximize this measure, hence optimizing the model.

Suppose we have a coin, and we want to find the most likely probability (parameter) for this coin to hit heads and tails - i.e., we want to create a model that calculates the most likely number of heads and tails in a number of coin tosses. If we let $\pi$ represent the unknown probability of heads, $1-\pi$ the unknown probabilty of tails, and toss the coin $100$ times, then our result could look something like this

$$
HHTHTTHHHTHT \dots,
$$

and let's assume we got 46 heads and 54 tails. We write up, the probability of the specific sequence we got (our data), given the unknown parameter $\pi$ as

$$ \begin{aligned}
P( \text{data} | \text{parameter} )
&= P(HHTHTTHHHTHT \dots | \pi) \\
&= \pi \pi (1-\pi) \pi (1-\pi) (1-\pi) \pi \pi \pi (1-\pi) \pi (1-\pi) \dots \\
&= \pi^{46} (1-\pi)^{54}.
\end{aligned} $$

The left-hand side is read: "the probability of the data given the parameter". Since the probability of heads and tails is $\pi$ and $1-\pi$ respectively, and they're independent events, we can take the product of the probabilities of each coin toss in our sequence to get the probability of the entire sequence. This is commonly known as the product rule of probability[^6][^7]. We want to figure out, what the most likely probability of heads is $(\pi)$ with our data of 46 heads and 54 tails. Just like our data, the parameter $\pi$ has a fixed value too, but it's unknown. We therefore treat it as a variable between 0 and 1 that we are free to choose. We now have the so-called [*likelihood function*](https://en.wikipedia.org/wiki/Likelihood_function){:target="_blank"}.

$$
\mathcal{L} ( \text{parameter} | \text{data} ) = \pi^{46} (1-\pi)^{54},
$$

i.e. a function of the parameter given the data. Below is a plot of the likelihood function, where the x-axis is the value of our parameter $\pi$, which varies from $0$ to $1$, and the y-axis is the probability of that specific value of $\pi$ given our data or *likelihood*. Don't worry about the low values on the y-axis - we're only interested in the relation between the values (the largest of them).

<video width="500" height="310" loop muted autoplay>
    <source src="../extra/linalgop-notes-9b/fig_02.mp4" type="video/mp4">
</video>

The maximum value of the likelihood function is at $\pi=0.46$, and we're done. We now have a parameter $\pi = 0.46$ that gives us the most likely ratio of heads to coin tosses, given the data we produced. We can think of this as optimizing our coin toss model, but let's examine closer, what we did. We tossed a coin $100$ times, asked ourselves what the most likely probability of heads is, and called this value $\pi$. Then we wrote up the likelihood function of $\pi$, and found the value of $\pi$ corresponding to the maximum of the likelihood function. Let's now try and generalize this method, in case we produced different data.\\
Let's say we toss the coin $n$ times, and we get $k$ heads. Our likelihood function would be

$$
\mathcal{L} ( \pi | \text{data} ) = \pi^k (1-\pi)^{n-k}.
$$

Then we want to find the maximum of this function. While we could try and take the derivative straight away, there is an important theorem, we use instead: the natural logarithm is a strictly increasing function, so the natural logarithm of a function achieves its maxima at the same values as the function itself. Therefore, instead of finding the maximum of $\mathcal{L}$, we can find the maximum of $\ln ( \mathcal{L} )$, which often times is easier. By using the rules of logarithms, we find

$$ \begin{aligned}
\ln ( \mathcal{L}( \pi | \text{data} ) )
&= \ln \left( \pi^k (1-\pi)^{n-k} \right) \\
&= \ln (\pi^k) + \ln \left( (1-\pi)^{n-k} \right) \\
&= k \ln (\pi) + (n-k) \ln (1-\pi).
\end{aligned} $$

Now, we want to find the maximum of this function, which we do by finding the derivative and setting it equal to zero. We can use the chain rule and the derivative of logarithms to find the derivative of the likelihood function:

$$ \begin{aligned}
\frac{d}{d\pi} \ln ( \mathcal{L} )
&= \frac{d}{d\pi} \left( k \ln (\pi) + (n-k) \ln (1-\pi) \right) \\
&= \frac{k}{\pi} + (-1) \frac{n-k}{1-\pi} \\
&= \frac{k}{\pi} - \frac{n-k}{1-\pi}
\end{aligned} $$

Then we set the derivative equal to zero and solve for $\pi$ to find the maximum:

$$ \begin{aligned}
\frac{d}{d\pi} \ln ( \mathcal{L} )
&= 0 \\
\frac{k}{\pi} - \frac{n-k}{1-\pi}
&= 0 \\
k(1-\pi) - \pi(n-k)
&= 0 \\
k - k \pi - \pi n + \pi k
&= 0 \\
k - \pi n
&= 0 \\
\pi
&= \frac{k}{n},
\end{aligned} $$

and we're done! The most likely probability of heads is therefore the number of heads $k$, we get in $n$ coin tosses ($\frac{46}{100} = 0.46$ in our example). While the example at hand is simple enough to find the result without using our method, we can use this same method in many other scenarios, where the result isn't as easily found. Also, notice how we utilized our knowledge of the chain rule, logarithms, and extrema.

[^1]: Yet, this is not a rigorous proof of the chain rule.
[^2]: I might write a post about this in the future.
[^3]: *Pattern Recognition and Machine Learning*, Christopher M. Bishop, pg. 23.
[^4]: https://en.wikipedia.org/wiki/Likelihood_function#Log-likelihood
[^5]: https://en.wikipedia.org/wiki/E_(mathematical_constant)
[^6]: *Pattern Recognition and Machine Learning*, Christopher M. Bishop, pg. 14.
[^7]: https://en.wikipedia.org/wiki/Probability#Summary_of_probabilities