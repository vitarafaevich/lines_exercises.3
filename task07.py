"""
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
"""

txt = input()


def lnght(txt):
    return min(len(i) for i in txt.split())


text = lnght(txt)
print("Длина самого короткого слова в предложении:", text)
