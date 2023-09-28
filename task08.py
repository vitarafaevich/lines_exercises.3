"""
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
"""

txt = input()
text = txt.split()


def lnght(text):
    return sorted(text, key=len)


a = lnght(text)
for i in range(len(a)):
    print(a[i])
