---
date: 2021-02-15
title: "The bare minimum guide to Matplotlib"
categories:
  - Guides
featured_image: https://upload.wikimedia.org/wikipedia/en/5/56/Matplotlib_logo.svg
---
If you want to work with arrays in Python, you use NumPy. If you want to work with tabular data, you use Pandas. The quintessential Python library for data visualization is Matplotlib. It's easy to use, flexible, and a lot of other visualization libraries build on the shoulders of Matplotlib. This means that learning Matplotlib will make it easier to understand and work with some of the more fancy visualization libraries.

### Getting started
You'll need to install the Matplotlib library. Assuming you have some terminal at your disposal and you have [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)){:target="_blank"} installed, you can install Matplotlib with the following commaned: `pip install matplotlib`. You can read more about the installation in Matplotlib's [installation guide](https://matplotlib.org/users/installing.html){:target="_blank"}.

### Two approaches
We'll begin by making a simple [scatter plot](https://en.wikipedia.org/wiki/Scatter_plot){:target="_blank"} in two different ways: the 'naive' way and the object-oriented way. Both approaches have their pros and cons. Generally, we can say that the object-oriented approach is best when you need multiple plots next to each other.<span class="marginnote">I almost always use the object-oriented approach though, even when I don't need to make multiple plots.</span>

#### 'Naive'
To start with we have to import matplotlib though. The `plt` framework is what we'll use for Python plotting.

{% highlight python %}
import matplotlib.pyplot as plt
import numpy as np
{% endhighlight %}

We also import numpy, so we can easily generate points to plot! Let's pick some points on the [sine function](https://en.wikipedia.org/wiki/Sine){:target="_blank"}. We choose some x-values and then calculate the y-values with `np.sin`.

{% highlight python %}
x = np.linspace(-3, 3, num=10)
y = np.sin(x)
{% endhighlight %}

Now that we've generated our points, we can make our scatter plot! We use the `scatter` function from the `plt` framework to make the plot, and we use `show` to visualize our plot.

{% highlight python %}
plt.scatter(x, y)
plt.show()
{% endhighlight %}

By running these $6$ lines, a window with the following plot should appear.

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/scatter_plot.svg">

If we don't want a scatter plot but a line plot, we can switch out `scatter` for `plot`.

{% highlight python %}
plt.plot(x, y)
plt.show()
{% endhighlight %}

This gives us the following plot.

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/jagged_line_plot.svg">

However, this line is very jagged. We can make it more smooth by generating more points.

{% highlight python %}
x = np.linspace(-3, 3, num=100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/smooth_line_plot.svg">


#### Object-oriented
Now that we know how to make and visualize a plot, let's look at the object-oriented way of producing the same plot. However, why would we want to know this? Simply because the object-oriented way is more powerful and allows for more complicated plots, as will be evident when we want to make multiple plots.

If we want to replicate the previous plot, we start by making a `Figure` object and an `Axes` object.<span class="marginnote">We assume, we have generated our data.</span>

{% highlight python %}
fig = plt.figure()
ax = fig.add_subplot()
{% endhighlight %}

We can think of the `Figure` object as the frame, we want to put plots into, and the `Axes` object is an actual plot in our frame. We then add the line plot to the `Axes` object and use `show` again to visualize the plot.

{% highlight python %}
ax.plot(x, y)

plt.show()
{% endhighlight %}

This generates the same plot as before.

### Line plots
Here are examples of [colours](https://matplotlib.org/3.1.0/gallery/color/named_colors.html){:target="_blank"} that we can use. We can specify colours in many different ways; hex code, RGB, plain old names.

{% highlight python %}
from scipy.stats import norm

x = np.linspace(-4, 4, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-1, scale=1), color="magenta")
ax.plot(x, norm.pdf(x, loc=0, scale=1), color=(0.85, 0.64, 0.12))
ax.plot(x, norm.pdf(x, loc=1, scale=1), color="#228B22")

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/colours.svg">

There are also many predefined [linestyles](https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html){:target="_blank"} that we can use. Note that without defining colours, Matplotlib will automatically choose some distinct default colors for our lines.

{% highlight python %}
x = np.linspace(-6, 6, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-3, scale=1), linestyle="solid")
ax.plot(x, norm.pdf(x, loc=-1, scale=1), linestyle="dotted")
ax.plot(x, norm.pdf(x, loc=1, scale=1), linestyle="dashed")
ax.plot(x, norm.pdf(x, loc=3, scale=1), linestyle="dashdot")

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/linestyles.svg">

We can also adjust the width of our lines!

{% highlight python %}
x = np.linspace(-2, 9, num=100)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

for i in range(1,7):
    ax.plot(x, norm.pdf(x, loc=i, scale=1), color="black", linewidth=i/2)

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/linewidths.svg">

### Scatter plots
For scatter plots, we can change the [markers](https://matplotlib.org/3.3.3/api/markers_api.html){:target="_blank"} and their size. Here's an example

{% highlight python %}
x = np.linspace(-4, 4, num=20)
y1 = x
y2 = -y1
y3 = y1**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.scatter(x=x, y=y1, marker="v", s=1)
ax.scatter(x=x, y=y2, marker="X", s=5)
ax.scatter(x=x, y=y3, marker="s", s=10)

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/markers.svg">

We can also combine line and scatter plots using the [`ax.plot`](https://matplotlib.org/3.3.4/api/_as_gen/matplotlib.pyplot.plot.html){:target="_blank"} function by changing the `fmt` parameter. The `fmt` parameter consists of a part for marker, line, and color: `fmt = [marker][line][color]`. If `fmt = "s--m"`, then we have square markers, a dashed line, and they'll be coloured magenta.

{% highlight python %}
x = np.linspace(-2, 2, num=20)
y = x ** 3 - x

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y, 'H-g')

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/linescatter.svg">

### Histograms
We can make histograms easily using the `ax.hist` function.

{% highlight python %}
x = np.random.randn(10000)

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.hist(x)

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/hist.svg">

We can change a lot of things in the histogram to make it nicer - we can even add multiple!

{% highlight python %}
x1 = np.random.randn(10000)-1
x2 = np.random.randn(10000)+1

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.hist(x1, color='turquoise', edgecolor='none', bins=50, alpha=0.5, density=True)
ax.hist(x2, color='magenta', edgecolor='none', bins=200, alpha=0.5, density=True)

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/hists.svg">

### Legends
Naturally, we'll want to add a legend to our plot. This is simply done with the [`ax.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html){:target="_blank"} function.

{% highlight python %}
x = np.linspace(-2, 2, num=100)
y1 = x
y2 = x**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y1, color='turquoise', label='First')
ax.plot(x, y2, color='magenta', label='Second')

ax.legend()

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/legend.svg">

Matplotlib will automatically try and find the best position for the legend on your plot, but we can change it by providing an argument for the `loc` parameter. Also, a common preference is to not have a frame around the legend, and we can disable it by setting the `frameon` parameter to `False`. Additionally, Matplotlib lists the elements of the legend in one column, but we can provide the number of columns to use in the `ncol` parameter.

{% highlight python %}
x = np.linspace(-2, 2, num=100)
y1 = x
y2 = np.sin(x)+np.cos(x)
y3 = x**2

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

ax.plot(x, y1, color='turquoise', label='First')
ax.plot(x, y2, color='magenta', label='Second')
ax.plot(x, y3, color='forestgreen', label='Third')

ax.legend(loc='lower center', frameon=False, ncol=3)

plt.show()
{% endhighlight %}

<img src="{{ site.baseurl }}/extra/matplotlib-bare-minimum/more_legend.svg">

### Final tips
There are so many quirks and different things you can do with Matplotlib, and unfortunately I cannot provide them all here. However, a few guidelines to get you started:
1. You save figures with the `plt.savefig()` function.
2. There are a bunch of libraries that build on the shoulders of Matplotlib that could be beneficial to the specific plot you're trying to create, e.g. [Seaborn](https://seaborn.pydata.org/), [Bokeh](https://docs.bokeh.org/en/latest/), [Plotly](https://plotly.com/), and many more.
3. Look at the [gallery](https://matplotlib.org/stable/gallery/index.html). Please, please, look at the [gallery](https://matplotlib.org/stable/gallery/index.html)! Don't waste 3 hours working on a plot, if someone has already made it. 
