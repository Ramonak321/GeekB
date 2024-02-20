1. Ввод длины массива
```
print("pls insert value array:")
n = int(input())
```
2. Ввод данных массива1
`print("Insert text or 'q' for end:")`
3. В функции **add_array** читаем вводимые данные в массив до тех пор пока не будет введено *'q'* или не будет достигнут указанный выше предел массива
```
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
```
4. В функции **search_three** выполняем поиск элементов с длиной 3 и менее и выводим новую функцию
```
def search_three(txt_arr):
    new_txt_arr = []
    for element in txt_arr:
        if len(element) <= 3:
            new_txt_arr.append(element)
    return new_txt_arr
```
5. Выводим результат новой функции на экран
`print([l for l in new_arr])`