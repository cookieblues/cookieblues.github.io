---
title: "BSLIALO, notes 9c: Integration and the fundamental theorem of calculus"
layout: post
tags: BSLIALO
excerpt_separator: <!--more-->
---
In <a href="{{ site.url }}/pages/bslialo-notes-9a">notes 9a</a> we introduced the derivative by looking at a $100$ meter sprint race. We looked at the so-called distance function $s(t)$, which told us how far we'd run in the race at time $t$, and asked if we could figure out a function for velocity $v(t)$. We found that the derivative of the distance function $s(t)$ was the velocity function $v(t)$, which we wrote up

$$
\frac{d}{dt}s(t) = s'(t) = v(t).
$$

This time we will look at the velocity function and try to figure out the distance function, i.e. we want to do the opposite as last time, where we found the derivative; we want to find the antiderivative.
<!--more-->

### Integration
Let's take the example from last time but only focus on the velocity. If we want to find the antiderivative, we could ask ourselves, what function when taking the derivative gives us the velocity function. In that case, we have essentially solved our problem of finding the antiderivative, but we're going to take a different approach. Let's say you run a constant $10$ meters per second, so you finish the $100$ meter sprint in $10$ seconds. If we plot the velocity function with time on the x-axis, and velocity $\left( \frac{\text{distance}}{\text{time}} \right)$ on the y-axis (like below), we can think of area on the plot as distance, since

$$\text{velocity} \times \text{time} = \frac{\text{distance}}{\text{time}} \times \text{time} = \text{distance}.$$

<video width="500" height="310" loop muted autoplay>
    <source src="../extra/bslialo-notes-9c/fig_02.mp4" type="video/mp4">
</video>

I know it sounds weird to have distance be area, but try and stick with it. The plot above illustrates, how the area equals the distance traveled. Take some time to study the plot above, and let this idea become clear. Now, it's easy to find the area, when the velocity is constant, since we're just dealing with a rectangle - so let's try and step it up a notch.

Let's say, the velocity function follows the parabola $v(t)=t(10-t)=10t-t^2$. A quick <a href="{{ site.url }}/pages/bslialo-notes-9b">extrema</a> analysis tells us, this function increases from $v(t) = 0$ at $t=0$ up to a maximum $v(t) = 25$ at $t=5$, and then decreases again to $v(t)=0$ at $t=10$. To find the area between this velocity function and the x-axis, we could use the rectangle as inspiration and try to fill rectangles under the curve. Let's chop the function up in $6$ rectangles, making their widths equal $\frac{10}{6}$ - and if we choose the rectangles' upper left corners to touch the function, then it would look something like the plot below.

<video width="500" height="310" loop muted autoplay>
    <source src="../extra/bslialo-notes-9c/fig_03.mp4" type="video/mp4">
</video>

We end up with six rectangles as wanted, where each rectangle's height is given by the point, where the upper left corner touches the velocity function. The height of the first rectangle is $v(0) = 0\cdot (10-0) = 0$, the height of the second rectangle is $v \left( \frac{10}{6} \right) = \frac{10}{6} \cdot \left( 10 - \frac{10}{6} \right) \approx 14$, the height of the third rectangle is $v \left( \frac{20}{6} \right) = \frac{20}{6} \cdot \left( 10 - \frac{20}{6} \right) \approx 22$, etc. The widths of all the rectangles are obviously $\frac{10}{6}$, as we defined, so we can write the area as

$$ \begin{aligned}
\text{Area}
&= \frac{10}{6} \cdot v(0) + \frac{10}{6} \cdot v \left( \frac{10}{6} \right) + \frac{10}{6} \cdot v \left( \frac{20}{6} \right) + \cdots + \frac{10}{6} \cdot  v \left( \frac{50}{6} \right).
\end{aligned} $$

If we call the points, where the rectangles touch the velocity function, $t_0, t_1, \dots, t_5$, we can write this as the sum

$$
\text{Area} = \sum_{n=0}^{5} v \left( t_n \right) \cdot \frac{10}{6}.
$$

We can write this even more generalized, if we let $N$ be the number of rectangles, and $a,b$ be the endpoints of the interval. So in our case $N=6$, and $a=0,b=10$. We could write this as

$$
\text{Area} = \sum_{n=0}^{N-1} v \left( t_n \right) \cdot \frac{b-a}{N}. \quad \quad (1)
$$

Obviously, we are not going to get a good approximation of the area under the velocity function with only six rectangles, but by increasing the number of rectangles our approximation will get closer and closer to the actual area. To do that, we want the width of the rectangles to get *infinitesimally* small, which means, they're as close to $0$ as possible. We can interpret this another way; if we want the width of the rectangles $\left( \frac{b-a}{N} \right)$ to get infinitesimally small, we can take the <a href="{{ site.url }}/pages/bslialo-notes-9a">limit</a> of $(1)$ as $N$ approaches infinity

$$
\text{Area} = \lim_{N \to \infty} \sum_{n=0}^{N-1} v \left( t_n \right) \cdot \frac{b-a}{N}. \quad \quad (2)
$$

The plot below illustrates how the area is refined as the number of rectangles increase.

<video width="500" height="310" loop muted autoplay>
    <source src="../extra/bslialo-notes-9c/fig_04.mp4" type="video/mp4">
</video>

This is the intuition behind integration, and what we wrote in $(2)$ is the general idea of an integral[^1]. Usually, we rewrite $(2)$ as

$$
\lim_{N \to \infty} \sum_{n=0}^{N-1} v \left( t_n \right) \Delta t, \quad \quad (3)
$$

where $\Delta t = \frac{b-a}{N}$ to signify the width, and $t_n = a + n \cdot \Delta t$. This is called a *definite* integral, which is an integral with a lower and upper limit, $a$ and $b$. To shorten this even further, we use the integral sign $\int$, and write $(3)$ as

$$
\int_a^b v(t) dt. \quad \quad (4)
$$

The integral sign represents the sum of the infinitesimally narrow rectangles between $a$ and $b$ under the function $v(t)$. This is read as: the integral from $a$ to $b$ of $v(t)$.

### The fundamental theorem of calculus
Let's take a moment to go through, what we've just done. Our original question was, whether or not we could find a distance function purely by looking at the velocity function. We reasoned that since $\text{velocity} \times \text{time} = \text{distance}$, then the area underneath the velocity function from start to finish, would be the distance traveled from start to finish. To calculate the area underneath the velocity function, we chopped it up into a bunch of infinitesimally narrow rectangles, and then found the area of the rectangles with the width and height of each of them. From this, we can say

$$
s(T) = \int_0^T v(t) dt, \quad \quad (5)
$$

i.e., the distance traveled from $t=0$ to $t=T$ (or $10$ if we want ten seconds) is the same as the integral from $t=0$ to $t=T$ of the velocity function. In <a href="{{ site.url }}/pages/bslialo-notes-9a">notes 9a</a> we talked about the derivative as the instantaneous rate of change of a function - if we consider $s(T)$ (the area under the velocity function) as a function on its own, we can deduce its derivative. If we denote the instantaneous change in time as $dT$, then the change in area can be approximated by a rectangle as before, where the height is the velocity function $v(T)$. In other words, if the time changes by a tiny amount $dT$, then the area under the velocity function changes by the rectangle $v(t)dT$, which gives us

$$ \begin{aligned}
ds(T) &= v(T)dT \\
\frac{d}{dT}s(T) &= v(T).
\end{aligned} $$

This is the first part of the fundamental theorem of calculus[^2]; let $f$ be some function, and $F$ the function of the area under $f$ (the integral of $f$), i.e.

$$
F(x) = \int_a^x f(t) dt,
$$

then the derivative of $F$ is equal to the original function $f$

$$
F'(x) = f(x). \quad \quad (6)
$$

The next question to tackle is then: how do we compute this? Well, $(6)$ gives us a hint that we actually mentioned in the beginning. To find the integral we compute the *indefinite* integral or the *antiderivative*, which is the integral without a lower or upper limit. We ask ourselves: what function when taking the derivative gives us $v(t)=10t-t^2$? We know that the derivative of $t^3$ is $3t^2$, so we can multiply this by $-1/3$ to get the second term - and the derivative of $t^2$ is $2t$, so multiplying this by $5$ gives us the first term. At the end we have

$$ \begin{aligned}
\int v(t) dt &= \int 10t-t^2 dt \\
&= 5t^2 - \frac{1}{3} t^3 + c.
\end{aligned} $$

The $c$ is the potential constant that we lose after taking the derivative.

The second and final part of the fundamental theorem of calculus follows from the first part. Given $f$ and its antiderivative $F$, we can say

$$
\int_a^b f(x) dx = F(b)-F(a).
$$

#### Example:
Let's take the definite integral

$$ \begin{aligned}
\int_{1}^e \frac{1}{x} dx,
\end{aligned} $$

where $e$ is [Euler's number](https://en.wikipedia.org/wiki/E_(mathematical_constant)){:target="_blank"}. We start by finding the antiderivative of $\frac{1}{x}$, which from <a href="{{ site.url }}/pages/bslialo-notes-9b">notes 9b</a> we know is $\ln x$, and then we can compute the integral

$$ \begin{aligned}
\int_{1}^e \frac{1}{x} dx = \ln(e) - \ln(1) = 1 - 0 = 1.
\end{aligned} $$



[^1]: Not the rigorous definition of the [Riemann integral](https://en.wikipedia.org/wiki/Riemann_integral#Riemann_integral){:target="_blank"}.
[^2]: Not the rigorous [theorem](https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus){:target="_blank"}.
