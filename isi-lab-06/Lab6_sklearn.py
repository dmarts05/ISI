#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:24:10 2023

@author: dmarts05
"""

import h5py
import os
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score

# -------------
# MAIN PROGRAM
# -------------
if __name__ == "__main__":

    np.random.seed(323)
    plt.close("all")

    dir_data = "Data"
    data_path = os.path.join(dir_data, "mammographic_data.h5")
    test_size = 0.3
    decision_threshold = 0.5

    # -------------
    # PRELIMINARY: LOAD DATASET AND PARTITION TRAIN-TEST SETS (NO NEED TO
    # CHANGE ANYTHING)
    # -------------

    # import features and labels
    h5f_data = h5py.File(data_path, "r")

    features_ds = h5f_data["data"]
    labels_ds = h5f_data["labels"]

    X = np.array(features_ds)
    y = np.array(labels_ds)

    h5f_data.close()

    # SPLIT DATA INTO TRAINING AND TEST SETS
    # ====================== YOUR CODE HERE ======================
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    # ============================================================

    # STANDARDIZE DATA
    scaler = preprocessing.StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # -------------
    # CLASSIFICATION WITH SCIKIT-LEARN'S LOGISTIC REGRESSION
    # -------------
    # Create an instance of the logistic regression classifier
    # ====================== YOUR CODE HERE ======================
    logreg = LogisticRegression()
    # ============================================================

    # Train the classifier
    # ====================== YOUR CODE HERE ======================
    logreg.fit(X_train, y_train)
    # ============================================================

    # Predict the classes of the test set samples using the trained classifier
    # ====================== YOUR CODE HERE ======================
    y_test_assig_skl = logreg.predict(X_test)
    # ============================================================

    # Display confusion matrix
    confm_skl = confusion_matrix(y_true=y_test, y_pred=y_test_assig_skl)
    disp = ConfusionMatrixDisplay(confusion_matrix=confm_skl)
    disp.plot()
    plt.title("Confusion Matrix for the scikit-learn classifier", fontsize=14)
    plt.show()

    # -------------
    # ACCURACY AND F-SCORE
    # -------------

    # Accuracy
    # ====================== YOUR CODE HERE ======================
    accuracy = accuracy_score(y_test, y_test_assig_skl)
    # ============================================================
    print("***************")
    print(
        "The accuracy of the Logistic Regression classifier is {:.4f}".format(accuracy)
    )
    print("***************")

    # F1 score
    # ====================== YOUR CODE HERE ======================
    f_score = f1_score(y_test, y_test_assig_skl)
    # ============================================================
    print("")
    print("***************")
    print(
        "The F1-score of the Logistic Regression classifier is {:.4f}".format(f_score)
    )
    print("***************")
