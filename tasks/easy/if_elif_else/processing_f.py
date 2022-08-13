"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дана строка. В зависимости от того, сколько встречается в строке буква f,
выполнить следующие действия:
    - 0 раз: буквы нижнего регистра заменить на верхний, верхнего на нижний
    - 1 раз: вывести ее индекс
    - 2 раза: вывести индекс последнего вхождения
    - больше 2 раз: вернуть исходную строку задом-наперед

ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'Hello World' -> 'hELLO wORLD'
- 'hi-fi acoustic' -> 3
- 'fast forward' -> 5
- 'finish false fox' -> 'xof eslaf hsinif'
"""
from typing import Union


def processing_f(str_with_f: str) -> Union[int, str]:
    kol_f = str_with_f.count('f')
    if kol_f == 0:
        result = str_with_f.swapcase()
    elif kol_f == 1:
        result = str_with_f.find('f')
    elif kol_f == 2:
        result = str_with_f.rfind('f')
    else:
        result = str_with_f[::-1]
    return result


if __name__ == '__main__':
    string = input('Введите строку для работы: ')
    print(f"Результат: {processing_f(string)}")
