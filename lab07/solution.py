import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0:
        return []

    if len(values) % width != 0:
        return []

    array = np.asarray(values, dtype=float)
    table = array.reshape((-1, width))
    return table.tolist()


def block(
    matrix: list[list[float]], rows: list[int], columns: list[int]
) -> list[list[float]]:
    if len(matrix) == 0:
        return []

    array = np.asarray(matrix, dtype=float)
    selected = array[np.ix_(rows, columns)]
    return selected.tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if len(matrix) == 0:
        return []

    array = np.asarray(matrix, dtype=float)
    means = np.mean(array, axis=0)
    rounded_means = np.round(means, 6)
    return rounded_means.tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if len(matrix) == 0:
        return 0.0

    array = np.asarray(matrix, dtype=float)
    values = array[:, column]
    value_range = np.max(values) - np.min(values)
    return round(float(value_range), 6)
