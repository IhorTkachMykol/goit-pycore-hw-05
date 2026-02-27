import sys


def parse_log_line(line: str) -> dict:
    """
    Парсить один рядок логу і повертає словник.
    Формат:
    YYYY-MM-DD HH:MM:SS LEVEL Message...
    """
    parts = line.strip().split()

    if len(parts) < 4:
        raise ValueError(f"Неправильний формат логу: {line}")

    date = parts[0]
    time = parts[1]
    level = parts[2]
    message = " ".join(parts[3:])

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    """Завантажує файл логів і повертає список словників."""
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує лог-записи за рівнем."""
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів за рівнем логування."""
    levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
    return {lvl: sum(1 for log in logs if log["level"] == lvl) for lvl in levels}


def display_log_counts(counts: dict):
    """Виводить таблицю з кількістю записів кожного рівня."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    # Перевірка аргументів
    if len(sys.argv) < 2:
        print("Помилка: потрібно передати шлях до лог-файлу.")
        print("Приклад: python main.py logfile.log")
        return

    file_path = sys.argv[1]
    level_filter = sys.argv[2].lower() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    # Підрахунок статистики
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо задано рівень фільтрації
    if level_filter:
        print()
        print(f"Деталі логів для рівня '{level_filter.upper()}':")

        filtered = filter_logs_by_level(logs, level_filter)

        if not filtered:
            print("Немає записів цього рівня.")
            return

        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
