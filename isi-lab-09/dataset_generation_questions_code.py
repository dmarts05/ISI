from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import numpy as np


def vis_data_2D(X, y):
    for class_value in range(2):
        # get row indexes for samples with this class
        row_ix = np.where(y == class_value)
        # create scatter of these samples
        plt.scatter(X[row_ix, 0], X[row_ix, 1], s=10, label=class_value)
    plt.legend()
    plt.title("Data", fontsize=14)
    plt.show()
    return


if __name__ == "__main__":
    # Question 1
    X, y = make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[3, 3], [0, 0]],
        cluster_std=1,
        random_state=2,
    )
    vis_data_2D(X, y)

    # Question 2
    X, y = make_moons(n_samples=1000, noise=0.2, random_state=0)
    vis_data_2D(X, y)
