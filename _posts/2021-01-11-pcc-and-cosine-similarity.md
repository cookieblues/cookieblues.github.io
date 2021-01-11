---
date: 2021-01-11
title: "Pearson Correlation Coefficient and Cosine Similarity in Word Embeddings"
categories:
  - Machine Learning
  - Natural Language Processing
featured_image: https://developers.google.com/machine-learning/crash-course/images/linear-relationships.svg
---
A friend of mine recently asked me about word embeddings and similarity. I remember, I learned that the typical way of calculating the similarity between a pair of word embeddings is to take the cosine of the angle between their vectors. This measure of similarity makes sense due to the way that these word embeddings are commonly constructed, where each dimension is supposed to represent some sort of semantic meaning<span class="marginnote">These word embedding techniques have obvious flaws, such as words that are spelled the same way but have different meanings (called [homographs](https://en.wikipedia.org/wiki/Homograph)), or sarcasm which often times is saying one thing but meaning the opposite.</span>. Yet, my friend asked if you could calculate the correlation between word embeddings as an alternative to cosine similarity, and it turns out that it's almost the exact same thing.

[Zhelezniak et al. (2019)](https://www.aclweb.org/anthology/N19-1100/) explains this well. Given a vocabulary of $N$ words $\mathcal{V} = \\{ w_1, \dots, w_N \\}$ with a corresponding word embedding matrix $\mathbf{W} \in \mathbb{R}^{N \times D}$, each row in $\mathbf{W}$ corresponds to a word. Considering a pair of these, we can calcuate their [Pearson correlation coefficient (PCC)](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#For_a_sample). Let $(\mathbf{x}, \mathbf{y}) = \\{ (x_1, y_1), \dots, (x_D, y_D) \\}$ denote this pair, and we can compute the PCC as

$$
r_{xy} = \frac{ \sum_{i=1}^D (x_i - \bar{x})(y_i - \bar{y}) }{ \sqrt{\sum_{i=1}^D (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^D (y_i - \bar{y})^2} }, \quad \quad (1)
$$

where $\bar{x} = \frac{1}{D} \sum_{i=1}^D x_i$ is the sample mean; and analogously for $\bar{y}$.

The [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) between vectors $\mathbf{x}, \mathbf{y}$ is

$$ \begin{aligned}
\cos \theta
&= \frac{\mathbf{x} \cdot \mathbf{y}}{\| \mathbf{x} \| \| \mathbf{y} \|} \\
&= \frac{\sum_{i=1}^D x_i y_i}{\sqrt{\sum_{i=1}^D x_i^2} \sqrt{\sum_{i=1}^D y_i^2}} \quad \quad (2),
\end{aligned} $$

where we see that equation $(1)$ and $(2)$ are the same, if the sample means are 0. The question then becomes: is the mean of word vectors (across the $D$ dimensions) 0?

[GloVe](https://nlp.stanford.edu/projects/glove/) is a popular algorithm for constructing word embeddings, and their pre-trained word embeddings are also commonly used. Let's download the pre-trained word embeddings, and see if the mean of their vectors equal 0.

<span class="marginnote">The GloVe embeddings take up a little more than 800 MB. Depending on your connection, this might take a few minutes to download.</span>
{% highlight python linenos %}
from urllib.request import urlretrieve
from zipfile import ZipFile


GLOVE_URL = 'http://nlp.stanford.edu/data/glove.6B.zip'
GLOVE_FILENAME = 'raw_data.zip'

urlretrieve(GLOVE_URL, GLOVE_FILENAME)

with ZipFile(GLOVE_FILENAME) as zipfile:
    zipfile.extractall('data')
{% endhighlight %}

This piece of code will give us a folder called `data` with 4 different GloVe embedding files of varying vector dimensionalities (50, 100, 200, and 300). I will use the file with dimensionality 300. We can now load the words and their corresponding vectors and calculate the mean of each vector.

{% highlight python linenos %}
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


DIM = 300
words = list()
word_matrix = np.zeros((400_000, 300)) # vocab is 400k

with open(f'data/glove.6B.{DIM}d.txt', encoding='utf-8') as f:
    pbar = tqdm(total=400_000) 
    for idx, line in enumerate(f):
        line = line.split()
        words.append(line[0])
        word_matrix[idx] = np.array(line[1:], dtype=np.float32)
        pbar.update(1)
    pbar.close()

means = word_matrix.mean(axis=1)
{% endhighlight %}

Plotting these means in a histogram will give us insight into the distribution.

<span class="marginnote">Distribution of means of GloVe word vectors from `glove.6B.300d.txt`.</span>
<figure>
    <img src="{{ site.baseurl }}/extra/pcc-and-cosine-similarity/means_hist.svg">
</figure>

As we can see, the means fall closely to 0, which means the PCC and the cosine similarity will be roughly the same when used to calculate similarity between pairs of word embeddings.
