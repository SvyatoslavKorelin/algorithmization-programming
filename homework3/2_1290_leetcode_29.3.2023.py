# encoding=utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Создаем указатель и приравниваем ему head
        f = head
        # Создаем пустую строку для двоичных
        stroka = ''
        # Пока указатель не равен None
        while f != None:
            # Преобразуем значение узла в строку и добавим его к строке
            stroka += str(f.val)
            # Переходим к следующему узлу списка
            ptr = f.next
        # Преобразование с возвратом
        return int(stroka, 2)
