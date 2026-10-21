def count_items(values: list) -> dict:
    counts = {}

    for value in values:
        counts[value] = counts.get(value, 0) + 1

    return counts


def unique_sorted(values: list) -> list:
    return sorted(set(values))


def common(first: list, second: list) -> list:
    first_values = set(first)
    second_values = set(second)
    shared_values = first_values & second_values
    return sorted(shared_values)


def only_in_first(first: list, second: list) -> list:
    first_values = set(first)
    second_values = set(second)
    first_only_values = first_values - second_values
    return sorted(first_only_values)
