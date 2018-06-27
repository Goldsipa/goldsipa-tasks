# -*- coding: utf-8 -*- 


def have_same_items(list1, list2):
    """ Проверяет состоят ли массивы list1 и list2 из одинакового
        числа одних и тех же элементов

        Parameters
        ----------
        list1 : list[int]
            отсортированный по возрастанию массив уникальных элементов
        list2 : list[int]
            массив произвольной длинны произвольных чисел

        Returns
        -------
        bool
    """
    list2 = sorted(list2)           # сортируем второй массив

    if(list1 == list2):            # проверяем одинаковость массивов
        return True
    else:
        return False