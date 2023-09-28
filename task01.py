"""
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
"""

txt = input()
cnt = 0
max_cnt = 0
start_ch = " "
for ch in txt:
    if ch == start_ch:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 0
print("Максимальное количество последовательных пробельных символов:", max_cnt)
