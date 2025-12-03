"""
TyperSteel - CLI приложение для приветствия пользователей.

Лабораторная работа №1 по изучению Git и GitHub.
Автор: Дворяшина Ирина
"""

import typer
from typing import Optional


def main(
    name: str = typer.Argument(..., help="Имя пользователя для приветствия"),
    lastname: Optional[str] = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(
        False, "--formal", "-f", help="Использовать формальное приветствие."
    ),
) -> None:
    """
    Приветствует пользователя по имени.

    Приложение поддерживает два режима:
    - Обычное приветствие: использует только имя
    - Формальное приветствие: использует имя и фамилию

    Args:
        name: Имя пользователя (обязательный параметр)
        lastname: Фамилия пользователя (опционально)
        formal: Флаг для включения формального режима приветствия

    Returns:
        None: Выводит приветствие в консоль

    Examples:
        $ python typersteel.py Ирина
        Привет, Ирина!

        $ python typersteel.py Ирина --lastname Дворяшина --formal
        Добрый день, Ирина Дворяшина!
    """
    # Формируем приветствие в зависимости от выбранного режима
    if formal:
        # Формальное приветствие с полным именем
        full_name = f"{name} {lastname}".strip()
        greeting = f"Добрый день, {full_name}!"
    else:
        # Неформальное приветствие только с именем
        greeting = f"Привет, {name}!"

    # Выводим приветствие в консоль
    print(greeting)


if __name__ == "__main__":
    # Запуск CLI приложения через Typer
    typer.run(main)
