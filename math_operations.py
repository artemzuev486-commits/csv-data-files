#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль с математическими операциями
Операции: сложение, вычитание, умножение, деление, возведение в степень
"""

def calculate_addition(operand_1: float, operand_2: float) -> float:
    result = operand_1 + operand_2
    return result


def calculate_subtraction(operand_1: float, operand_2: float) -> float:
    result = operand_1 - operand_2
    return result


def calculate_multiplication(operand_1: float, operand_2: float) -> float:
    result = operand_1 * operand_2
    return result


def calculate_division(operand_1: float, operand_2: float) -> float:
    if operand_2 == 0:
        raise ValueError("Деление на ноль невозможно")
    result = operand_1 / operand_2
    return result


def calculate_power(operand_1: float, operand_2: float) -> float:
    result = operand_1 ** operand_2
    return result


if __name__ == "__main__":
    # Тестирование всех операций
    a, b = 8, 2
    
    print(f"{a} + {b} = {calculate_addition(a, b)}")
    print(f"{a} - {b} = {calculate_subtraction(a, b)}")
    print(f"{a} * {b} = {calculate_multiplication(a, b)}")
    print(f"{a} / {b} = {calculate_division(a, b)}")
    print(f"{a} ^ {b} = {calculate_power(a, b)}")