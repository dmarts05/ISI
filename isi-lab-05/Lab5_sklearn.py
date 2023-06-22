#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:12:41 2022
Modified on Mon Mar 13 2023

@author: dmarts05

This script carries out a classification experiment of the spambase dataset by
means of the kNN classifier, USING THE SCIKIT-LEARN PACKAGE
"""

# Import whatever else you need to import
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    recall_score,
)


# %%
# -------------
# MAIN PROGRAM
# -------------
if __name__ == "__main__":
    # %% PART 1: LOAD DATASET AND TRAIN-TEST PARTITION

    # Load csv with data into a pandas dataframe
    """
    Each row in this dataframe contains a feature vector, which represents an
    email.
    Each column represents a variable, EXCEPT LAST COLUMN, which represents
    the true class of the corresponding element (i.e. row): 1 means "spam",
    and 0 means "not spam"
    """
    dir_data = "Data"
    spam_df = pd.read_csv(os.path.join(dir_data, "spambase_data.csv"))
    y_df = spam_df[["Class"]].copy()
    X_df = spam_df.copy()
    X_df = X_df.drop("Class", axis=1)

    # Convert dataframe to numpy array
    X = X_df.to_numpy()
    y = y_df.to_numpy()

    """
    Parameter that indicates the proportion of elements that the test set will
    have
    """
    proportion_test = 0.3

    """
    Partition of the dataset into training and test sets is done. 
    Use the function train_test_split from scikit_learn
    """
    # ====================== YOUR CODE HERE ======================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.ravel(), test_size=proportion_test
    )
    # ============================================================

    """
    Create an instance of the kNN classifier using scikit-learn
    """
    # ====================== YOUR CODE HERE ======================
    k = 3
    knn = KNeighborsClassifier(n_neighbors=k)
    # ============================================================

    """
    Train the classifier
    """
    # ====================== YOUR CODE HERE ======================
    knn.fit(X_train, y_train)
    # ============================================================

    """
    Get the predictions for the test set samples given by the classifier
    """
    # ====================== YOUR CODE HERE ======================
    y_test_assig = knn.predict(X_test)
    # ============================================================

    """
    Show the confusion matrix. Use the same methods that were used in the
    first part of the lab (i.e., see Lab5.py)
    """
    # ====================== YOUR CODE HERE ======================
    confusion_matrix_kNN = confusion_matrix(y_true=y_test, y_pred=y_test_assig)

    disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_kNN)
    disp.plot()
    plt.title("Confusion Matrix", fontsize=14)
    plt.show()

    accuracy = accuracy_score(y_true=y_test, y_pred=y_test_assig)
    print("Accuracy: {:.4f}".format(accuracy))

    sensitivity = recall_score(y_true=y_test, y_pred=y_test_assig)
    print("Sensitivity (TPR): {:.4f}".format(sensitivity))

    specificity = confusion_matrix_kNN[0, 0] / confusion_matrix_kNN[0, :].sum()
    print("Specificity (TNR): {:.4f}".format(specificity))
    # ============================================================
