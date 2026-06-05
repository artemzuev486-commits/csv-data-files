#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль с математическими операциями
Использует корректные термины из словарей:
- типы данных: float, int
- ключевые слова: def, return
"""

def calculate_addition(operand_1: float, operand_2: float) -> float:
    """
    Сложение двух чисел
    """
    result = operand_1 + operand_2
    return result


def calculate_subtraction(operand_1: float, operand_2: float) -> float:
    """
    Вычитание двух чисел
    """
    result = operand_1 - operand_2
    return result


# Дополнительные функции для полноты
def calculate_multiplication(operand_1: float, operand_2: float) -> float:
    """
    Умножение двух чисел
    """
    result = operand_1 * operand_2
    return result


def calculate_division(operand_1: float, operand_2: float) -> float:
    """
    Деление двух чисел
    """
    if operand_2 == 0:
        raise ValueError("Деление на ноль невозможно")
    result = operand_1 / operand_2
    return result


def calculate_power(operand_1: float, operand_2: float) -> float:
    """
    Возведение числа в степень
    operand_1 - основание степени
    operand_2 - показатель степени
    """
    result = operand_1 ** operand_2
    return result


# Основная функция для демонстрации
if __name__ == "__main__":
    print("=" * 50)
    print("Модуль математических операций")
    print("=" * 50)
    
    # Тестирование функций
    a, b = 15.0, 7.0
    
    print(f"\nИсходные числа: a = {a}, b = {b}")
    print(f"Сложение (addition):        {a} + {b} = {calculate_addition(a, b)}")
    print(f"Вычитание (subtraction):    {a} - {b} = {calculate_subtraction(a, b)}")
    print(f"Умножение (multiplication): {a} * {b} = {calculate_multiplication(a, b)}")
    print(f"Деление (division):         {a} / {b} = {calculate_division(a, b):.2f}")
    print(f"Степень (power):            {a} ^ {b} = {calculate_power(a, b):.0f}")