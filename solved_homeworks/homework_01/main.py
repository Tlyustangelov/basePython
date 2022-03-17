"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*number):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    powed_numbers = []
    for num in number:
        powed_numbers.append(pow(num,2))
    return powed_numbers


def is_prime(number):
    # функция для проверки на простое число

    if number < 2:
        return False

    for i in range (2,number):
        if number % i == 0:
            return False
    return True


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(*number,arg):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if arg == PRIME:
        return list(filter(is_prime, number))
    else:
        ost = 0
        if arg == ODD:
            ost = 1
        return list(filter(lambda x: x % 2 == ost, number))