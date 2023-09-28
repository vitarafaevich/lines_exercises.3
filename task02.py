"""
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
"""

txt = input()
max_cnt = 0
cnt = 0
start_ch = ""
for ch in txt:
    if ch == start_ch:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1
        start_ch = ch
print("Максимальное количество последовательных символов:", max_cnt)
