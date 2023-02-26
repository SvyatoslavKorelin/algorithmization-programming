# encoding=utf-8
# сложность 0(n)

def maxProfit(prices): # на вход подаются цены в зависимости от дня
    max_profit = 0 # прибыли изначально нет

    if prices is None: # если цен нет, то и прибыли нет (защита от пустого ввода)
        return max_profit

    for i in range(1, len(prices)): # перебор от 1 (питон считает с 0 по умолчанию), до максимального количества дней (макс колич дней = колич цен)
        if prices[i] > prices[i - 1]: # если текущая цена больше цены предыдущего дня
            max_profit += prices[i] - prices[i - 1] # прибыль = затраты - расходы

    return max_profit # возврат максимального заработка

print(maxProfit([7,1,5,3,6,4]))