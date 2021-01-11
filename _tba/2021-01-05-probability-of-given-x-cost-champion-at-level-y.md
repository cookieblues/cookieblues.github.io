---
date: 2021-01-05
title: "What's the expected number of rolls needed to find a given $x$-cost champion at level $y$?"
categories:
  - Gaming
  - Teamfight Tactics
featured_image: https://images.contentstack.io/v3/assets/blt76b5e73bfd1451ea/blt5aa79e7028e4be73/5f5bca73806bc7495596e1ba/TFT_Fates_Homepage_Set_Module_Image.jpg
---
Sometimes I find myself needing a specific 4-cost champion at level 8, and I wonder if it's worth rolling down to find it. Yet, it depends on how much gold I need to spend on rolling. If it's just 10 gold, then I'll probably be inclined to do it no matter what, but if it's 40 gold, then I might be more hesitant and dependent on other factors, e.g. health or opponents' board.

The probability of getting a specific $x$-cost champion obviously depends on how contested it is, and how many other $x$-cost champions have been bought. The more contested a champion is, the lower the probability will be, and the more contested all other $x$-cost champions are, the higher the probability will be. Therefore, we'll make the assumption that no champions have been bought from the pool. This is obviously an unrealistic situation, but the probabilities will be good estimates.

So, how do we calculate this?

Firstly, we need to know how the game works. Each shop has 5 slots, and each slot has a specific distribution of returning an $x$-cost champion. The distribution for each level is shown in the table below<span class="sidenote-number"></span>
<span class="sidenote">
These can be gathered ingame or from patch notes: [10.9](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-9-notes/), [10.12](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-12-notes/), [10.24](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-24-notes/), and [10.25](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-25-notes/).
</span>.

|         | 1-cost | 2-cost | 3-cost | 4-cost | 5-cost |
|:--------|-------:|-------:|-------:|-------:|-------:|
| Level 1 |  100%  |   0%   |   0%   |   0%   |   0%   |
| Level 2 |  100%  |   0%   |   0%   |   0%   |   0%   |
| Level 3 |   75%  |  25%   |   0%   |   0%   |   0%   |
| Level 4 |   55%  |  30%   |  15%   |   0%   |   0%   |
| Level 5 |   45%  |  33%   |  20%   |   2%   |   0%   |
| Level 6 |   35%  |  35%   |  25%   |   5%   |   0%   |
| Level 7 |   22%  |  35%   |  30%   |  12%   |   1%   |
| Level 8 |   15%  |  25%   |  35%   |  20%   |   5%   |
| Level 9 |   10%  |  15%   |  30%   |  30%   |  15%   |

Secondly, after the slot has rolled for the cost of the champion, it rolls from the pool of champions with that cost. There are 29 copies of each unique 1-cost champion, 22 copies of 2-cost champions, 18 copies of 3-cost champions, 12 copies of 4-cost champions, and 10 copies of 5-cost champions<span class="sidenote-number"></span><span class="sidenote">[Patch 9.22 notes](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-9-22-notes/) and [patch 10.12 notes](https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-10-12-notes/).</span>. Furthermore, we have to know the amount of unique champions for each cost. You can count these up yourself, but there are 13 unique 1-, 2-, and 3-cost champions, 11 unique 4-cost champions, and 8 unique 5-cost champions.


