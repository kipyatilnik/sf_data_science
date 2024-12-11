"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
за минимальное количество попыток
"""

import numpy as np

def random_predict(number: int=1) -> int:
    """ Случайно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
        
    def optimal_selection(number, number_first, number_last, count) -> int:
        """ Оптимизируем отбор чисел.
        
        Используем рекурсию, логически отсеиваем лишние подборы
        и исключаем повторный подбор использованных чисел.

        Args:
            number (int): загаданное число. 
            number_first (int): нижняя граница диапозона подбора.
            number_last (int): верхняя граница диапозона подбора.
            count (int): текущее значение количества попыток.

        Returns:
            int: число попыток
        """
        
        count += 1
        predict_number = np.random.randint(number_first, number_last + 1)
        
        if number == predict_number:
            return count
        elif number < predict_number:
            return optimal_selection(number, number_first, predict_number - 1, count)
        else:
            return optimal_selection(number, predict_number + 1, number_last, count)
        
    count = optimal_selection(number, 1, 100, count)
    
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