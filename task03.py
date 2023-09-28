"""
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
"""

txt = input()
exclsv_ch = set(txt)
exclsv_ch = [i for i in exclsv_ch if i.isalpha() == True]
print("Количество различных букв в тексте:", len(exclsv_ch))
