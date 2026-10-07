def winner(names: list[str], scores: list[float]) -> str:
    """Return the name with the highest score, keeping the earliest tie."""
    if not names:
        return ""

    best_index = 0
    for index in range(1, len(scores)):
        if scores[index] > scores[best_index]:
            best_index = index
    return names[best_index]


def average(scores: list[float]) -> float:
    """Return the mean score rounded to two decimal places."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    """Return participant names ordered by descending score."""
    indices = sorted(range(len(names)), key=lambda index: scores[index], reverse=True)
    return [names[index] for index in indices]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    """Return names of participants scoring strictly above the average."""
    mean_score = average(scores)
    return [name for name, score in zip(names, scores) if score > mean_score]
