import numpy as np


def main():
    array = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]])

    print("\nArray:")
    print(array)

    print("\nArray[:, :]:")
    print(array[:, :])

    print("\nArray[:, 1:]:")
    print(array[:, 1:])

    print("\nArray[:, :1]:")
    print(array[:, :1])


main()