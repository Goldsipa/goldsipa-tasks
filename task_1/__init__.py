# -*- coding: utf-8 -*- 


def fill_spiral_matrix(n):
    """ Создает мартицу размером n * n и заполняет ее по спирали

    Parameters
    ----------
    n : int
        Размерность матрицы.
    
    Variables
    ---------
    dx, dy : int
        Начальные приращения/начальный вектор
    x, y : int
        Начальная позиция

    Returns
    -------
    list[list[int]]
        Матрица заполненная по спирали
    """

    dx,dy = 0,1
    x,y = 0,0

    result = [[None]* n for j in range(n)]

    for i in range(1, n**2+1):          # цикл для заполнения матрицы
        result[x][y] = i
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and result[nx][ny] == None:          # индекс в пределах матрицы и не на занятой ячейке
            x,y = nx,ny
        else:
            dx,dy = dy,-dx          # изменяем направление вектора на 90 градусов
            x,y = x+dx, y+dy

    return result
