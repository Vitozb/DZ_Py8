def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите Фамилию ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('Введите Фамилию ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('Введите Фамилию ')
            print(delete_by_lastname(phone_book,lastname))
            phone_book=read_txt('phonebook.txt')
        elif choice==5:
            number=input('Введите номер абонента: ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('Введите Фамилию Имя Отчество Телефон Описание через пробел ')
            add_user(phone_book,user_data)
            write_txt('phonebook.csv',phone_book)
        choice=show_menu()





def show_menu():
    print('1. Распечатать справочник\n'
    '2. Найти телефон по фамилии\n'
    '3. Изменить номер телефона\n'
    '4. Удалить запись\n'
    '5. Найти абонента по номеру телефона\n'
    '6. Добавить абонента в справочник\n'
    '7. Закончить работу')
    choice=int(input())
    return choice

def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    with open('phonebook.csv','r',encoding='utf-8') as phb:
        for line in phb:
            record=dict(zip(fields,line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename,phone_book):
    with open('phonebook.csv','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    for record in phone_book:
        print(', '.join(record.values()))

def find_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            return(f"Телефон: {record['Телефон']}"'\n')

    return "Телефон не найден"

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            write_txt('phonebook.csv', phone_book)
            return "Номер телефона успешно изменен\n"
    return "Фамилия не найдена"

def delete_by_lastname(phone_book, last_name):
    removed = False
    updated_phone_book = []
    
    for record in phone_book:
        if record['Фамилия'] != last_name:
            updated_phone_book.append(record)
        else:
            removed = True
    
    if removed:
        write_txt('phonebook.csv', updated_phone_book)
        return f"Запись с фамилией '{last_name}' удалена\n"
        
    return f"Запись с фамилией '{last_name}' не найдена\n"


def find_by_number(phone_book, number):
    for record in phone_book:
        if record['Телефон'] == number:
            return f"Абонент: {record['Фамилия']} {record['Имя']} {record['Отчество']}\n"
    return "Абонент с таким номером не найден\n"

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    print(user_data)
    new_record = dict(zip(fields, user_data.strip().split(' ')))
    print(new_record)
    phone_book.append(new_record)
    write_txt('phonebook.csv', phone_book)
    print("Новый абонент успешно добавлен\n")




work_with_phonebook()