"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num * num for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_Prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    if (n % 2 == 0):
        return False

    for i in range(3, int(n**0.5 + 1), 2):
        if (n % i == 0):
            return False

    return True

def filter_numbers(nums, fltr):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if fltr == ODD:
        return list(filter(lambda x: x % 2 == 1, nums))
    elif fltr == EVEN:
        return list(filter(lambda x: x % 2 == 0, nums))
    elif fltr == PRIME:
        return list(filter(is_Prime, nums))

def main():
    print(power_numbers(1, 4, 7, 4, 90))
    print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ODD))
    print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], EVEN))
    print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], PRIME))

if __name__ == "__main__":
    main()
