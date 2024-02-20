# Задача: Написать программу, которая из имеющегося массива строк 
# формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте 
# выполнения алгоритма. 
# При решении не рекомендуется пользоваться коллекциями, 
# лучше обойтись исключительно массивами.

def add_array(txt_arr, n):
    i = 0
    while i < n:
        txt = input()
        if txt != 'q':
            txt_arr.append(txt)
        else:
            return txt_arr
        i += 1
    return txt_arr

def search_three(txt_arr):
    new_txt_arr = []
    for element in txt_arr:
        if len(element) <= 3:
            new_txt_arr.append(element)
    return new_txt_arr

print("pls insert value array:")
n = int(input())
print("Insert text or 'q' for end:")
txt_arr = []
txt_arr = add_array(txt_arr, n)
new_arr = search_three(txt_arr)
print([l for l in new_arr])