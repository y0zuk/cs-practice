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
