import numpy as np

np.set_printoptions(precision=2)

m = np.random.uniform(-10, 10, size=(10, 4))
print(m)

print()

# a
print("a)")
# Compute Euclidean distance matrix
dist_m = np.sqrt(((m[:, None, :] - m) ** 2).sum(axis=2))
print(dist_m)

print()

# b
print("b)")

# Find pairs of points with distance < 10
dist_10_points = np.column_stack(np.where(dist_m < 10))

# Create messages for those pairs of points
msgs = [
    f"The Euclidean distance between vectors {i} and {j} is {dist_m[i, j]:.2f}."
    for i, j in dist_10_points
]

# Print messages
for msg in msgs:
    print(msg)
