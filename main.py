"""Скрипт для автоматического создания git-коммитов по датам."""

from datetime import date


def make_commits(start: date, days: int):
    """Создаёт указанное число коммитов, начиная с даты start."""
    start_ord = start.toordinal()

    for i in range(days):
        current = date.fromordinal(start_ord + i)
        human_date = current.strftime("%d.%m.%Y г.")

        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(human_date + "\n")


def main():
    """Точка входа — создает 31 коммит начиная с 1 января 2025."""
    start = date(2025, 1, 1)
    make_commits(start, 31)


if __name__ == "__main__":
    main()
