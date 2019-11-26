---
title: "The bare minimum guide to LaTeX"
layout: post
tags: bare_min_guide
excerpt_separator: <!--more-->
---
A few people have been asking for a short guide to LaTeX, but since I don't have that much time on my hands these days, I thought I'd start with a very short guide that I can expand if needed.

### Why?
You can think of LaTeX as a programming language for documents. It's well-suited for large projects and complicated document structures, as it keeps track of a bunch of things by itself (we won't get into those things in this post though). The other huge plus for LaTeX is the ability to write complicated mathematical equations simple and beautiful.

### Getting started with Overleaf
While it's possible to install LaTeX and a LaTeX editor on your computer, I think using Overleaf (version 2) is the best choice for most; you won't have to find a proper LaTeX installation, worry about a million LaTeX files, deal with packages, figure out how to collaborate with other people, or worry about having access to your documents on different computers.\\
Firstly, go to [this link](https://www.overleaf.com?r=094710d5&rm=d&rs=b){:target="_blank"} (this is a referral link that gives me a few bonuses on Overleaf - it won't have any affect on you, but if you prefer not to use this, then go to Google and search for Overleaf v2) and sign up for an Overleaf (version 2) account. Secondly, go back to Overleaf and log in. Thirdly, you should see a green button in the top left that says "New Project". Click the button and choose "Blank Project". It will ask you to name your project, which can be whatever you want (it can be changed later if needed), and then press "Create".
<!--more-->

### The structure of a LaTeX document
You should see a document on the right side of your screen, a bit of code in the middle, and an overview of your project on the left (that only contains `main.tex`). If you don't see the document on the right, then there should be a tiny button in the top right (below "Chat") that looks like two arrows pointing at each other. Hover over the button and it should say "Split screen". If you click the button, your document should appear.

Let's look at the code now. I've posted below, what your code should look like (except for a few things).

{% highlight latex %}
\documentclass{article}
\usepackage[utf8]{inputenc}

\title{The bare minimum guide to LaTeX}
\author{Cookieblues}
\date{April 2019}

\begin{document}

\maketitle

\section{Introduction}

\end{document}
{% endhighlight %}

At first, it can look a bit daunting, but let's try and decompose the different parts. The first line specifies what kind of document you want to write. In this case it defaults to an `article`, which is probably what most documents should be. The second line imports the package "`inputenc`". The next three lines of code specifies some metadata about the document; the title, author and date. All of this is called the **preample**, because it comes before the actual document. This is where, you can make changes to the structure of your document, i.e., the size of the margins, the size of the font, define specific functions, change the layout, etc. However, we won't dive into all these things in this guide. We'll only change the date from `\date{April 2019}` to `\date{\today}`.\\
Next up is the actual document, which is signified by the command `\begin{document}` (which is followed by `\end{document}`, when the document ends). This is where, you'll write your actual paper. To understand how to do this, we'll have to learn a bit of LaTeX code.

### Writing LaTeX
As can be seen from the code above, most commands in LaTeX follow one of two standards: either `\begin{command}` followed by `\end{command}` or just `\command`. Usually, a backslash `\` signifies a command, and the brackets`{` `}` is where you put the arguments for the command. An example is in the preample of our document, where we use the command `\author{}` and feed it the argument `Cookieblues`. Another is the `\maketitle` command in our document. It doesn't take any arguments, but it writes the title, author, and date that we defined in our preample. We also use the command `\section{}`, which naturally creates a section in our document with the argument as the header. If we want to make a subsection in that section, we just use `\subsection{}`.\\
You might've noticed, there's a number next to the section. This is used for your table of contents. Let's add a table of contents right after our title and before our introduction. We can do this with the command `\tableofcontents`. If we don't want to have a section or subsection appear in the table of contents (and thereby not have a number next to it), we can put an asterisk at the end of the section command like `\subsection*{No number}`. Let's add this subsection to our document as well. Our code should now look like the one below.

{% highlight latex %}
\usepackage[utf8]{inputenc}

\title{The bare minimum guide to LaTeX}
\author{Cookieblues}
\date{\today}

\begin{document}

\maketitle

\tableofcontents

\section{Introduction}
\subsection*{No number}
% this is a comment that won't appear in the document

\end{document}
{% endhighlight %}

You might have noticed the small comment after the subsection. If you want to write comments in your LaTeX code, you can use `%`.

### Text
If you want to write something in your document, you just do it. No need for special commands, you just write what you want, where you want it. I'll write "`This is the introduction`" under the introduction section, and I'll write "`This is the subsection under the introduction`". The commands for **bold** and *italic* text are `\textbf{bold}` and `\textit{italic}` respectively.

### Equations
This is where LaTeX shines! And why it's the default tool for the vast majority of natural scientific papers. If you want to write an equation, you can use the `\begin{equation}` command, then write your equation, and end it with `\end{equation}`. I use LaTeX equations on this website as well, and here are a couple of examples of regular functions:
{% highlight latex %}
\begin{equation}
x+y
\end{equation}
{% endhighlight %}

$$
x+y
$$

{% highlight latex %}
\begin{equation}
\sqrt{2}
\end{equation}
{% endhighlight %}

$$
\sqrt{2}
$$

{% highlight latex %}
\begin{equation}
\sin(x)
\end{equation}
{% endhighlight %}

$$
\sin(x)
$$

{% highlight latex %}
\begin{equation}
\tan(x)
\end{equation}
{% endhighlight %}

$$
\tan(x)
$$

{% highlight latex %}
\begin{equation}
\sqrt{\exp(\cos(2x))}
\end{equation}
{% endhighlight %}

$$
\sqrt{\exp(\cos(2x))}
$$

#### Super- and subscripts

{% highlight latex %}
\begin{equation}
x^2
\end{equation}
{% endhighlight %}

$$
x^2
$$

{% highlight latex %}
\begin{equation}
a_{12}
\end{equation}
{% endhighlight %}

$$
a_{12}
$$

{% highlight latex %}
\begin{equation}
e^{a+b} = e^a e^b
\end{equation}
{% endhighlight %}

$$
e^{a+b} = e^a e^b
$$

{% highlight latex %}
\begin{equation}
\sin^2(x) + \cos^2(x) = 1
\end{equation}
{% endhighlight %}

$$
\sin^2(x) + \cos^2(x) = 1
$$

#### Fractions

{% highlight latex %}
\begin{equation}
\frac{1}{2} = 1/2
\end{equation}
{% endhighlight %}

$$
\frac{1}{2} = 1/2
$$

{% highlight latex %}
\begin{equation}
\frac{1}{\sin(x)}
\end{equation}
{% endhighlight %}

$$
\frac{1}{\sin(x)}
$$

{% highlight latex %}
\begin{equation}
\frac{x+\frac{1}{x}}{x^2-1}
\end{equation}
{% endhighlight %}

$$
\frac{x+\frac{1}{x}}{x^2-1}
$$

{% highlight latex %}
\begin{equation}
(f/g)' = \frac{f'g-fg'}{g^2}
\end{equation}
{% endhighlight %}

$$
(f/g)' = \frac{f'g-fg'}{g^2}
$$

#### Integrals, sums, and other operators

{% highlight latex %}
\begin{equation}
\int x^3 dx + \sum_{n=1}^{N} n
\end{equation}
{% endhighlight %}

$$
\int x^3 dx + \sum_{n=1}^{N} n
$$

{% highlight latex %}
\begin{equation}
\int_0^1 \frac{1}{x} dx + \sum_{a,b} a-b
\end{equation}
{% endhighlight %}

$$
\int_0^1 \frac{1}{x} dx + \sum_{a,b} a-b
$$

{% highlight latex %}
\begin{equation}
\int_0^\pi \sin (x) dx + \sum_{n=1}^N \frac{1}{n}
\end{equation}
{% endhighlight %}

$$
\int_0^\pi \sin (x) dx + \sum_{n=1}^N \frac{1}{n}
$$

{% highlight latex %}
\begin{equation}
\int \frac{x^{\sin (x)}}{\sqrt{\cos (x)}} dx + \sum_{n=1}^N \frac{n}{n+1}
\end{equation}
{% endhighlight %}

$$
\int \frac{x^{\sin (x)}}{\sqrt{\cos (x)}} dx + \sum_{n=1}^N \frac{n}{n+1}
$$

#### Greek letters

{% highlight latex %}
\begin{equation}
2\pi
\end{equation}
{% endhighlight %}

$$
2\pi
$$

{% highlight latex %}
\begin{equation}
|x-a| < \delta
\end{equation}
{% endhighlight %}

$$
|x-a| < \delta
$$

{% highlight latex %}
\begin{equation}
\varphi = \frac{1+\sqrt{5}}{2}
\end{equation}
{% endhighlight %}

$$
\varphi = \frac{1+\sqrt{5}}{2}
$$

{% highlight latex %}
\begin{equation}
\int_0^\pi \sin (x) dx
\end{equation}
{% endhighlight %}

$$
\int_0^\pi \sin (x) dx
$$

#### Brackets
Square brackets are just plainly written `[` and `]`, curly brackets require a backslash beforehand `\{` `\}` as they are otherwise used for wrapping arguments in LaTeX. If the expression is large, you can write `\left` and `\right` before the paranthesis to make LaTeX adjust the size of them for your expression. Here are some examples:

{% highlight latex %}
\begin{equation}
\{1,2,3,4\}
\end{equation}
{% endhighlight %}

$$
\{1,2,3,4\}
$$

{% highlight latex %}
\begin{equation}
y - \left( \frac{1}{x} \right)^2 = 0
\end{equation}
{% endhighlight %}

$$
y - \left( \frac{1}{x} \right)^2 = 0
$$

{% highlight latex %}
\begin{equation}
\left( \int_0^t \log (y) dy \right)^t
\end{equation}
{% endhighlight %}

$$
\left( \int_0^t \log (y) dy \right)^t
$$

{% highlight latex %}
\begin{equation}
\int_a^b \frac{x}{b-a} dx = \left[ \frac{x}{b-a} \right]^b_a
\end{equation}
{% endhighlight %}

$$
\int_a^b \frac{x}{b-a} dx = \left[ \frac{x}{b-a} \right]^b_a
$$

### Final tips
You might've noticed that your document didn't change even though you changed your LaTeX code. This is because LaTeX is just that: code. There's a big green button that says "Recompile" in the top left of your document. If you click it, the new code, you have written, will be executed, and you will see it in your document (or you get an error, if there's a mistake in your code). To the right of the button is a small downward pointing arrow - if you click that, you can turn "Auto compile" on or off. This will get Overleaf to compile your code regularly as you write it.

When you get started writing mathematics in LaTeX, often times you'll find yourself in need of symbols that you don't know the name of and definitely not the LaTeX code for. In these cases, you could either Google your way to the answer, or use the brilliant site of [Detexify](http://detexify.kirelabs.org/classify.html){:target="_blank"}. You simply use your mouse to draw the symbol that you want, and Detexify tries to identify the most probably symbols that you're looking for - and not only does it detect the symbol, but it also provides you with the package it's from (in case it requires one). It's a very useful tool that is worth a bookmark!

### Exercises
To practice writing equations, try and see if you can write the equations underneath.

$$
a^z + b^z = c^z
$$

$$
\sqrt{\frac{n}{n-1}}
$$

$$
e^{ix} = r ( \cos \theta + i \sin \theta )
$$

$$
\int \frac{\sin (x)}{x^2+1} dx
$$

$$
\int_a^b x^{10} \sum_{i=1}^n i^2 dx
$$

These next ones require something I haven't shown in this post, so a little bit of Googling or outside-the-box thinking is required.

$$
1+2+3+\cdots+n = \frac{n(n+1)}{2}
$$

$$
\lim_{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0} = c
$$

$$
\frac{1}{\zeta (s)} = \prod_{p \text{ prime}} \left( 1 - \frac{1}{p^s} \right)
$$

$$
\det
\begin{pmatrix}
    a & b \\
    c & d
\end{pmatrix}
= ad-bc
$$

$$
\max \left\{ 0, \left| \frac{1}{a}-b \right| \right\}
$$
