"""
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
"""

txt_1, txt_2, txt_3 = input(), input(), input()
exclsv_ch = " "

for ch in txt_1:
    if ch not in txt_2 and ch not in txt_3:
        exclsv_ch = ch
        print(exclsv_ch)
for ch in txt_2:
    if ch not in txt_1 and ch not in txt_3:
        exclsv_ch = ch
        print(exclsv_ch)
for ch in txt_3:
    if ch not in txt_1 and ch not in txt_2:
        exclsv_ch = ch
        print(exclsv_ch)
