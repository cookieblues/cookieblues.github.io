---
date: 2021-02-15
title: "The bare minimum guide to Matplotlib"
categories:
  - Guides
featured_image: https://upload.wikimedia.org/wikipedia/en/5/56/Matplotlib_logo.svg
---

https://en.wikipedia.org/wiki/Pie_chart
https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart

import numpy as np
impo
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def rectangle_histogram(n_train, n_val, n_test, n_squares, ax, sidelength=1, **kwargs):
    sqrt_n_squares = np.ceil(np.sqrt(n_squares))
    start_x = 0
    start_y = sqrt_n_squares * sidelength
    actual_sidelength = sidelength * 0.9

    train_rects = list()
    for i in range(n_train):
        cur_x = start_x + (i % sqrt_n_squares)
        cur_y = start_y - (i // sqrt_n_squares)
        rect = plot_rectangle(
            cur_x, cur_y, width=actual_sidelength, height=actual_sidelength
        )
        train_rects.append(rect)
    train_patch = PatchCollection(
        train_rects, facecolor="darkturquoise", alpha=0.375, edgecolor="none"
    )
    ax.add_collection(train_patch)

    val_rects = list()
    for i in range(n_train, n_train + n_val):
        cur_x = start_x + (i % sqrt_n_squares)
        cur_y = start_y - (i // sqrt_n_squares)
        rect = plot_rectangle(
            cur_x, cur_y, width=actual_sidelength, height=actual_sidelength
        )
        val_rects.append(rect)
    val_patch = PatchCollection(
        val_rects, facecolor="indigo", alpha=0.375, edgecolor="none"
    )
    ax.add_collection(val_patch)

    test_rects = list()
    for i in range(n_train + n_val, n_train + n_val + n_test):
        cur_x = start_x + (i % sqrt_n_squares)
        cur_y = start_y - (i // sqrt_n_squares)
        rect = plot_rectangle(
            cur_x, cur_y, width=actual_sidelength, height=actual_sidelength
        )
        test_rects.append(rect)
    test_patch = PatchCollection(
        test_rects, facecolor="magenta", alpha=0.375, edgecolor="none"
    )
    ax.add_collection(test_patch)


def plot_rectangle(x, y, width, height, **kwargs):
    return Rectangle((x, y), width=width, height=height, **kwargs)