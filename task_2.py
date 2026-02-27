import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту.
    Числа вважаються коректними та відокремленими пробілами.
    """
    # Знаходимо всі дійсні числа (формат: 12, 12.5, 0.01, 1000.01 тощо)
    pattern = r"\d+\.\d+|\d+"  # дійсні числа або цілі
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    """
    Повертає суму всіх чисел у тексті, використовуючи генератор func.
    """
    return sum(func(text))
  

text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
