from pathlib import Path

from tablestats import count_types, read_rows, to_csv, total_minutes


def main():
    table_name = input().strip()
    table_path = Path(__file__).parent / table_name

    with open(table_path, encoding="utf-8") as table:
        rows = read_rows(table)

    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(total_minutes(rows, "ошибка"))

    summary_path = Path(__file__).with_name("summary.csv")
    with open(summary_path, "w", encoding="utf-8") as output:
        output.write(to_csv(counts))


if __name__ == "__main__":
    main()
