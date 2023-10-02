"""
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
"""

txt = input()
exclsv_ch = set(txt)
cntr = 0
for i in exclsv_ch:
    if i.isalpha() == True:
        cntr += 1
print("Количество различных букв в тексте:", cntr)

