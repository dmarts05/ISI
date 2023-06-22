# import necessary packages
import pandas as pd
import numpy as np

# load the AirlinesCluster dataset
url = "AirlinesCluster.csv"
airlines_dataset = pd.read_csv(url)
# suppress scientific float notation
np.set_printoptions(precision=5, suppress=True)

print("********** Dataset loading questions **********")
# visualization of the first few records of the dataset
print(airlines_dataset.head())
print(airlines_dataset.head(n=2))
# visualization of the last few records from the dataset
print(airlines_dataset.tail())
print(airlines_dataset.tail(n=2))
# display the different datatypes available in the dataset
print(airlines_dataset.dtypes)
# visualization of descriptive stats of the dataset
print(airlines_dataset.describe())

# Question 1.3.1: Based on the previous result, which two features have (on average) the smallest values and the largest values?
print("********** Question 1.3.1 **********")
# Get feature with the smallest value on average
print(
    "Feature with smallest value on average"
    f" ({str(airlines_dataset.mean().min())}):"
    f" {str(airlines_dataset.mean().idxmin())}"
)
# Get feature with the highest value on average
print(
    "Feature with highest value on average"
    f" ({str(airlines_dataset.mean().max())}):"
    f" {str(airlines_dataset.mean().idxmax())}"
)

print("********** Dataset preprocessing questions **********")
# import the necessary packages
from sklearn import preprocessing

# standardize the data to normal distribution
dataset_standardized = preprocessing.scale(airlines_dataset)
# visualization of descriptive stats of the normalized dataset
dataset_standardized = pd.DataFrame(dataset_standardized)
print(dataset_standardized.describe())

# Question 1.4.1: What are the mean and standard deviation of the features in the standardized dataset?
print("********** Question 1.4.1 **********")
# Get mean of the standardized dataset
print("Mean of the standardized dataset: ")
print(dataset_standardized.mean())
# Get standard deviation of the standardized dataset
print("Standard deviation of the standardized dataset: ")
print(dataset_standardized.std())

# Question 1.4.2: Based on the normalized dataset descriptive stats, which two features have (on average) the smallest values and the largest values?
print("********** Question 1.4.2 **********")
# Get feature with the smallest value on average
print(
    "Feature with smallest value on average"
    f" ({str(dataset_standardized.mean().min())}):"
    f" {str(dataset_standardized.mean().idxmin())}"
)
# Get feature with the highest value on average
print(
    "Feature with highest value on average"
    f" ({str(dataset_standardized.mean().max())}):"
    f" {str(dataset_standardized.mean().idxmax())}"
)

print(
    "********** Building and using the clustering model questions **********"
)
# import necessary packages
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 7))
# visualization of the original data
plt.subplot(221)
plt.scatter(dataset_standardized[0], dataset_standardized[1])
plt.title("Original unclustered data")
# train the model using k=2
kmeans_model = KMeans(n_clusters=2, random_state=42)
kmeans_model.fit(dataset_standardized)
kmeans_predictions = kmeans_model.predict(dataset_standardized)
# visualization of the clustered data using k=2
plt.subplot(222)
plt.scatter(
    dataset_standardized[0], dataset_standardized[1], c=kmeans_predictions
)
plt.title("Clustered data, k=2")
# train the model using k=3
kmeans_model = KMeans(n_clusters=3, random_state=42)
kmeans_model.fit(dataset_standardized)
kmeans_predictions = kmeans_model.predict(dataset_standardized)
# visualization of the clustered data using k=3
plt.subplot(223)
plt.scatter(
    dataset_standardized[0], dataset_standardized[1], c=kmeans_predictions
)
plt.title("Clustered data, k=3")
# train the model using k=5
kmeans_model = KMeans(n_clusters=5, random_state=42)
kmeans_model.fit(dataset_standardized)
kmeans_predictions = kmeans_model.predict(dataset_standardized)
# visualization of the clustered data using k=5
plt.subplot(224)
plt.scatter(
    dataset_standardized[0], dataset_standardized[1], c=kmeans_predictions
)
plt.title("Clustered data, k=5")
plt.show()
# visualization of descriptive stats of the clustered data using k=5
cluster_kmeans_data = pd.DataFrame(kmeans_predictions + 1)
airlines_dataset["KmeansCluster"] = cluster_kmeans_data
kmeans_mean_cluster_pd = pd.DataFrame(
    airlines_dataset.groupby("KmeansCluster").mean()
)
print(kmeans_mean_cluster_pd)

# Consider the results of the clustering model using k=5.
# Question 2.1.1.1: Compared to the other clusters, Cluster 1 has the largest average values in which features (if any)? Based on this, how would you describe the Airline’s customers in Cluster 1?
# Question 2.1.1.2: Apply the previous analysis to the remaining four clusters and describe them.
print("********** Question 2.1.1.1 + Question 2.1.1.2 **********")
# Get highest average value for Balance, QualMiles, BonusMiles, BonusTrans, FlightMiles, FlightTrans, DaysSinceEnroll and get the cluster
print(
    "Cluster with highest average value for Balance, QualMiles, BonusMiles,"
    " BonusTrans, FlightMiles, FlightTrans, DaysSinceEnroll:"
)
print(
    kmeans_mean_cluster_pd[
        [
            "Balance",
            "QualMiles",
            "BonusMiles",
            "BonusTrans",
            "FlightMiles",
            "FlightTrans",
            "DaysSinceEnroll",
        ]
    ].idxmax()
)
# Get lowest average value for Balance, QualMiles, BonusMiles, BonusTrans, FlightMiles, FlightTrans, DaysSinceEnroll and get the cluster
print(
    "Cluster with lowest average value for Balance, QualMiles, BonusMiles,"
    " BonusTrans, FlightMiles, FlightTrans, DaysSinceEnroll:"
)
print(
    kmeans_mean_cluster_pd[
        [
            "Balance",
            "QualMiles",
            "BonusMiles",
            "BonusTrans",
            "FlightMiles",
            "FlightTrans",
            "DaysSinceEnroll",
        ]
    ].idxmin()
)
