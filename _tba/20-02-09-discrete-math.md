---
title: "Crash course in discrete mathematics"
layout: post
tags: crash_course
excerpt_separator: <!--more-->
---
I study data science at the [IT University of Copenhagen](https://www.itu.dk/){:target="_blank"}, where there's a fair bit of mathematics. I feel that there's a presumption of mathematical understanding and rigor in a lot of the courses, which is never founded in the start of the programme. I used to study mathematics, and I was taught these things during a discrete mathematics course, so I've stitched the best bits and pieces together from that course with what I've learned since to create this short and (hopefully) useful crash course in discrete mathematics. The goal is that after reading this post, the reader should be able to read and write mathematics (better than before at least), as well as understand certain mathematical concepts a little better such as proofs, functions, combinatorics, etc.

So, what *is* discrete mathematics actually? It's kind of difficult to explain or define, but once you start doing discrete mathematics, it will become more evident. The word "discrete" comes from the Latin "discretus" which means separated, and I think that comes closest to explain it. Discrete mathematics studies mathematical structures that are *discrete*, which means *not continuous*. Commonly, discrete mathematics is described as dealing with countable things, but that does not mean finite; discrete structures can be both finite and infinite. Let's just dive into it though!

The guide will mainly focus on solving exercises and they will gradually get more difficult. Don't expect to solve the exercises quickly - spend at least 10 minutes on an exercise before you move on (or look at the solution). I've rated the exercises from one (easiest) to five (hardest).
<!--more-->

### Numbers
To begin with, we have to be familiar with the different kinds of numbers that we're dealing with. This is important when we start talking about certain properties that they each possess.

> **Definition 1** *The numbers $\dots, -3, -2, -1, 0, 1, 2, 3, \dots$ are called the set of **integers** (or **whole numbers**) and are denoted by $\mathbb{Z}$.*

> **Definition 2** *The positive integers $1, 2, 3, \dots$ are called the set of **natural numbers** and are denoted by $\mathbb{N}$. Commonly $\mathbb{N}_0$ denotes the set of natural numbers and $0$.*

> **Definition 3** *The numbers that can be written as fractions $\frac{a}{b}$, where $a$ and $b$ are integers and $b \not = 0$, are called the set of **rational numbers** and are denoted by $\mathbb{Q}$.*

In discrete mathematics, we'll mainly be dealing with integers, but we'll also touch on some properties of rational numbers.
<!--more-->

> **Theorem 4** *For any integers $x$, $y$, $z$, the following basic rules apply:*
>
> $$ \begin{aligned}
x+y &= y+x \\
(x+y)+z &= x+(y+z) \\
x+0 &= 0+x = x \\
x+(-x) &= (-x) + x = 0 \\
xy &= yx \\
(xy)z &= x(yz) \\
x \cdot 1 &= 1x = x \\
x(y+z) &= xy+xz, \quad (x+y)z = xz+yz \\
x &\leq x \\
\text{if } x &\leq y \text{ and } y \leq z \text{ then } x \leq z \\
\text{if } x &\leq y \text{ and } y \leq x \text{ then } x = y \\
\text{if } x &\leq y \text{ then } x+z \leq y+z \\
\text{if } x &\leq y \text{ and } 0 \leq z \text{ then } xz \leq yz
\end{aligned} $$

> **Definition 5** *An integer $d$ is called a **divisor** (or **factor**) of another integer $n$, if there exists an integer $q$ such that $dq=n$. We write $d \mid n$ and say "$d$ **divides** $n$", "$n$ is **divisible** by $d$", or "$n$ is a **multiple** of $d$".*

As an example, $12$ is divisible by $1$, $2$, $3$, $4$, $6$, and $12$. These are all the *positive* divisors of $12$. Likewise, $-39$, $26$, and $130$ are all multiples of $13$.

*Exercise 1 (1/5):* Determine all the divisors of 27, and all *positive* divisors of 31.

> **Theorem 6** *Let $n$ and $d$ be integers. If $d \mid n$, then $d \mid -n$.* \\
**Proof:** By definition 5 we know that there exists an integer $q$ such that $dq = n$. To show $d \mid -n$, we have to find an integer $q_1$ such that $dq_1 = -n$. Since $dq=n$ then $-dq = -n$, so $d \cdot (-q) = -n$. Since $q$ is an integer, then $-q$ must be an integer too. So if $q_1 = -q$, it satisfies $dq_1 = -n$ and shows that $d \mid -n$. $\square$

*Exercise 2 (2/5):* Let $n$ and $d$ be integers. Show that if $d \mid n$, then $-d \mid n$, and $-d \mid -n$.

*Exercise 3 (2/5):* Let $a$, $b$, and $c$ be integers. Show that if $a \mid b$ and $b \mid c$, then $a \mid c$.

*Exercise 4 (3/5):* The integers $n$ and $m$ satisfy $2 \mid n$ and $6 \mid m$. Show that $4 \mid m(m+n)$.

*Exercise 5 (3/5):* The integers $n$ and $m$ satisfy $n+m=n^2$. Show that $n \mid m$.

> **Definition 7** *1, -1, $n$, and $-n$ are called the **trivial divisors** of $n$. A divisor of $n$ that isn't trivial is called a **non-trivial divisor**.*

> **Definition 8** *An integer $n > 1$ is called a **prime number** (or just **prime**) if it only has trivial divisors. If $n$ is not a prime number, then it's called a **composite number**.*

The first $10$ prime numbers are therefore $2$, $3$, $5$, $7$, $11$, $13$, $17$, $19$, $23$, and $29$.

*Exercise 6 (1/5):* Determine all the prime numbers less than $50$.

> **Note 9** *The integer $1$ is neither a prime number nor a composite number.*

> **Definition 10** *A prime number that is a divisor in a number $n$ is called a **prime factor** of $n$.*

*Exercise 7 (1/5):* Determine all the prime factors of $30$.

> **Theorem 11** *Every integer $n>1$ has at least one prime factor. In particular, the smallest divisor larger than $1$ is a prime factor.* \\
**Proof:** Let $n>1$ be an integer, and $p>1$ the smallest divisor of $n$. If $p$ is not prime, then $p$ is a composite number and has a non-trivial divisor larger than $1$. It follows from exercise 3 that this divisor must also be a divisor of $n$, which contradicts that $p$ is the smallest divisor of $n$ that is larger than $1$. Therefore $p$ has to be prime and thereby a prime factor of $n$. $\square$

> **Definition 12** *The **prime factorization** of an integer $n>1$ is the product of primes equal to $n$, i.e. $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_m^{\alpha_m} $, where $p_i$ is prime, and $\alpha_i$ is a natural number.*

As an example, the prime factorization of $6$ is $2 \cdot 3$, and the prime factorization of $72$ is $2^3 \cdot 3^2$.

*Exercise 8 (1/5):* Determine the prime factorization of $180$ and $9009$.

> **Lemma 13 *Euclid's lemma*** *If $m$ and $n$ are integers, $p$ is prime, and $p \mid ab$, then $p \mid a$ or $p \mid b$.*

> **Theorem 14 *Fundamental theorem of arithmetic*** *Every integer $n>1$ has a unique prime factorization.*\\
**Proof:** We'll return to this after induction.

*Exercise 9 (2/5):* The product of $4$ distinct positive integers is equal to 2020. What is the sum of the $4$ integers?

What follows from the uniqueness of the prime factorization is that for integers $a$, $b$, $n$ larger than $1$, if $n=a \cdot b$, then the prime factorization of $n$ is equal to the product of the prime factorizations of $a$ and $b$.

*Exercise 10 (1/5):* If $n^2$ is divisible by a prime $p$, is $n$ also divisible by $p$?

> **Corollary 15** Let $p_1, p_2, \dots, p_m$ be $m$ distinct prime numbers, and let $\alpha_1, \alpha_2, \dots, \alpha_m$ be natural numbers. An integer $n$ is divisible by the product $p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_m^{\alpha_m}$ if and only if it's divisible by the numbers $p_1^{\alpha_1}, p_2^{\alpha_2}, \dots, p_m^{\alpha_m}$.\\
**Proof:** TBA.

As an example, if we want to show that an integer $n$ is divisible by $6$, it is enough to show that $n$ is divisible by $2$ and $3$.

*Exercise 11 (2/5):* Is $11011 \cdot 111$ divisible by $121$?

*Exercise 12 (3/5):* Show that the product of $3$ consecutive integers is divisible by $6$.

*Exercise 13 (3/5):* Show that the product of $5$ consecutive integers is divisible by $60$.

*Exercise 14 (4/5):* Show that $n^3-n$ is divisible by 6 for any integer $n$.

*Exericse 15 (5/5):* Let $a$ and $b$ be $2$ positive integers that sum to $2002$. Is it possible for $2002$ to divide $ab$?[^1]

*Exercise 16 (5/5):* It is true of three integers $a$, $b$, and $c$ that $a+b^2=c^2$. Show that $6$ divides $abc$.[^2]

*Exercise 17 (5/5):* Show that if $a$ and $b$ are integers and $a^2+b^2+9ab$ is divisible by $11$, then $a^2-b^2$ is divisible by $11$.[^3]



### Logic
Now we'll take a look at logic, which is essential to understanding and reading mathematics. Logic is the kind of word that gets thrown around in everyday conversation without having any reference to the analysis of argument.

> **Definition 16** *A (mathematical) **proposition** is a statement that is either true or false.*

Examples of propositions are $1 > 2$ and $1 < 2$, where the first is false and the second is true. However, $2+8$ and $\sin \pi$ are not propositions, as they are neither true nor false. What about the statement $x > 5$ though? It's not a proposition, because we haven't determined the value of $x$ yet, and hence cannot determine whether it's true or false. However, it will be a proposition once we assign a value to $x$. In this case, we call $x$ a **free variable**.

> **Definition 17** *A statement, which contains a free variable, is called a **predicate**.*

Predicates can have multiple free variables such as $a^2 + b^2 = c^2$.

> **Definition 18** *Let $p$ and $q$ be propositions. We define the following relationships between propositions represented by **connectives**:*
>
* ***Conjugation**: $p \wedge q$ is true, when both $p$ and $q$ are true or false. It's read "$p$ and $q$".*
* ***Disjunction**: $p \vee q$ is true, when either $p$ or $q$ are true or they both are true and false when both $p$ and $q$ are false. It's read "$p$ or $q$".*
* ***Negation**: $\neg p$ is true when $p$ is false, and false when $p$ is true. It's read "not $p$" or "non $p$".*
* ***Conditional (or implication)**: $p \Rightarrow q$ is false when $p$ is true and $q$ is false, otherwise it's true. It's read "if $p$ then $q$". Note that we can write the conditional the other way too $q \Leftarrow p$.*
* ***Biconditional**: $p \Leftrightarrow q$ is true if $p$ and $q$ have the same truth value. It's read "$p$ if and only if $q$".*

We can illustrate these definitions in a table, where we show all combinations of truth values for $p$ and $q$, and we can comebine connectives to create more complicated propositions. The table below shows the truth values of the connectives for all combinations of truth values for $p$ and $q$, and the column to the right has a more complicated proposition.

| $p$ | $q$ | $p \wedge q$ | $p \vee q$ | $\neg p$ | $p \Rightarrow q$ | $p \Leftrightarrow q$ | $(\neg (p \wedge q)) \wedge (p \vee q)$ |
|:---:|:---:|:------------:|:----------:|:--------:|:-----------------:|:---------------------:|:---------------------------------------:|
|  T  |  T  |       T      |      T     |     F    |         T         |           T           |                    F                    |
|  T  |  F  |       F      |      T     |     F    |         F         |           F           |                    T                    |
|  F  |  T  |       F      |      T     |     T    |         T         |           F           |                    T                    |
|  F  |  F  |       F      |      F     |     T    |         T         |           T           |                    F                    |

*Exercise 18 (1/5):* Write up the truth table for $(p \Rightarrow q) \wedge (q \Rightarrow p)$.

*Exercise 19 (1/5):* Write up the truth table for $(\neg (p \vee q)) \Rightarrow r$.

> **Definition 19** *A **contradiction** is a proposition that is always false.*

As an example, the proposition $p \wedge (\neg p)$ is a contradiction, as can be seen from the truth table below.

| $p$ |$\neg p$|$p \wedge (\neg p)$|
|:---:|:------:|:-----------------:|
|  T  |   F    |         F         |
|  F  |   T    |         F         |

If we let $p$ be the proposition "it is raining", then $\neg p$ will be "it is not raining", and the proposition $p \wedge (\neg p)$ becomes "it is raining and it is not raining". Obviously, it cannot be raining and not raining at the same time, which makes this proposition always false and thereby a contradiction.

> **Definition 20** *A **tautology** is a proposition that is always true.*

We can use almost the same example as before. The proposition $p \vee (\neg p)$ is a tautology, as can be seen from the truth table below.

| $p$ |$\neg p$| $p \vee (\neg p)$ |
|:---:|:------:|:-----------------:|
|  T  |   F    |         T         |
|  F  |   T    |         T         |

Again, if we let $p$ be the proposition "it is raining", then $\neg p$ will be "it is not raining", and the proposition $p \vee (\neg p)$ becomes "it is raining or it is not raining". Obviously, it's either raining or not, which makes this proposition always true and thereby a tautology.

*Exercise 20 (1/5):* Show that $((p \wedge q) \Rightarrow r) \Leftrightarrow (p \Rightarrow (q \Rightarrow r))$ is a tautology.

*Exercise 21 (1/5):* Show that $\neg (((p \wedge q) \Rightarrow r) \Leftrightarrow (p \Rightarrow (q \Rightarrow r)))$ is a contradiction.

> **Definition 21** *Two propositions $p$ and $q$ are called **equivalent**, and we write $p \equiv q$, if and only if $p \Leftrightarrow q$ is a tautology.*

*Exercise 22 (1/5):* Show that $\neg (p \wedge q) \equiv \neg p \vee \neg q$ and $\neg (p \vee q) \equiv \neg p \wedge \neg q$ using truth tables, which are called the **De Morgan's laws**.

> **Definition 22** *The **contrapositive** of the conditional $p \Rightarrow q$ is $\neg q \Rightarrow \neg p$.*

*Exercise 23 (1/5):* Show that $p \Rightarrow q$ and $\neg q \Rightarrow \neg p$ are equivalent, i.e. $p \Rightarrow q \equiv \neg q \Rightarrow \neg p$.

*Exercise 24 (3/5):* Let $a,b,c \in \mathbb{Z}$. Use  De Morgan's laws and then contraposition to show that if $a \nmid bc$, then $a \nmid b$ and $a \nmid c$. We could also write this as $a \nmid bc \Rightarrow (a \nmid b) \wedge (a \nmid c)$. Note that $p \nmid q$ means $p$ does not divide $q$.

Note that we can also combine predicates with connectives, and we have two more operators to talk about when it comes to predicates.

> **Definition 23** *Let $p(x)$ be a predicate of the elements in a set $D$. We can create the proposition*
>
$$
\forall x \in D : p(x),
$$
>
*which is true, exactly when $p(x)$ is true for all elements $x$ in $D$. We say "for all (or any/each/every) $x$ in $D$ $p(x)$ (is true)". This is called the **universal quantifier**.*\\
*We can also create the proposition*
>
$$
\exists x \in D : p(x),
$$
>
*which is true, exactly when $p(x)$ is true for (at least) one element $x$ in $D$. We say "for some (or there exists a) $x$ in $D$ p(x) (is true)". This is called the **existential quantifier**.*

Let's do some examples of these to get them under our skin. The predicate $x^2 \geq 0$ is true no matter what real number we set $x$ to be. We can therefore say that the proposition $\forall x \in \mathbb{R} : x^2 \geq 0$ is true. Likewise, we can say the proposition $\exists x \in \mathbb{R} : x^2 < 1$ is true, since if $x=0$ then $x^2 = 0 < 1$. However, the proposition $\forall x \in \mathbb{R} : x^2 < 1$ is not true, for example if $x=5$ then $x^2 = 25 \nless 1$.

If we have a predicate with two free variables but we quantify one of them, for example $\forall x \in \mathbb{R} : x^2 > y$, then this is a predicate of the free variable $y$. The predicate is true for negative values of $y$ and false for nonnegative (positive and zero) values of $y$.\\
Also, we can use multiple quantifiers, where *the order matters* (in most cases). For example, the proposition

$$
\forall y \in \mathbb{R} \exists x \in \mathbb{R} : x^2 > y
$$

says that for all real numbers $y$ there exists a real number $x$ such that $x^2$ is larger than $y$. This is true. It doesn't matter what $y$ we choose, we can always find a real number such that when we square it, it's larger than $y$. However, if we switch the quantifiers, then the proposition

$$
\exists x \in \mathbb{R} \forall y \in \mathbb{R} : x^2 > y
$$

is false, since we cannot find a real number such that when we square it, it will be larger than all other real numbers.

> **Theorem 24** *Let $x$ be an element of some set $D$ and $p(x)$ a predicate of $x$. We then have the following rules:*
>
$$ \begin{aligned}
\neg (\forall x \in D : p(x)) &\equiv \exists x \in D : \neg p(x) \\
\neg (\exists x \in D : p(x)) &\equiv \forall x \in D : \neg p(x)
\end{aligned} $$



### Proofs


#### Induction (and recursion)


### Set theory


#### Relations

### Functions


### Counting

#### Combinatorics and permutations


### Graph theory



[^1]: Exercise 3 from the Georg Mohr competition (2002): [link](http://georgmohr.dk/gmopg/gm02pb.pdf){:target="_blank"}.
[^2]: Exercise 2 from the Georg Mohr competition (2008): [link](http://georgmohr.dk/gmopg/gm08pb.pdf){:target="_blank"}.
[^3]: Exercise 2 from the Georg Mohr competition (2004): [link](http://georgmohr.dk/gmopg/gm04pb.pdf){:target="_blank"}.
