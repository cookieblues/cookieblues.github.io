---
title: "BSLIALO, notes 9a: The derivative, the limit, and the concept of approach"
layout: post
category: Linear Algebra and Optimisation
tags: BSLIALO
excerpt_separator: <!--more-->
---
Imagine you're participating in a $100$ metres sprint race. When you hear the starter's pistol, you accelerate for dozens of metres, i.e. your velocity will increase until you reach your maximum speed. Let's assume, you reach your maximum speed $5$ seconds into the race, after which you start to fatigue and decelerate - and let's also assume, you finish the race in $10$ seconds. If we let $s(t)$ be the distance you've traveled at time $t$, and $v(t)$ your velocity at time $t$, then we can draw your velocity and the distance you've traveled in a plot like the one below.

<span class="marginnote">Notice how towards the middle of the race you're traveling more metres per unit of time than at the beginning and end.</span>
<figure>
    <video width="500" height="310" loop muted autoplay>
        <source src="{{ site.url }}/extra/bslialo-notes-9a/fig_01.mp4" type="video/mp4">
    </video>
</figure>

<!--more-->

We know that to calculate velocity, we take the ratio of the distance traveled and the time it took. If we start at $s(t_1)$ and end at $s(t_2)$, we say

$$v_{\text{average}} = \frac{s(t_2)-s(t_1)}{t_2-t_1}.$$

We can write this more formally as the average velocity from $t_1$ to some amount of time after that, if we use the time difference $t_2-t_1=\Delta t$. This gives us

$$v_{\text{average}} = \frac{s(t_1 + \Delta t)-s(t_1)}{\Delta t}. \quad \quad (1)$$

This is a **change** in distance divided by a **change** in time, but if we were to ask, how fast you were running at an instant, the question doesn't seem to make sense. Because no distance is traveled in a single point in time, and no time has passed in an instant. Yet, in the plot above we have a function $v(t)$ that seemingly gives us the velocity at any point in time. The function gives us the **instantaneous rate of change** of distance.

### Approach and limits
To understand this phenomenon of **instantaneous change**, we have to talk about the concept of approach. Let's look at the function $f(x) = x^2+1$. Imagine we had to figure out what $f(0)$ is equal to, without inserting $0$ into the function. One way of doing it could be to start from a number higher than $0$ (let's call it $a$) and gradually evaluate the function while decreasing $a$. This would give us a sequence

$$ \begin{aligned}
f(1)&=2, \quad &\text{when } a&=1 \\
f(0.5)&=1.7, \quad &\text{when } a&=0.5 \\
f(0.25)&=1.5, \quad &\text{when } a&=0.25 \\
f(0.125)&=1.35, \quad &\text{when } a&=0.125,
\end{aligned} $$

and so on. Now, we know that $f(0)=0^2+1=1$, but let's say that we didn't know or were unable to do this calculation.
How would we go about showing that $f(0)=1$ without actually evaluating it?

Well, if we can show for any value $c$ that we can get closer to $1$ for some value $x_c$, then that's pretty good.
That is, if we're given a value $c$ (close to $1$), we want to show that we can find a value $x_c$ that gets $f(x)$ closer to $1$ than $c$ is.
Formally, this means that for all possible values of $c$, we must be able to find a value $x_c$ that satisfies $\mid 1-f(x_c) \mid < \mid 1-c \mid $.
If we can be certain about this, then we can say that $f(x)$ approaches $1$ as $x$ approaches $x_c$<span class="sidenote-number"></span>.
<span class="sidenote">This is not the [rigorous definition of a limit](https://en.wikipedia.org/wiki/(%CE%B5,_%CE%B4)-definition_of_limit#Precise_statement_and_related_statements).</span>

We can certainly do this! Let's say $c=1.01$, then we solve


$$ \begin{aligned}
f(x) &= 1.01 \\
x^2 + 1 &= 1.01 \\
x &= \sqrt{1.01-1} \\
x &= \pm 0.1
\end{aligned} $$

and choose $x_c$ to be between $-0.1$ and $0.1$. We can generalize this such that for a given $c$, we pick $x_c$ to be between $-\sqrt{c-1}$ and $\sqrt{c-1}$. The key thing here is, if we want to say that a function approaches a value, then we have to be able to get **arbitrarily close** to it - and this has to be the case, if we're approaching from either side of $x_c$ (higher or lower).

This is the concept of approach and the intuition behind limits. Suppose $f(x)$ is defined for all $x$ around $x_c$ but not necessarily at $x_c$. We can say

$$
\lim_{x \to x_c} f(x) = c, \quad \quad (2)
$$

if we can get $f(x)$ arbitrarily close to $c$ for values of $x$ close but not equal to $x_c$. Equation $(2)$ is read: "the limit of $f$ of $x$ as $x$ approaches $x_c$ equals $c$". Another way to write this is

$$
f(x) \to c \quad \text{as} \quad x \to x_c,
$$

which is read: "$f$ of $x$ approaches $c$ as $x$ approaches $x_c$".

#### Example:
Suppose we have to find the limit

$$
\lim_{x \to 1} \frac{1-\sqrt{x}}{1-x}.
$$

The problem here is that we cannot insert $x=1$ into the fraction, as we would then divide by $0$. Instead, we do a bit of algebraic manipulation to get a limit, we can evaluate

$$ \begin{aligned}
\lim_{x \to 1} \frac{1-\sqrt{x}}{1-x}
&= \lim_{x \to 1} \frac{1-\sqrt{x}}{(1-\sqrt{x})(1+\sqrt{x})} \\
&= \lim_{x \to 1} \frac{1}{1+\sqrt{x}} \\
&= \frac{1}{1+\sqrt{1}} \\
&= \frac{1}{2}.
\end{aligned} $$

### Derivatives
If we return to our initial example of the sprint race, we asked ourselves: how fast were you running at a point in time? With our new knowledge of approach and limits, we can rephrase the question and instead ask: what happens when $\Delta t$ approaches $0$ in equation $(1)$? The question asks us to find

$$
v(t) = \lim_{\Delta t \to 0} \frac{s(t+\Delta t)-s(t)}{\Delta t}. \quad \quad (3)
$$

<span class="marginnote">The animation illustrates how $v(t)$ changes as $\Delta t$ approaches $0$.</span>
<figure>
    <video width="500" height="310" loop muted autoplay>
        <source src="{{ site.url }}/extra/bslialo-notes-9a/fig_02.mp4" type="video/mp4">
    </video>
</figure>

As can be seen above, the velocity turns out to be the slope or tangent line of the distance. This is also what we call the derivative of the distance function. This is usually denoted

$$
\frac{d}{dt}s(t) = v(t),
$$

where $\frac{d}{dt}$ is the differentiation operator.
<span class="marginnote">Differentiation is the process of finding a derivative.</span>
Using the common notation $y=f(x)$ to show that the independent (free) variable is $x$ and the dependent variable is $y$, we can write up several notations for the derivative:

$$ \frac{df}{dx} = \frac{dy}{dx} = \frac{d}{dx}f(x) = f'(x) = y' = Df(x) = D_x f(x).$$

#### Example:
Let $f(x) = x + \frac{1}{x}$. Let's try to find the derivative using the definition from $(3)$. We see

$$ \begin{aligned}
f'(x)
&= \lim_{\Delta x \to 0} \frac{f(x+\Delta x)-f(x)}{\Delta x} \\
&= \lim_{\Delta x \to 0} \frac{x+\Delta x + \frac{1}{x + \Delta x} - \left( x + \frac{1}{x} \right)}{\Delta x} \\
&= \lim_{\Delta x \to 0} \frac{\Delta x + \frac{1}{x + \Delta x} - \frac{1}{x}}{\Delta x} \\
&= \lim_{\Delta x \to 0} 1 + \frac{x - (x + \Delta x)}{\Delta x (x + \Delta x)x} \\
&= \lim_{\Delta x \to 0} 1 - \frac{1}{(x + \Delta x)x} \\
&= 1 - \frac{1}{x^2},
\end{aligned} $$

which is the actual derivative.

### Final thoughts
One of my professors once said: "differentiation is mechanics and integration is art". At first it just sounded like a crap quote, but it's more of a general saying than a quote really. Differentiation is mostly tedious calculation, and you just have to practice it a lot to learn it. However, integration often requires some creativity, but we'll get to that later on. I'm considering uploading a few exercises after this first week of calculus that try and teach some core tips and tricks of differentiation and integration.

