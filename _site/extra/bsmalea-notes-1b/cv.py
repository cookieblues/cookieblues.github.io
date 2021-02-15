import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.constants import golden

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")


x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
t = np.array([1.15, 0.84, 0.39, 0.14, 0, 0.56, 1.16, 1.05, 1.45, 2.39, 1.86])


def kfold(n_points, n_splits=2):
    split_sizes = np.full(n_splits, n_points // n_splits)
    leftover = n_points % n_splits
    split_sizes[:leftover] += 1
    idx = np.arange(n_points)
    current = 0
    for split_size in split_sizes:
        val_idx = idx[current:current+split_size]
        train_idx = np.delete(idx, val_idx)
        yield train_idx, val_idx
        current += split_size

k = 3
N = 11
folds = kfold(N, k)
for fold in folds:
    print(fold)
