---
title: "The bare minimum guide to Matplotlib"
layout: post
tags: bare_min_guide
excerpt_separator: <!--more-->
---
TBA.
<!--
Short introduction with a bit of history.
-->

### Why?
Python is easy. Data science requires it. You can make beautiful plots like this.
<!--
I study data science, and it's important for me.
-->

### Getting started
You'll need to install the Matplotlib library. Assuming you have some terminal at your disposal and you have [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)){:target="_blank"} installed, you can install Matplotlib with the following commaned: `pip install matplotlib`. You can read more about the installation in Matplotlib's [installation guide](https://matplotlib.org/users/installing.html){:target="_blank"}.

### Beginnings
We're going to begin by making a very simple [scatter plot](https://en.wikipedia.org/wiki/Scatter_plot){:target="_blank"} in two different ways: the 'naive' way and the object-oriented way.

#### 'Naive' approach
To start with we have to import matplotlib though. The `plt` framework is what we'll use for Python plotting.

{% highlight python %}
import matplotlib.pyplot as plt
import numpy as np
{% endhighlight %}

We also import numpy, so we can easily generate points to plot! Let's pick some points on the [sine function](https://en.wikipedia.org/wiki/Sine){:target="_blank"}. We choose some x-values and then calculate the y-values with `np.sin`.

{% highlight python %}
x = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])
y = np.sin(x)
{% endhighlight %}

Now that we've generated our points, we can make our scatter plot! We use the `scatter` function from the `plt` framework to make the plot, and we use `show` to visualize our plot.

{% highlight python %}
plt.scatter(x, y)
plt.show()
{% endhighlight %}

By running these $6$ lines, a window with the following plot should appear.

<img src="{{ site.url }}/pages/extra/matplotlib-bare-minimum/scatter_plot.svg">

If we don't want a scatter plot but a line plot, we can switch out `scatter` for `plot`.

{% highlight python %}
plt.plot(x, y)
plt.show()
{% endhighlight %}

This gives us the following plot.

<img src="{{ site.url }}/pages/extra/matplotlib-bare-minimum/jagged_line_plot.svg">

However, this line is very jagged. We can make it more smooth by generating more points.

{% highlight python %}
x = np.linspace(-3, 3, num=100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
{% endhighlight %}

<img src="{{ site.url }}/pages/extra/matplotlib-bare-minimum/smooth_line_plot.svg">


#### Object-oriented approach
Now that we know how to make and visualize a plot, let's look at the object-oriented way of producing the same plot. However, why would we want to know this? Simply because the object-oriented way is more powerful and allows for more complicated plots, as will be evident when we want to make multiple plots.

If we want to replicate the previous plot, we start by making a `Figure` object and an `Axes` object (we assume, we have generated our data).

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

fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-1, scale=1), color="magenta")
ax.plot(x, norm.pdf(x, loc=0, scale=1), color=(0.85, 0.64, 0.12))
ax.plot(x, norm.pdf(x, loc=1, scale=1), color="#228B22")

plt.show()
{% endhighlight %}

<img src="{{ site.url }}/pages/extra/matplotlib-bare-minimum/colours.svg">

There are also many predefined [linestyles](https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html){:target="_blank"} that we can use. Note that without defining colours, Matplotlib will automatically choose some distinct default colors for our lines.

{% highlight python %}
x = np.linspace(-6, 6, num=100)

fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()

ax.plot(x, norm.pdf(x, loc=-3, scale=1), linestyle="solid")
ax.plot(x, norm.pdf(x, loc=-1, scale=1), linestyle="dotted")
ax.plot(x, norm.pdf(x, loc=1, scale=1), linestyle="dashed")
ax.plot(x, norm.pdf(x, loc=3, scale=1), linestyle="dashdot")

plt.show()
{% endhighlight %}

<img src="{{ site.url }}/pages/extra/matplotlib-bare-minimum/linestyles.svg">

We can also adjust the width of our lines!

{% highlight python %}
x = np.linspace(-2, 9, num=100)

fig = plt.figure(figsize=(6,6/golden))
ax = fig.add_subplot()

for i in range(1,7):
    ax.plot(x, norm.pdf(x, loc=i, scale=1), color="black", linewidth=i/2)

plt.show()
{% endhighlight %}

<img src="{{ site.url }}/pages/extra/matplotlib-bare-minimum/linewidths.svg">

### Scatter plots


