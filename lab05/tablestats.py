from collections.abc import Iterable


def read_rows(lines: Iterable[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        fields = line.split(",")
        values: list[str] = []
        for field in fields:
            values.append(field.strip())

        if headers is None:
            headers = values
            continue

        if len(values) != len(headers):
            continue

        row: dict[str, str] = {}
        for index in range(len(headers)):
            row[headers[index]] = values[index]
        rows.append(row)

    return rows


def count_types(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for row in rows:
        kind = row.get("тип")
        if kind is None:
            continue

        if kind in counts:
            counts[kind] = counts[kind] + 1
        else:
            counts[kind] = 1

    return counts


def total_minutes(rows: list[dict[str, str]], kind: str) -> float:
    total = 0.0

    for row in rows:
        if row.get("тип") != kind:
            continue

        value = row.get("минуты")
        if value is None:
            continue

        value = value.replace(",", ".")
        try:
            minutes = float(value)
        except ValueError:
            continue

        total = total + minutes

    return round(total, 1)


def to_csv(counts: dict[str, int]) -> str:
    lines: list[str] = ["тип,количество"]

    kinds = sorted(counts)
    for kind in kinds:
        line = str(kind) + "," + str(counts[kind])
        lines.append(line)

    result = "\n".join(lines)
    result = result + "\n"
    return result
