---
title: "BSLIALO, notes 11: Motion along a curve"
layout: post
tags: BSLIALO
excerpt_separator: <!--more-->
---
### Notation
Before we get onto the subject of vector functions, it's critical to understand the notation. Unfortunately, the most common notation is confusing to most students in the beginning, which is why I'll take a paragraph or two to explain, what's going on.

As it's a prerequisite for this course, you must've heard of unit vectors before. These are simply vectors of length $1$. The 'standard' unit vectors are

$$
    \mathbf{i} =
    \begin{pmatrix}
        1 \\
        0 \\
        0 \\
    \end{pmatrix},
    \quad
    \mathbf{j} =
    \begin{pmatrix}
        0 \\
        1 \\
        0 \\
    \end{pmatrix},
    \; \; \text{and} \; \;
    \mathbf{k} =
    \begin{pmatrix}
        0 \\
        0 \\
        1 \\
    \end{pmatrix}.
$$

<!--more-->
We can therefore write

$$ \begin{aligned}
    \begin{pmatrix}
        1 \\
        2 \\
        3
    \end{pmatrix}
    &= 1 \cdot
    \begin{pmatrix}
        1 \\
        0 \\
        0 \\
    \end{pmatrix}
    + 2 \cdot 
    \begin{pmatrix}
        0 \\
        1 \\
        0 \\
    \end{pmatrix}
    + 3 \cdot
    \begin{pmatrix}
        0 \\
        0 \\
        1 \\
    \end{pmatrix} \\
    &= \mathbf{i} + 2 \mathbf{j} + 3 \mathbf{k}.
\end{aligned} $$

Usually, when we're talking about vectors, we're talking about *column* vectors

$$
    \mathbf{u} = 
    \begin{pmatrix}
        2 \\
        3 \\
        7
    \end{pmatrix},
$$

which are plainly written in columns. However, there are also *row* vectors

$$
    \mathbf{v} = 
    \begin{pmatrix}
        2 & 3 & 7
    \end{pmatrix}.
$$

The transpose of column vectors are row vectors and vice versa

$$ \begin{aligned}
    \mathbf{u}^\intercal &= \mathbf{v} \\
    \mathbf{u} &= \mathbf{v}^\intercal.
\end{aligned} $$


