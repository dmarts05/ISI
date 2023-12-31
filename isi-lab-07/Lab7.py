#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:19:51 2022
Modified on March 2023

@author: dmarts05
"""

import h5py
import os
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.metrics import f1_score


def create_k_folds(n_splits, classes, stratified=False):
    """
    Creates a vector with as many elements as elements are in the dataset. Each
    element of such vector contains the number of the index of the fold in
    which that element should be. This assignation is made randomly.

    Parameters
        ----------
        n_splits: int
            Number of folds to generate.
        classes: numpy 1D array
            Vector that indicates the classes of the elements of the dataset.
        stratified: boolean
            Boolean variable which indicates whether the k-fold partition
            should be stratified (True) or not (False). Default value: False

    Returns
        -------
        indices_folds: numpy 1D array
            Vector (numpy 1D array) with the same length as the input vector y
            that contains the fold in which the corresponding element of the
            dataset should be.
            It means that, if the i-th position of the output vector is N, then
            the element X[i] of the dataset, whose class is y[i] will be in the
            N-th fold.
    """
    indices_folds = np.zeros(classes.shape, dtype=int)

    if not stratified:
        # ====================== YOUR CODE HERE ======================
        # Randomly shuffle the indices of the dataset
        indices_shuffled = np.random.permutation(classes.shape[0])

        # Calculate the size of each fold
        fold_size = classes.shape[0] // n_splits

        # Assign each element to a fold
        for fold_idx in range(n_splits):
            start_idx = fold_idx * fold_size
            end_idx = (fold_idx + 1) * fold_size
            indices_folds[indices_shuffled[start_idx:end_idx]] = fold_idx
        # ============================================================
    else:
        # ====================== YOUR CODE HERE ======================
        unique_classes, counts_classes = np.unique(classes, return_counts=True)
        folds = []
        for _ in range(n_splits):
            folds.append([])

        for class_idx, class_count in enumerate(counts_classes):
            class_indices = np.where(classes == unique_classes[class_idx])[0]
            np.random.shuffle(class_indices)
            class_folds = np.array_split(class_indices, n_splits)

            for fold_idx in range(n_splits):
                folds[fold_idx] += list(class_folds[fold_idx])

        np.random.shuffle(folds)

        for fold_idx, fold in enumerate(folds):
            indices_folds[fold] = fold_idx
        # ============================================================

    return indices_folds


# %%
# -------------
# MAIN PROGRAM
# -------------
if __name__ == "__main__":
    np.random.seed(323)

    dir_data = "Data"
    data_path = os.path.join(dir_data, "mammographic_data.h5")

    # %%
    # -------------
    # PRELIMINARY: LOAD DATASET
    # -------------

    # import features and labels
    h5f_data = h5py.File(data_path, "r")

    features_ds = h5f_data["data"]
    labels_ds = h5f_data["labels"]

    X = np.array(features_ds)
    y = np.array(labels_ds)
    # y = np.reshape(y, newshape=(y.shape[0],))
    y = y.flatten()

    h5f_data.close()

    # %%
    # -------------
    # PART 1: CREATE K FOLDS AND CHECK THE PROPORTIONS
    # -------------
    K = 10  # number of folds

    # Generate the indices of the folds by calling create_k_folds
    # ====================== YOUR CODE HERE ======================
    indices_folds = create_k_folds(K, y, stratified=True)
    # ============================================================

    proportion_class_0 = np.sum(y == 0) / y.size
    proportion_class_1 = 1 - proportion_class_0
    print("**********************************************************")
    print("****** CHECK THE CLASS PROPORTIONS WITHIN THE FOLDS ******")
    print("**********************************************************")
    print("\n")
    print("The distribution of the complete dataset is:")
    print("- {:.2f} % elements of class 0".format(100 * proportion_class_0))
    print("- {:.2f} % elements of class 1".format(100 * proportion_class_1))
    print("\n")
    print("The distribution of the elements within each fold is:")

    for i in range(K):
        # Obtain the indices of the test set elements (i.e., those in fold i)
        test_indices = np.nonzero(indices_folds == i)[0]
        # Obtain the indices of the test set elements (i.e., those in the other
        # folds)
        train_indices = np.nonzero(indices_folds != i)[0]

        prop_class_0_train = np.sum(y[train_indices] == 0) / train_indices.size
        prop_class_1_train = 1 - prop_class_0_train
        prop_class_0_test = np.sum(y[test_indices] == 0) / test_indices.size
        prop_class_1_test = 1 - prop_class_0_test
        print("* FOLD {}:".format(i + 1))
        print(
            "  - TRAIN: {:.2f} % elements of class 0;  {:.2f} % elements of class 1".format(
                100 * prop_class_0_train, 100 * prop_class_1_train
            )
        )
        print(
            "  - TEST: {:.2f} % elements of class 0;  {:.2f} % elements of class 1".format(
                100 * prop_class_0_test, 100 * prop_class_1_test
            )
        )

    # %%
    # -------------
    # PART 2: CROSS VALIDATION WITH SVM
    # -------------

    # Parameters for SVM
    C_value = 1
    kernel_type = "linear"

    # Initialization of the vectors to store the accuracies and Fscores
    # of each fold
    accuracies = np.zeros(shape=(K,))
    Fscores = np.zeros(shape=(K,))

    # Cross-validation iterative process
    for i in range(K):
        # Use the indices of the test and train set elements of the i-th fold
        # to extract the train and test subsets of this fold.
        # ====================== YOUR CODE HERE ======================
        X_train_fold = X[indices_folds != i]
        y_train_fold = y[indices_folds != i]
        X_test_fold = X[indices_folds == i]
        y_test_fold = y[indices_folds == i]
        # ============================================================

        # Standardize data of this fold
        scaler = preprocessing.StandardScaler()
        scaler.fit(X_train_fold)
        X_train_fold = scaler.transform(X_train_fold)
        X_test_fold = scaler.transform(X_test_fold)

        # Instantiate the SVM with the defined kernel type and C value, train
        # it and use it to classify. Use the train and test sets of the current
        # iteration.
        # ====================== YOUR CODE HERE ======================
        # Instantiate
        svc = svm.SVC(C=C_value, kernel=kernel_type)

        # Train
        svc.fit(X_train_fold, y_train_fold)

        # Classify test set
        y_test_assig_fold = svc.predict(X_test_fold)
        # ============================================================

        # Compute the accuracy and f-score of the test set in this fold and
        # store them in the vectors accuracies and Fscores, respectively
        # ====================== YOUR CODE HERE ======================
        accuracy_fold = np.mean(y_test_fold == y_test_assig_fold)
        Fscore_fold = f1_score(y_test_fold, y_test_assig_fold)

        accuracies[i] = accuracy_fold
        Fscores[i] = Fscore_fold
        # ============================================================

    # %%
    # -------------
    # PART 3: SHOW FINAL RESULTS
    # -------------

    print("\n\n")
    print("***********************************************")
    print("******* RESULTS OF THE CROSS VALIDATION *******")
    print("***********************************************")
    print("\n")

    for i in range(K):
        print("FOLD {}:".format(i + 1))
        print("    Accuracy = {:4.3f}".format(accuracies[i]))
        print("    Fscore = {:5.3f}".format(Fscores[i]))

    # ====================== YOUR CODE HERE ======================
    # Calculate mean and std of the accuracies and F1-scores
    mean_accuracy = np.mean(accuracies)
    std_accuracy = np.std(accuracies)
    mean_fscore = np.mean(Fscores)
    std_fscore = np.std(Fscores)
    # ============================================================

    print("\n")
    print(
        "AVERAGE ACCURACY = {:4.3f}; STD ACCURACY = {:4.3f}".format(
            mean_accuracy, std_accuracy
        )
    )
    print(
        "AVERAGE FSCORE = {:4.3f}; STD FSCORE = {:4.3f}".format(mean_fscore, std_fscore)
    )
    print("\n")
    print("***********************************************")
    print("***********************************************")
    print("***********************************************")
    print("\n\n\n")
