---
title: "A look at Linear Algebra and Optimisation"
layout: post
tags: BSLIALO
---
Over the next month or two I'll try and post notes for the course "[Linear Algebra and Optimisation](https://mit.itu.dk/ucs/cb_www/course.sml?course_id=2013608&mode=search&lang=da&print_friendly_p=t&goto=1540218458.000){:target="_blank"}" at the [IT University of Copenhagen](https://www.itu.dk/){:target="_blank"}. I'll attempt to write the notes as to give an intuitive understanding of the introduced concepts. Therefore the notes will **not** contain rigorous proofs and explanations of every little theorem, you might run into in a linear algebra course.\\
While I didn't take the course myself, because I got merit from another linear algebra course, I did help a few of my classmates when they were taking it, and I'm also currently TAing the course.

### Overview
The course is 14 weeks, tightly packed, and assumes you are familiar with basic vector calculation. It's split up in a linear algebra part and a calculus part, each taking up about half of the course with the linear algebra part taking up the first half. Since the course is underway in the 8th week as of writing this, which is the last week of linear algebra, I will start the notes from the 9th week to accomodate the students taking the course. On top of that, I'll split the first notes into three parts considering the amount of material that has to be plown through.

1. Vectors, linear combinations, and span
2. Systems of linear equations
3. Linear transformations and matrices
4. Determinants
5. Vector spaces, subspaces, basis
6. Method of least squares with projection matrices
7. Eigenvectors, eigenvalues, and diagonalisation
8. PageRank algorithm
9. Introduction to calculus:\\
   (a) <a href="{{ site.url }}/pages/bslialo-notes-9a">The derivative, the limit, and the concept of approach</a>\\
   (b) <a href="{{ site.url }}/pages/bslialo-notes-9b">The chain rule, derivatives of logarithmic functions, extrema, and optimisation</a>\\
   (c) <a href="{{ site.url }}/pages/bslialo-notes-9c">Integration and the fundamental theorem of calculus</a>
10. <a href="{{ site.url }}/pages/bslialo-notes-10">Taylor polynomials and Newton-Raphson's method</a>
11. Motion along a curve
12. Partial derivatives and gradients
13. Optimisation, 2nd derivative test, and Lagrange multipliers
14. Multiple integrals

### Motivation
While I've taught linear algebra before, and it probably won't be the last time, having online notes to reference will likely buy me time in the future. Except for this, my motivation is threefold:

1) The data science programme is mathematically heavy with network analysis, algorithms and data structures, and machine learning as courses on the menu. As such, a solid mathematical foundation is required. Most, if not all, other mathematically inclined programmes in Denmark have an introductory math course: mathematics and physics at KU have introduction to mathematics[^1][^2], computer science at KU has discrete mathematics[^3], and engineer students at DTU have to take an extensive introductory mathematics course[^4]. Ordinary concepts introduced by these courses include complex numbers, sequences and series, simple differential equations, Taylor's theorem, etc., which are not necessarily essential concepts to grasp as a data scientist.\\
Yet, these courses also serve the purpose of introducing students to rigour and argument in mathematics, as well as refresh some elementary mathematics that the students might not have been exposed to for years. The approach of BSLIALO (as I will refer to it from now on) is to skip the previously mentioned less essential concepts, and instead attempt to bunch together linear algebra and real analysis into one ambitious introductory mathematics course. The idea is intriguing. However, based on other programmes it seems unrealistic, with the way it is structured now.

2) The entire programme is chaotic due to its recent kickoff last year. I started at kickoff last year, and now a year later we've lost half of the students who started. While there could be a multitude of reasons for this, I suspect BSLIALO and statistics. It's evident from the distribution of the grades (that I will not reveal) of those two courses that something isn't right. Two quite extensive mathematics courses in the first year without an introduction to mathematics takes its toll. So, because of the high level of difficulty, and the intrinsic chaos present on a new programme, I feel that it's only reasonable to help one another - especially considering the importance of linear algebra in data science.

3) Linear algebra is intuitive and applicable. Yet, it's often taught with long, convoluted, and dull calculations without insight in its practicality. When it comes to data science, I think learning-by-doing has merit to it. However, I also believe application often follows from intuition; having an innate grasp of a concept makes it easier to discover and thereby utilize it in different contexts. While BSLIALO does a great job of inserting applications into the syllabus (the method of least squares with projection, diagonalisation, and the PageRank algorithm), it unfortunately lacks much 'intuition teaching'. My hope is that I can provide at least some intuition.

As of writing this, the course has run twice, and the latest version can be found [here](https://mit.itu.dk/ucs/cb_www/course.sml?course_id=2013608&mode=search&lang=da&print_friendly_p=t&goto=1540218458.000){:target="_blank"}. 


[^1]: https://studier.ku.dk/bachelor/matematik/undervisning-og-opbygning/matematik/
[^2]: https://studier.ku.dk/bachelor/fysiske-fag/undervisning-og-opbygning/
[^3]: https://studier.ku.dk/bachelor/datalogi/undervisning-og-opbygning/
[^4]: https://www.dtu.dk/Uddannelse/Bachelor#uddannelsens-opbygning
