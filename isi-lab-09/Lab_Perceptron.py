# -*- coding: utf-8 -*-
"""
@author: Lab ULE
"""

# import the necessary packages
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np


def vis_classification_2D(X, y, clf):
    # Define the minimum and maximum values for X
    min1, max1 = X[:, 0].min() - 1, X[:, 0].max() + 1
    min2, max2 = X[:, 1].min() - 1, X[:, 1].max() + 1
    # Define the x1 and x2 limits
    x1grid = np.arange(min1, max1, 0.01)
    x2grid = np.arange(min2, max2, 0.01)
    # Create the meshgrid: all of the lines and rows of the grid
    xx1, xx2 = np.meshgrid(x1grid, x2grid)
    # Flatten each grid to a vector and create the matrix "grid"
    r1, r2 = xx1.flatten(), xx2.flatten()
    r1, r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))
    grid = np.hstack((r1, r2))

    y_assig = clf.predict(grid)
    # Reshape the predictions back into a grid
    zz = y_assig.reshape(xx1.shape)

    # Create a plot
    plt.figure()
    # Plot the grid of xx1, xx2 and z values
    plt.contourf(xx1, xx2, zz, cmap="Blues")

    for class_value in range(2):
        # get row indexes for samples with this class
        row_ix = np.where(y == class_value)
        # create scatter of these samples
        plt.scatter(X[row_ix, 0], X[row_ix, 1], s=10, label=class_value)
    plt.legend()
    plt.show()
    return


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


#
# -------------
# MAIN PROGRAM
# -------------

# Create the dataset with 3000 samples, 2 features
# Use two centers. One of the centers  at [4,-5] and the other at [0,3].
# Fix the standard deviation for the gaussian data with value 3
# ====================== YOUR CODE HERE ======================
# X, y = make_blobs(
#     n_samples=3000,
#     n_features=2,
#     centers=[[4, -5], [0, 3]],
#     cluster_std=3,
#     random_state=1,
# )

# Moon dataset
X, y = make_moons(n_samples=3000, noise=0.3, random_state=1)
# ============================================================


# Plot the binary dataset
vis_data_2D(X, y)


# Split train-test data
# Use 30% of the data for test and make the split stratified according to the class
# ====================== YOUR CODE HERE ======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=1
)
# ============================================================


# Create the classification model: Perceptron
# with maximum number of iterations of 1000, learning rate 1 and tolerance 1e-4
# ====================== YOUR CODE HERE ======================
clf = Perceptron(max_iter=1000, tol=1e-4, random_state=1, eta0=1, verbose=1)
# ============================================================


# Train the Perceptron
# ====================== YOUR CODE HERE ======================
clf.fit(X_train, y_train)
# ============================================================


# Evaluate the Perceptron
# ====================== YOUR CODE HERE ======================
print("=======================")
print("Train Accuracy:", clf.score(X_train, y_train))
print("Test Accuracy:", clf.score(X_test, y_test))
print("=======================")
# ============================================================


# Visualize the classification boundary and the test data
vis_classification_2D(X_test, y_test, clf)


# Compute the outputs of the classifier for the test data X_test
# ====================== YOUR CODE HERE ======================
y_test_assig = clf.predict(X_test)
# ============================================================


# Compute the output of the classifier for an example with features [0, 15]
# ====================== YOUR CODE HERE ======================
y_i_assig = clf.predict([[0, 15]])
# ============================================================


# Perceptron weights  after training
# ====================== YOUR CODE HERE ======================
print("weights of TRAINED Perceptron (w1 and w2): {}".format(clf.coef_))
# Model bias term
print("Bias term of the TRAINED perceptron (w0) {}".format(clf.intercept_))
# ====================== YOUR CODE HERE ======================
