import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the file as a pandas dataframe
df = pd.read_csv("company_sales_data.csv")

# Extract the sales data for facecream and facewash for all the months
face_cream_sales = df["facecream"]
face_wash_sales = df["facewash"]
months = df["month_number"]

# Bar chart
bar_width = 0.35
plt.bar(
    months,
    face_cream_sales,
    width=-(bar_width / 2),
    align="edge",
    label="Face Cream sales data",
    color="b",
)
plt.bar(
    months,
    face_wash_sales,
    width=bar_width / 2,
    align="edge",
    label="Face Wash sales data",
    color="orange",
)

plt.xticks(np.arange(1, months.max() + 1))

plt.grid(linestyle="dashed")

plt.xlabel("Month number")
plt.ylabel("Sales units in number")

plt.title("Facewash and facecream sales data")

plt.legend(loc="upper left")
plt.show()
