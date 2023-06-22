# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

# load the AirlinesCluster dataset
url = "AirlinesCluster.csv"
airlines_dataset = pd.read_csv(url)
# suppress scientific float notation
np.set_printoptions(precision=5, suppress=True)

# standardize the data to normal distribution
dataset_standardized = preprocessing.scale(airlines_dataset)
# visualization of descriptive stats of the normalized dataset
dataset_standardized = pd.DataFrame(dataset_standardized)

# Implementation of the Elbow method
Sum_of_squared_errors = []
# Definition of the number of clusters to evaluated
K = range(1, 30)
for k in K:
    # Training of kmeans model using k clusers
    kmeans_model = KMeans(n_clusters=k, random_state=42)
    kmeans_model.fit(dataset_standardized)
    # Computing the sum of squared errors for the trained model
    Sum_of_squared_error = kmeans_model.inertia_
    Sum_of_squared_errors.append(Sum_of_squared_error)
# Visualization of the Sum of Squared Error vs the Number of clusters curve
plt.figure(figsize=(10, 5))
plt.plot(K, Sum_of_squared_errors, "bx-")
plt.xlabel("Number of clusters, k")
plt.ylabel("Sum of squared errors")
plt.title("Elbow Method For Optimal k")
plt.show()


k_sum_of_squared_errors = np.column_stack((K, Sum_of_squared_errors))
print(k_sum_of_squared_errors)
