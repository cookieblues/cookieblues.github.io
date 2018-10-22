---
title: A Look at Linear Algebra and Optimisation
layout: post
tags: LinAlgOp
---
Over the next month or two I'll try and post notes for the course "Linear Algebra and Optimisation" at the IT University of Copenhagen. While I didn't take the course myself, because I got merit from another linear algebra course, I did help a few of my classmates when they were taking it, and I'm also currently TAing the course for the new students.

### Motivation
While I've taught linear algebra before, and it probably won't be the last time, having online notes to reference will likely buy me time in the future. Except for this, my motivation is threefold:

1) The data science programme is mathematically heavy with network analysis, algorithms and data structures, and machine learning as courses on the menu. As such, a solid mathematical foundation is required. Most, if not all, other mathematically inclined programmes in Denmark have an introductory math course: mathematics and physics at KU have introduction to mathematics[^1][^2], computer science at KU has discrete mathematics[^3], and engineer students at DTU have to take an extensive introductory mathematics course[^4]. Ordinary concepts introduced by these courses include complex numbers, sequences and series, simple differential equations, Taylor's theorem, etc., which are not necessarily important concepts to grasp as a data scientist.\\
Yet, these courses also serve the purpose of introducing students to rigour in mathematics, as well as refresh some elementary mathematics that the students might not have seen for years. The approach of LinAlgOp (as I will refer to it from now on) is to skip the previously mentioned lesser important concepts, and instead attempt to bunch together linear algebra and real analysis into one ambitious introductory mathematics course. The idea is intriguing, but in my opinion unrealistic with the way it's structured now.

2) The entire programme is chaotic due to its recent kickoff last year. I started at kickoff last year, and now a year later we've lost half of the students who started. While there could be a multitude of reasons for this, I suspect LinAlgOp and statistics. It's evident from the distribution of the grades (that I will not reveal) of those two courses that something isn't right. Two quite extensive mathematics courses on the first year with no introduction to mathematics takes its toll. So, because of the high level of difficulty, and the intrinsic chaos present on a new programme, I feel that it's only reasonable to help one another - especially considering the importance of linear algebra in data science.

3) Linear algebra is intuitive and applicable; however, it's often taught with long, convoluted, and dull calculations without any insight in its practicality. When it comes to data science, I think learning-by-doing has merit to it. Yet, I also believe application often follows from intuition. Having an innate grasp of a concept makes it easier to discover and utilize it in different contexts. While LinAlgOp does a great job of inserting applications into the syllabus (the method of least squares with projection, diagonalisation, and even the PageRank algorithm), it unfortunately lacks much "intuition teaching". My hope is that I can provide at least some intuition.

As of writing this, the course has run twice, and the latest version can be found [here](https://mit.itu.dk/ucs/cb_www/course.sml?course_id=2013608&mode=search&lang=da&print_friendly_p=t&goto=1540218458.000){:target="_blank"}. 


[^1]: https://studier.ku.dk/bachelor/matematik/undervisning-og-opbygning/matematik/
[^2]: https://studier.ku.dk/bachelor/fysiske-fag/undervisning-og-opbygning/
[^3]: https://studier.ku.dk/bachelor/datalogi/undervisning-og-opbygning/
[^4]: https://www.dtu.dk/Uddannelse/Bachelor#uddannelsens-opbygning
