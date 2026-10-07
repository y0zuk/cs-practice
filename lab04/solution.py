def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    bi = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[bi]:
            bi = i
    return names[bi]

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    ins = sorted(range(len(names)), key=lambda i: scores[i], reverse=True)
    return [names[i] for i in ins]


def above_average(names: list[str], scores: list[float]) -> list[str]:
    mean_score = average(scores)
    return [name for name, score in zip(names, scores) if score > mean_score]
