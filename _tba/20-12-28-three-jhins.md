---
date: 2020-12-28
title: "What was the probability that k3soju hit 2-star Jhin at round 3-2 (level 5)?"
categories:
  - Gaming
  - Teamfight Tactics
featured_image: https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jhin_0.jpg
---
I just watched k3soju get a 2-star Jhin at level 5. You can watch the vod [here](https://www.twitch.tv/videos/852660769). He gets to hit five shops before he has the 2-star Jhin. He sees the shops at 3:37:55, 3:39:00, 3:40:15, 3:41:04, and 3:42:18, where he hits a Jhin on the 2nd, 4th, and 5th shop. The chat immediately tried figuring out the probability, but as k3soju mentions, it's a bit complicated to figure out - and technically impossible without knowing everything that the 7 other players got as well. However, with a few reasonable assumptions, I think, we can come up with a decent estimate.

We'll make the following assumptions:
- No player rolled at level 5. We know this is true for k3soju (as is visible from the vod), but we cannot see the other players. However, it's fairly unlikely that anyone rolled at the beginning of level 5, even if you slowroll for a champion.
- If a player hits a 4-cost champion, they buy it. This is likely since a 4-cost champion is powerful at level 5.

In the carousel (round 2-4) at 3:37:10, we can see that every player is level 4, and when the carousel ends at 3:37:55, there are three players who automatically reach level 5 (k3soju, ttv theJirachy, and Wintrade account) and therefore see a level 5 shop. Four players (Uecker, xiao dian dian, Mismatched Socks, and Deadpool LAN) manually level to 5, but do not see a level 5 shop according to our assumption - it's also reasonable to think that these players just leveled to 5 in order to put another champion on their board, and get a level 5 shop next round. The last player, I Hated Jungle, manually levels to 5 in round 2-6.

k3soju hits the 3rd Jhin on round 3-2, which means that we can now figure out the total number of level 5 shops that is seen. Round 2-5 has 3 shops; round 2-6 has 7 shops; round 2-7, 3-1, and 3-2 have 8 shops. A total of $3+7+8 \times 3 = 34$ shops is therefore seen before the 2-star Jhin.

There are 11 unique 4-cost champions (Aatrox, Ahri, Ashe, Cassiopeia, Jhin, Morgana, Riven, Sejuani, Shen, Talon, and Warwick), and 12 copies of each in the pool<span class="sidenote-number"></span><span class="sidenote">[Patch 9.22 notes](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-9-22-notes/) and [patch 10.12 notes](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-12-notes/).</span>. Furthermore, each of the five slots in the shop has a 2% chance of containing a 4-cost champion at level 5<span class="sidenote-number"></span><span class="sidenote">[Patch 10.24 notes](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-24-notes/).</span>.

Let $X_i$ denote the event of seeing $i$ Jhins in a shop, and $Y_j$ denote the event of seeing $j$ 4-cost champions in a shop. We know that $0 \leq i,j \leq 5$, and if $i > j$ then $P(X_i \| Y_j) = 0$, since we cannot see more Jhins than there are 4-cost champion slots in the shop. We are interested in the marginal probability $P(X_i)$ given by

$$ \begin{aligned}
P(X_i)
&= \sum_{j=0}^5 P(X_i, Y_j) \\
&= \sum_{j=0}^5 P(X_i | Y_j) P(Y_j)
\end{aligned} $$

The probability of seeing $j$ 4-cost champions in a shop follows a Binomial distribution (until there are no more 4-cost champions in the pool), and therefore $P(Y_j) = {5\choose j} 0.02^j (1-0.02)^{5-j}$. Let's say that there $m$ Jhins left in the pool, and there are $n$ 4-cost champions left in the pool, then the probability of getting $i$ Jhins given that $j$ slots in shop will contain 4-cost champions is

$$
P(X_i | Y_j) = {i \choose j} \left( \prod_{s=0}^{i-1} \frac{m-s}{n-s} \right) \left( \prod_{t=0}^{j-i-1} \frac{n-(m-i)-t}{n-i-t} \right).
$$


The joint probability $P(X_i, Y_j) = P(X_i \| Y_j) P(Y_j)$.


As an example<span class="marginnote">This is done as an example, as it will help us later on, but this example is the same as calculating the probability of seeing no Jhins at all and subtracting the result from 1.</span>, let's calculate the probability of seeing one or more Jhins in a shop (given that the pool is full). We will split the calculation into parts; firstly, we'll calculate the probability of seeing 1, 2, 3, 4, or 5 4-cost champions, and then the probability that these contain at least one Jhin. Let $X_i$ denote the event of seeing $i$ Jhins in a shop, and $Y_j$ denote the event of seeing $j$ 4-cost champions in a shop. We are interested in finding the probability of $i$ Jhins given $j$ 4-cost champion slots in the shop, or more formally the conditional probability $P(X_i \| Y_j)$.

Obviously, $P(X_i \| Y_j) = 0$ if $i > j$, because we cannot see more Jhins in the shop than there are 4-cost champion slots. From Bayes' theorem we know

$$
P(X_i | Y_j) = \frac{P(Y_j | X_i) P(X_i)}{P(Y_j)}.
$$





To make it easier for us to calculate the probability, we'll split it up into parts. We start by calculating the probability given that no other player saw a Jhin (and therefore didn't buy it), then given that one other player saw a Jhin, then two Jhins, three Jhins, etc.




<span class="marginnote">It's important to note that k3soju didn't have a chosen champion, when he saw his first level 5 shop. However, according to [the patch 10.24 notes](https://teamfighttactics.leagueoflegends.com/en-us/news/game-updates/teamfight-tactics-patch-10-24-notes/), there's no chance of hitting a chosen 4-cost champion at level 5, so this does not increase his chance of a 2-star Jhin.</span>


