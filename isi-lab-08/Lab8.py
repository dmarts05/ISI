import os
import pandas as pd
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.svm import SVC
import numpy as np


def load_config_json(file_name: str) -> dict:
    """Load configuration file in JSON format.

    Args:
        file_name (str): Configuration file name.

    Returns:
        dict: Configuration file contents.
    """

    import json

    with open(file_name, "r") as file:
        config = json.load(file)

    return config


def load_clf_config(config: dict, clf_num: int) -> dict:
    """Load clf configuration.

    Args:
        config (dict): Configuration file contents.
        clf (int): clf number.

    Returns:
        dict: clf configuration.
    """

    if clf_num == 1:
        params = config["knn"]
    elif clf_num == 2:
        params = config["logistic_regression"]
    elif clf_num == 3:
        params = config["svm"]
    elif clf_num == 4:
        params = config["naive_bayes"]
    elif clf_num == 5:
        params = config["perceptron"]

    return params


def show_clf_select_menu():
    """Show clf selection menu."""

    print("Select a clf:")
    print("1. KNN")
    print("2. Logistic Regression")
    print("3. SVM")
    print("4. Naive Bayes")
    print("5. Perceptron")


def select_clf() -> int:
    """Select a clf."""

    while True:
        try:
            show_clf_select_menu()
            clf = int(input("Enter your choice: "))
            if clf < 1 or clf > 5:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return clf


if __name__ == "__main__":
    # Load configuration file
    config = load_config_json("config.json")

    # Select a clf
    clf_num = select_clf()

    # Set numpy random seed
    np.random.seed(config["general"]["random_seed"])

    # Directory containing the data
    dir_data = "Data"

    # Read the CSV file into a DataFrame
    data_medium_high_df = pd.read_csv(
        os.path.join(dir_data, "data_inserts_Medium-high.csv")
    )

    # Extract features (X_df) and target labels (y_df) from the DataFrame
    y_df = data_medium_high_df[["Class"]].copy()
    X_df = data_medium_high_df.copy()
    X_df = X_df.drop("Class", axis=1)

    # Convert features and labels to NumPy arrays
    X = X_df.to_numpy()
    y = y_df.to_numpy()

    # Split the data into training and testing sets
    proportion_test = config["general"]["proportion_test"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.ravel(), test_size=proportion_test
    )

    # Standardize the data if the parameter is set to True
    if config["general"]["standardize"]:
        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Load clf config data
    params = load_clf_config(config, clf_num)

    # Create an instance of the selected clf
    if clf_num == 1:
        clf = KNeighborsClassifier(n_neighbors=params["n_neighbors"], p=params["p"])
    elif clf_num == 2:
        clf = LogisticRegression(C=params["C"], solver=params["solver"])
    elif clf_num == 3:
        # degree is only used for polynomial kernel and gamma is only used for rbf, poly and sigmoid kernels
        clf = SVC(
            C=params["C"],
            kernel=params["kernel"],
            # gamma=params["gamma"],
            # degree=params["degree"],
        )
    elif clf_num == 4:
        clf = GaussianNB()
    elif clf_num == 5:
        clf = Perceptron(alpha=params["alpha"])
    # Train the clf on the training data
    clf.fit(X_train, y_train)

    # Make predictions on the test data
    y_test_assig = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_true=y_test, y_pred=y_test_assig)
    print("Accuracy: {:.4f}".format(accuracy))

    # Calculate precision
    precision = precision_score(y_true=y_test, y_pred=y_test_assig)
    print("Precision: {:.4f}".format(precision))

    # Calculate sensitivity (true positive rate or recall)
    sensitivity = recall_score(y_true=y_test, y_pred=y_test_assig)
    print("Sensitivity (TPR): {:.4f}".format(sensitivity))

    # Calculate specificity (true negative rate)
    specificity = recall_score(y_true=y_test, y_pred=y_test_assig, pos_label=0)
    print("Specificity (TNR): {:.4f}".format(specificity))

    # Calculate f1 score
    f_score = f1_score(y_true=y_test, y_pred=y_test_assig)
    print("F1 score: {:.4f}".format(f_score))
