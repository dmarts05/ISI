# import necessary packages
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.hierarchy import fcluster
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd

# Loading and standardizing the data to normal distribution
url = "AirlinesCluster.csv"
airlines_dataset = pd.read_csv(url)
dataset_standardized = preprocessing.scale(airlines_dataset)
dataset_standardized_pd = pd.DataFrame(dataset_standardized)
# Creating the linkage matrix and perform hierarchical clustering on samples
hierarchical_cluster = linkage(dataset_standardized, "ward")
# Plot a complete dendrogram
plt.title("Hierarchical Clustering Dendrogram (complete)")
plt.xlabel("Sample index or (cluster size)")
plt.ylabel("Distance")
dendrogram(
    hierarchical_cluster,
    leaf_rotation=90,
    leaf_font_size=6,
)
plt.show()
# Plot a truncated dendrogram at 5 clusters
plt.title("Hierarchical Clustering Dendrogram (truncated)")
plt.xlabel("Sample index or (cluster size)")
plt.ylabel("Distance")
dendrogram(
    hierarchical_cluster,
    truncate_mode="lastp",  # show only the last p merged clusters
    p=5,  # show only the last p merged clusters
    leaf_rotation=90.0,
    leaf_font_size=12.0,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()
# visualization of the clustered data using 5 clusters
num_clusters = 5
hierarchical_cluster_predictions = fcluster(
    hierarchical_cluster, num_clusters, criterion="maxclust"
)
hierarchical_cluster_predictions[0:30:],
# Plotting clustered data using independent colors
plt.figure(figsize=(10, 8))
dataset_standardized_pd = pd.DataFrame(dataset_standardized)
plt.scatter(
    dataset_standardized_pd.iloc[:, 0],
    dataset_standardized_pd.iloc[:, 1],
    c=hierarchical_cluster_predictions,
    cmap="prism",
)
plt.title("Airline Data - Hierarchical Clutering, 5 clusters")
plt.show()
# visualization of descriptive stats of the clustered data using 5 clusters
cluster_Hierarchical_data = pd.DataFrame(hierarchical_cluster_predictions)
airlines_dataset["HierarchicalCluster"] = cluster_Hierarchical_data
hierarchical_cluster_pd = pd.DataFrame(
    airlines_dataset.groupby("HierarchicalCluster").mean()
)
pd.set_option("display.max_columns", None)
print(hierarchical_cluster_pd)

# Get highest average value for Balance, QualMiles, BonusMiles, BonusTrans, FlightMiles, FlightTrans, DaysSinceEnroll and get the cluster
print(
    "Cluster with highest average value for Balance, QualMiles, BonusMiles,"
    " BonusTrans, FlightMiles, FlightTrans, DaysSinceEnroll:"
)
print(
    hierarchical_cluster_pd[
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
    hierarchical_cluster_pd[
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
