"""
Задание 11.
Петя и Вася играют в игру "Города". Первым называет город Петя. Каждый следующий,
называемый город должен начинаться на ту букву, на которую окончился предыдущий.
Программа получает на вход строку, состоящую из слов (городов), разделенных пробелами,
которые называли игроки. В результате работы, программа должна определять имя победителя.
Игрок выигрывает, если он назвал слово последним. Однако, игрок проигрывает, если он
первым нарушил правила игры.
"""

txt = input()
text = txt.split()
victory = " "
first_wrd = text[0]
last_lttr = first_wrd[-1]

for i in range(len(text)):
    if text[i][0] == last_lttr:
        last_lttr = text[i][-1]
    else:
        if i % 2 != 0:
            victory = "Петя"
        else:
            victory = "Вася"
print(victory)
