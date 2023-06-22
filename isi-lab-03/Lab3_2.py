import numpy as np

m = np.random.uniform(0, 3, size=(20, 20))

# a
print("a)")
print(m)

print()

# b
print("b)")
coords = np.where((m >= 1.0) & (m <= 2.0))
formatted_coords = [f"({i}, {j})" for i, j in zip(coords[0], coords[1])]
print(formatted_coords)

print()

# c
print("c)")
coords = np.where((m < 1.0) | (m > 2.0))
formatted_coords = [f"({i}, {j})" for i, j in zip(coords[0], coords[1])]
print(formatted_coords)

print()

# d
print("d)")
rounded_m = m.round()
print(rounded_m)

coords = np.where(rounded_m != 1)
formatted_coords = [f"({i}, {j})" for i, j in zip(coords[0], coords[1])]
print(formatted_coords)
