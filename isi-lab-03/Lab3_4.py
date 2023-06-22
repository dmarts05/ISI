import numpy as np
import timeit


def square_natural_numbers_list(N):
    squares = []
    for i in range(1, N + 1):
        squares.append(i**2)
    return squares


def square_natural_numbers_numpy_loop(N, arr):
    for i in range(1, N + 1):
        arr[i - 1] = i**2
    return arr


def square_natural_numbers_numpy_vectorize(N, arr):
    n = np.arange(1, N + 1)
    arr[:] = n**2
    return arr


AMOUNT_OF_NATURALS = 1000000
AMOUNT_OF_RUNS = 25
list_squares = []
numpy_squares = np.zeros(AMOUNT_OF_NATURALS, dtype=int)

# a
print("a)")
time_list = timeit.timeit(
    lambda: square_natural_numbers_list(AMOUNT_OF_NATURALS), number=AMOUNT_OF_RUNS
)
print("Time using list function: {:.4f} seconds.".format(time_list / AMOUNT_OF_RUNS))

print()

# b
print("b)")
time_numpy_loop = timeit.timeit(
    lambda: square_natural_numbers_numpy_loop(AMOUNT_OF_NATURALS, numpy_squares),
    number=AMOUNT_OF_RUNS,
)
print(
    "Time using numpy loop function: {:.4f} seconds.".format(
        time_numpy_loop / AMOUNT_OF_RUNS
    )
)

print()

# c
print("c)")
time_numpy_vectorize = timeit.timeit(
    lambda: square_natural_numbers_numpy_vectorize(AMOUNT_OF_NATURALS, numpy_squares),
    number=AMOUNT_OF_RUNS,
)
print(
    "Time using numpy vectorize function: {:.4f} seconds.".format(
        time_numpy_vectorize / AMOUNT_OF_RUNS
    )
)
