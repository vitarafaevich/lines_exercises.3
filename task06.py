"""
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
"""

txt = input()
text = txt.split()
text.reverse()
result = " ".join(text)
print(result)
