# Задача: Написать программу, которая из имеющегося массива строк 
# формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте 
# выполнения алгоритма. 
# При решении не рекомендуется пользоваться коллекциями, 
# лучше обойтись исключительно массивами.

def add_array(n):
    i = 0
    while i < n:
        txt = input()
        if txt != 'q':
            txt_arr[i] = txt
        else:
            return txt_arr
        i += 1
    return txt_arr

def search_three(txt_arr):
    for i in txt_arr:
        if len(txt_arr[i]) == 3:
             txt_arr[i]
        i += 1

print("pls insert value:")
n = input()
print("Insert text or q:")
txt_arr = []
txt_arr = add_array(n)
print(search_three())