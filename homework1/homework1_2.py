# encoding=utf-8

# программа принимает на вход количество команд. Если количсетво команд четное, то программа делит количество команд на 2 и команды играют 1 на 1.
# Если число команд нечетное, то одна команда автоматически переходит в следующий раунд. Количество матчей и команд высчитывается по формулам
# данным из условий. При это цикл повторяться пока команд не останется. После выводится число матчей
# сложность 4 дествия за 1 цикл 0(N)
def MatchCount(teams): # принимает на вход количество команд
    matches = 0 # количество матчей (копилка)
    if teams == 1: # защита от дурака (если будет введена одна команда)
        return 0 # если изначально всего одна команда то играть будет не с кем и матчей будет 0
    while teams > 1: # условие, что пока команд больше 1 будут выполняться действия ниже
        if teams % 2 == 0: # проверка четности
            teams = teams // 2 # делим на 2 количество команд т.к половина выбывает
            matches = matches + teams # количество матчей
        else: # не четное число
            teams = ((teams - 1) // 2) + 1 # формулы из условий задачи, если нечетное число команд (колич команд)
            matches = matches + (teams - 1) // 2 # формулы из условий задачи, если число команд нечетное (количество матчей)
    return matches # когда команды закончатся и играть будет некому выводим число матчей

print(MatchCount(13)) # запуск функции с заданным параметром









