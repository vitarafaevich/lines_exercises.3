"""
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
"""

import keyword
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lttr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
smb = "_"
txt = input()
text = txt.split()

if txt[0].isalpha() and txt != keyword:
    for i in range(len(text)):
        if txt.isalpha():
            if i in num or i in lttr or i in smb:
            print("подходит")
        else:
            print("неподходит")