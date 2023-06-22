import numpy as np

# a
print("a)")
Matrix1 = np.array([[4, -2, 7], [9, 4, 1], [5, -1, 5]], dtype=int)
print(Matrix1)

print()

# b
print("b)")
Matrix2 = Matrix1.transpose()
print(Matrix2)

print()

# c
print("c)")
wise_prodM1M2 = Matrix1 * Matrix2
print(wise_prodM1M2)

print()

# d
print("d)")
prodM1M2 = Matrix1 @ Matrix2
print(prodM1M2)

print()

# e
print("e)")
prodM2M1 = Matrix2 @ Matrix1
print(prodM2M1)

print()

# f
print("f)")
mat_corners = Matrix1[:: Matrix1.shape[0] - 1, :: Matrix1.shape[1] - 1]
print(mat_corners)

print()

# g
print("g)")
max = Matrix1.max()
vec_max = Matrix1.max(axis=1)
print(f"Global max of Matrix1: {max}")
print(f"Each row's max of Matrix1: {vec_max}")

print()

# h
print("h)")
min = Matrix1.min()
vec_min = Matrix1.min(axis=0)
print(f"Global min of Matrix1: {min}")
print(f"Each columns' min of Matrix1: {vec_min}")

print()

# i
print("i)")
prod_minmax = vec_min.reshape(-1, 1) @ vec_max.reshape(1, -1)
print(prod_minmax)

print()

# j
print("j)")
mat_sum = Matrix1[:, [0, 2]].sum(
    axis=0,
)
print(mat_sum)
