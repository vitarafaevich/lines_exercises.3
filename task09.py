"""
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
"""

txt = input()
text = txt.split()
for i in text:
    if text.count(i) == 2:
        print(i)
        break
