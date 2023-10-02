"""
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
в слове нет повторяющихся букв и это слово симметрично.
"""

txt = input()
text = txt.split()
first_wrd = text[0]

excl_wrd = set(text)
for i in excl_wrd:
    if i != first_wrd:
        print(i)
