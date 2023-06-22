import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the iris dataset into a DataFrame using Pandas
df = pd.read_csv("iris.csv")

# Create 3D scatter plot
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

x = df["sepal_length"]
y = df["sepal_width"]
z = df["petal_length"]
marker_size = df["petal_width"] * 10

setosa = ax.scatter(
    x[df["variety"] == "Setosa"],
    y[df["variety"] == "Setosa"],
    z[df["variety"] == "Setosa"],
    c="indigo",
    s=marker_size[df["variety"] == "Setosa"],
    marker="o",
    label="Setosa",
)

versicolor = ax.scatter(
    x[df["variety"] == "Versicolor"],
    y[df["variety"] == "Versicolor"],
    z[df["variety"] == "Versicolor"],
    c="c",
    s=marker_size[df["variety"] == "Versicolor"],
    marker="o",
    label="Versicolor",
)

virginica = ax.scatter(
    x[df["variety"] == "Virginica"],
    y[df["variety"] == "Virginica"],
    z[df["variety"] == "Virginica"],
    c="orangered",
    s=marker_size[df["variety"] == "Virginica"],
    marker="o",
    label="Virginica",
)

# Add legend
ax.legend(
    handles=[setosa, versicolor, virginica],
    loc="upper right",
    bbox_to_anchor=(1.3, 1.1),
)

# Calculate the center of mass of each variety
com_setosa = np.mean(
    df[df["variety"] == "Setosa"][
        ["sepal_length", "sepal_width", "petal_length"]
    ].values,
    axis=0,
)
com_versicolor = np.mean(
    df[df["variety"] == "Versicolor"][
        ["sepal_length", "sepal_width", "petal_length"]
    ].values,
    axis=0,
)
com_virginica = np.mean(
    df[df["variety"] == "Virginica"][
        ["sepal_length", "sepal_width", "petal_length"]
    ].values,
    axis=0,
)

# Add labels to the center of mass of each variety
ax.text(com_setosa[0], com_setosa[1], com_setosa[2], "Setosa", fontsize=8)
ax.text(
    com_versicolor[0], com_versicolor[1], com_versicolor[2], "Versicolor", fontsize=8
)
ax.text(com_virginica[0], com_virginica[1], com_virginica[2], "Virginica", fontsize=8)

# Set the axis labels and title
ax.set_xlabel(df.columns[0])
ax.set_ylabel(df.columns[1])
ax.set_zlabel(df.columns[2])
ax.set_title("Scatter plot of the iris dataset")

# Show the plot
plt.show()
