"""
Задание 13.
Дима часто пользуется общественным транспортом и всегда проверяет номер билета,
является ли он "счастливым". Счастливым считается билет, имеющий в номере четное
количество цифр. Причем,  сумма цифр первой половины номера равна сумме цифр
второй половины.  Программа на вход получает  последовательность номеров билетов.
Ввод номеров должен завершить тогда, когда будет введен "счастливый" билет.
Программа должна вывести его порядковый номер. Счет начинается с 1.
"""


def tckt(ticket):
    if len(ticket) % 2 == 0:
        first_p = ticket[:len(ticket)//2]
        sm_first = sum([int(digit) for digit in first_p])
        second_p = ticket[len(ticket) // 2:]
        sm_second = sum([int(digit) for digit in second_p])
        return sm_first == sm_second


tickets = []
while True:
    ticket = input()
    tickets.append(ticket)
    if tckt(ticket):
        break

for i, ticket in enumerate(tickets, start=1):
    if tckt(ticket):
        print(i)
