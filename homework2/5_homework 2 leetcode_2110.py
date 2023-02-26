# encoding=utf-8
# сложность 0(n)
def decent_periods(price_and_day):
    v = len(price_and_day) #
    smooth = v # все элементы плавного спуска (длина плавного спуска 1)
    for i in range(1, v): # перебор
        a = i
        while a < v and price_and_day[a] == price_and_day[a - 1] - 1: # поиск плавных спусков
            a = a + 1
        smooth = smooth + (a - i) # прибавка найденных периодов плавного спуска
    return smooth

print(decent_periods([8, 6, 7, 7]))
