def main_menu():
    print('Меню:\n 1 - Просмотр книги\n 2 - Добавить контакт\n 3 - Найти контакт\n 4 - Изменить контакт\n 0 - выход')
    menu = int(input())
    if menu == 1:
        open_book()
    elif menu == 2:
        add_contact()
    elif menu == 3:
        print("Выбор условия:\n 1 - Поиск по Фамилии\n 2 - Поиск по имени\n 3 - Поиск по телефону\n 0 - Назад")
        var_search = int(input())
        search_menu(var_search)
    elif menu ==4:
        print("Выбор условия:\n 1 - Удалить контакт\n 2 - Скопировать контакт\n 0 - Назад")
        var_search = int(input())
        if var_search == 1:
            delete_contact()
        elif var_search == 2:
            copy_contact()
        else:
            return main_menu
    elif menu == 0:
        bye = [print("Adios")]
        return bye
    else:
        print("Введены неверные данные повторите")
    main_menu()

def open_book():
    print("Фамилия \t Имя \t\t Телефон")
    with open("phonebook.txt", 'r', encoding="utf-8") as phonebook:
        book = phonebook.readlines()
        for line in book:
            print(line.strip("\t"))
    phonebook.close

def add_contact():
    with open("phonebook.txt", "a+", encoding="utf-8") as book:
        print("Введите Фамилию, Имя и Телефон через ПРОБЕЛ")
        line = str(input())
        for l in line.split(" "):
            book.write(l + '\t\t')
        book.write("\n")
    book.close

def search_menu(x):
    if x == 0:
        return main_menu()
    print("Ввведи даные для поиска: ")
    srh = str(input())
    with open("phonebook.txt", 'r', encoding="utf-8") as phonebook:
        book = phonebook.readlines()
        for line in book:
            if srh in line:
                print(line.strip("\t"))
    phonebook.close

def delete_contact():
    print("ID \t Фамилия \t Имя \t\t Телефон")
    with open("phonebook.txt", 'r', encoding="utf-8") as phonebook:
        book = phonebook.readlines()
        i = 0
        for line in book:
            i += 1
            print(i, end="\t")
            print(line.strip("\t"))
    print("Введите ID удаляемого контакта: ")
    id = int(input())
    book.pop(id - 1)
    with open("phonebook.txt", 'w', encoding="utf-8") as phonebook:
        phonebook.writelines(book)

def copy_contact():
    print("ID \t Фамилия \t Имя \t\t Телефон")
    with open("phonebook.txt", 'r', encoding="utf-8") as phonebook:
        book = phonebook.readlines()
        i = 0
        for line in book:
            i += 1
            print(i, end="\t")
            print(line.strip("\t"))
    print("Введите ID копируемого контакта: ")
    id = int(input())
    with open("phonebook2.txt", "a+", encoding="utf-8") as book2:
        book2.write(book[id-1])
        book2.write('\n')
    book2.close

                    
    


main_menu()
        
