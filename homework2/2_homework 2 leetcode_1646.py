# encoding=utf-8
# сложность 0(n)
def solution(n):
    spisok = [] # сюда заносятся значения
    for i in range(n + 1): # длина из условия
        if i == 0: # условие 1
            spisok.append(0)
        elif i == 1: # условие 2
            spisok.append(1)
        elif i % 2 == 0: # условие 3
            spisok.append(spisok[i//2])
        else:
            spisok.append(spisok[i//2] + spisok[(i // 2)+1]) # условие 4
    return max(spisok) # возврат максимального значения

print(solution(7))