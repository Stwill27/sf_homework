"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lower_bound = 1 #нижняя граница предполагаемого списка
    upper_bound = 101 #верхняя граница предполагаемого списка
    
    while True:
        count += 1
        predict_number = (upper_bound+lower_bound-1)//2 #предполагаемое число
        
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number > number:
            upper_bound = predict_number #коррекция верхней границы
        elif predict_number < number:
            lower_bound = predict_number + 1 #коррекция нижней границы
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

score_game(random_predict)