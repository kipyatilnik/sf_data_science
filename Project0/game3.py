"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Случайно угадавыаем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
        
    def optimal_selection(number,num_first,num_last,count) -> int:
        count+=1
        predict_number = np.random.randint(num_first,num_last+1) # предполагаемое число
        if number == predict_number:
            return(count)
        elif number < predict_number:
#            print(f"cur_count:{count} cur_number:{number} cur_predict_number{predict_number} cur_num_first{num_first} cur_num_last{num_last}")
            return(optimal_selection(number,num_first,predict_number-1,count))
        else:
#            print(f"cur_count:{count} cur_number:{number} cur_predict_number{predict_number} cur_num_first{num_first} cur_num_last{num_last}")
            return(optimal_selection(number,predict_number+1,num_last,count))
    count = optimal_selection(number,1,100,count)
    return(count)
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за:{score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)