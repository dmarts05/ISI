import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import DBSCAN


def get_estimated_number_of_clusters(labels):
    # Number of clusters in labels, ignoring noise if present
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    return n_clusters


def get_estimated_number_of_noise_points(labels):
    # Number of noise points in labels (represented as -1 if present)
    n_noise_points = list(labels).count(-1)
    return n_noise_points


# Loading and standardizing the data to normal distribution
url = "AirlinesCluster.csv"
airlines_dataset = pd.read_csv(url)
dataset_standardized = preprocessing.scale(airlines_dataset)
dataset_standardized_pd = pd.DataFrame(dataset_standardized)

# Use DBSCAN to cluster the data
print("********** DBSCAN a) **********")
eps = 0.3
min_samples = 10
db = DBSCAN(eps=eps, min_samples=min_samples).fit(dataset_standardized)
labels = db.labels_
# Print eps and min_samples configuration parameters
print(
    f"DBSCAN configuration parameters: eps = {eps}, min_samples ="
    f" {min_samples}"
)
# Print the estimated number of clusters
print(
    f"Estimated number of clusters: {get_estimated_number_of_clusters(labels)}"
)
# Print the estimated number of noise points
print(
    "Estimated number of noise points:"
    f" {get_estimated_number_of_noise_points(labels)}"
)

print("********** DBSCAN b) **********")
eps = 0.3
min_samples = 5
db = DBSCAN(eps=eps, min_samples=min_samples).fit(dataset_standardized)
labels = db.labels_
# Print eps and min_samples configuration parameters
print(
    f"DBSCAN configuration parameters: eps = {eps}, min_samples ="
    f" {min_samples}"
)
# Print the estimated number of clusters
print(
    f"Estimated number of clusters: {get_estimated_number_of_clusters(labels)}"
)
# Print the estimated number of noise points
print(
    "Estimated number of noise points:"
    f" {get_estimated_number_of_noise_points(labels)}"
)

print("********** DBSCAN c) **********")
eps = 0.2
min_samples = 10
db = DBSCAN(eps=eps, min_samples=min_samples).fit(dataset_standardized)
labels = db.labels_
# Print eps and min_samples configuration parameters
print(
    f"DBSCAN configuration parameters: eps = {eps}, min_samples ="
    f" {min_samples}"
)
# Print the estimated number of clusters
print(
    f"Estimated number of clusters: {get_estimated_number_of_clusters(labels)}"
)
# Print the estimated number of noise points
print(
    "Estimated number of noise points:"
    f" {get_estimated_number_of_noise_points(labels)}"
)
