# encoding=utf-8
def numIslands(grid):
    # Определение вспомогательной функции для выполнения поиска в глубину на карте
    def w(i, j):
        # Проверка на граничные условия
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return 0
        # Отметить текущую ячейку как посещенную
        grid[i][j] = '0'
        # Рекурсивный вызов функции поиска в глубину на соседних ячейках
        w(i+1, j)
        w(i-1, j)
        w(i, j+1)
        w(i, j-1)
    # Получение размера карты
    m = len(grid)
    n = len(grid[0])
    # подсчет островов изначально 0
    count = 0
    # Обход всей карты и выполнение поиска в глубину на непосещенных ячейках с землей
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                w(i, j)
    # Возврат количества островов
    return count