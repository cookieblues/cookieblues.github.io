---
title: "BSLIALO, notes 10: Taylor polynomials and Newton-Raphson's method"
layout: post
category: Linear Algebra and Optimisation
tags: BSLIALO
excerpt_separator: <!--more-->
---
Now that we're past the introductory calculus stuff, we can start to look at some applications of calculus. This week can be considered the week of approximation; we are going to approximate functions as polynomials (Taylor polynomials), and approximate roots of functions (Newton-Raphson's method).\\
It's important to note that Newton-Raphson's method is used in both [optimisation](https://en.wikipedia.org/wiki/Newton's_method_in_optimization){:target="_blank"} and [general calculus](https://en.wikipedia.org/wiki/Newton%27s_method){:target="_blank"}. Since the method is the same and only the contexts differ, I will not distinguish between the two. Keep in mind though, "Newton's method" and "Newton-Raphson's method" are the same - I'll refer to it as Newton-Raphson's method though.

### Taylor polynomials
Let's say, we want to approximate $\cos (x)$ as a polynomial of degree four near $x=0$, i.e., we want to find $k_0, \dots, k_4$ so

$$
\cos (x) = k_0 + k_1 x + k_2 x^2 + k_3 x^3 + k_4 x^4.
$$

<!--more-->
Since we want to estimate near $x=0$, we notice that all the terms except for $k_0$ becomes zero, since $x$ is a factor in all the other terms. We therefore have $\cos(x) = k_0$, and at $x=0$ we get $\cos(0) = 1 = k_0$. Our polynomial then becomes

$$
\cos (x) = 1 + k_1 x + k_2 x^2 + k_3 x^3 + k_4 x^4.
$$

Now, we can look at the derivatives of cosine and our polynomial. Taking the derivative on both sides gives

$$ \begin{aligned}
\frac{d}{dx} \cos (x) &= \frac{d}{dx} \left( 1 + k_1 x + k_2 x^2 + k_3 x^3 + k_4 x^4 \right) \\
-\sin (x) &= k_1 + 2 k_2 x + 3 k_3 x^2 + 4 k_4 x^3, \quad \quad (1)
\end{aligned} $$

and using the same reasoning as before, we can see that all terms in $(1)$ will be zero except for $k_1$. We end up with $-\sin (x) = k_1$, which at $x=0$ gives $-\sin (0) = 0 = k_1$, and our polynomial is now

$$ \begin{aligned}
\cos (x) &= 1 + 0 x + k_2 x^2 + k_3 x^3 + k_4 x^4 \\
&= 1 + k_2 x^2 + k_3 x^3 + k_4 x^4.
\end{aligned} $$

Then we do it again with the second derivative which gives us 

$$ \begin{aligned}
\frac{d}{dx} -\sin (x) &= \frac{d}{dx} \left( 0 + 2 k_2 x + 3 k_3 x^2 + 4 k_4 x^3 \right) \\
-\cos(x) &= 2 k_2 + 6 k_3 x + 12 k_4 x^2.
\end{aligned} $$

Once again, all terms except $2k_2$ will be zero at $x=0$. We're then left with $-\cos(x) = 2 k_2$, which at $x=0$ gives $-\cos(0) = -1 = 2 k_2$, which in turn makes $k_2 = -\frac{1}{2}$, and our polynomial is now

$$ \begin{aligned}
\cos (x) &= 1 + 0 x - \frac{1}{2} x^2 + k_3 x^3 + k_4 x^4 \\
&= 1 - \frac{1}{2}x^2 + k_3 x^3 + k_4 x^4.
\end{aligned} $$

Continuing this process, and taking the third derivative gives us

$$ \begin{aligned}
\frac{d}{dx} -\cos(x) &= \frac{d}{dx} \left( 2 k_2 + 6 k_3 x + 12 k_4 x^2 \right) \\
\sin(x) &= 6 k_3 + 24 k_4 x.
\end{aligned} $$

All terms except $k_3$ will be zero at $x=0$, i.e., $\sin(0) = 0 = 6 k_3$, which makes $k_3 = 0$. Our polynomial is then

$$ \begin{aligned}
\cos (x) &= 1 + 0 x - \frac{1}{2} x^2 + 0 x^3 + k_4 x^4 \\
&= 1 - \frac{1}{2}x^2 + k_4 x^4.
\end{aligned} $$

Repeating this procedure one more time with the fourth derivative yielding

$$ \begin{aligned}
\frac{d}{dx} \sin(x) &= \frac{d}{dx} \left( 6 k_3 + 24 k_4 x \right) \\
\cos(x) &= 24 k_4,
\end{aligned} $$

brings us back to $\cos(x)$. At $x=0$ we have $\cos(0) = 1 = 24 k_4$, which makes $k_4 = \frac{1}{24}$. We have finally found all the coefficients to our polynomial, which is

$$
1 - \frac{1}{2} x^2 + \frac{1}{24} x^4.
$$

Underneath is shown an animation of each iteration of this process. Notice how the polynomial only changes when the degree is even. As we saw above, this is because the coefficients for the terms of odd powers are zero.

<video width="500" height="310" loop muted autoplay>
    <source src="{{ site.url }}/pages/extra/bslialo-notes-10/fig_01.mp4" type="video/mp4">
</video>

Alright, I know that was a bit of a mouthful to get through, so let's get to the point of the Taylor's theorem

Let's go through this process one more time, and try to approximate $\cos (x)$ as a polynomial of degree four at $x=\frac{\pi}{2}$, but this time we'll pay more attention to what we're doing.


Taylor polynomial: if $f$ is $n$ times differentiable at the point $x_0$, then

$$
T_n f(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
$$

Taylor's theorem with remainder. Assume $f$ and its $n+1$th derivative are continuous in $[a,b]$, then

$$
f(b) = T_n f(b) + \frac{1}{n!} \int_a^b f^{(n+1)}(t) (n-t)^n dt
$$

Corollary: if you let $M \in \mathbb{R}$ be $ \| f^{(n+1)}(t) \| \leq M $ for all numbers $t$ between $a$ and $x$ then

$$
|R_n f(x)| \leq \frac{M}{(n+1)!} |x-a|^{n+1}
$$

hey

### Newton-Raphson's method
Next, we'll look at a root-finding algorithm, and afterwards we'll see the use of it in optimization.



The two-term Taylor polynomial is

$$ \begin{aligned}
f(x) &= \frac{f(x_0)}{0!}(x-x_0)^0 + \frac{f'(x_0)}{1!}(x-x_0)^1 + \frac{f''(\xi)}{2!}(x-x_0)^2 \\
&= f(x_0) + f'(x_0)(x-x_0) + \frac{1}{2}
\end{aligned} $$

for some $\xi$ between $x_0$ and $x$.
Since we want to find the root of $f$, we let $f(x)=0$, so

$$ \begin{aligned}
0 &= f(x_0) + f'(x_0)(x-x_0) \\
-f(x_0) &= f'(x_0)(x-x_0) \\
-\frac{f(x_0)}{f'(x_0)} &= x-x_0 \\
x_0 -\frac{f(x_0)}{f'(x_0)} &= x
\end{aligned} $$


Why do newtons method and taylors theorem look the same?
They are the same! Newton’s method is simply the Taylor series approximated only by the linear parts, and with the assumption that the next iteration is a zero of the function.


