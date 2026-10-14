def read_rows(lines):
    rows = []
    headers = None

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        fields = line.split(",")
        values = []
        for field in fields:
            values.append(field.strip())

        if headers is None:
            headers = values
            continue

        if len(values) != len(headers):
            continue

        row = {}
        for index in range(len(headers)):
            row[headers[index]] = values[index]
        rows.append(row)

    return rows


def count_types(rows):
    counts = {}

    for row in rows:
        kind = row.get("тип")
        if kind is None:
            continue

        if kind in counts:
            counts[kind] = counts[kind] + 1
        else:
            counts[kind] = 1

    return counts


def total_minutes(rows, kind):
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
