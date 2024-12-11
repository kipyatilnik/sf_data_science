""" Игра угадай число.

Компьютер сам загадывает и сам угадывает число.
"""

import numpy as np

def random_predict(number: int=1) -> int:
    """ Случайно угадываем число.

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток.
    """
    
    count = 0
        
    while True:
        count += 1 
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break 
    return count
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (int): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_mean = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_mean.append(random_predict(number))
    
    score = int(np.mean(count_mean))
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток.')
    
    return score


if __name__ == '__main__':
    score_game(random_predict)