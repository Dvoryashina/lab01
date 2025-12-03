"""
TyperSteel - CLI приложение для приветствия пользователей.

Лабораторная работа №1 по изучению Git и GitHub.
Автор: Дворяшина Ирина
"""

import typer
from typing import Optional


GREETING_STYLES = {
    "formal": "Добрый день",
    "informal": "Привет"
}


def format_greeting(name: str, lastname: str, is_formal: bool) -> str:
    """
    Форматирует текст приветствия в зависимости от режима.

    Args:
        name: Имя пользователя
        lastname: Фамилия пользователя
        is_formal: Флаг формального режима

    Returns:
        str: Отформатированное приветствие
    """
    if is_formal:
        full_name = f"{name} {lastname}".strip()
        style = GREETING_STYLES["formal"]
        return f"{style}, {full_name}!"

    style = GREETING_STYLES["informal"]
    return f"{style}, {name}!"


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
    greeting = format_greeting(name, lastname or "", formal)
    typer.echo(greeting)


if __name__ == "__main__":
    # Запуск CLI приложения через Typer
    typer.run(main)
