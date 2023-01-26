commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


def main_menu():
    print('Главное меню')
    for i, item in enumerate(commands, 1):
        print(f'\t {i}. {item}')
    choice = input('Выберите пункт меню: ')
    return choice
            
    

def information(massege:str):
    print(massege)


def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:15} {contact[2]:20}')
        print()


def create_new_contact():
    name = input('Введите ФИО :')
    phone = input('Введите телефон :')
    comment = input('Введите комментарий :')
    return name, phone, comment

def input_error():
    print('Введите корректный пункт меню')

def empty_request():
    print('Данный контакт не найден')

def many_request():
    print('Введите более точные данные ')

def select_contact(messege :str):
    contact = input(messege)
    return contact

def delete_confirm(contact:str):
    result=input(f'Вы действительно хотите удалить контакт {contact}? (y/n) ').lower()
    if result =='y':
        return True
    else:
        return False


def change_contact():
    print('Введите новые данные иначе нажмите Enter')
    name = input('Введите ФИО :')
    phone = input('Введите телефон :')
    comment = input('Введите комментарий :')
    return name, phone, comment


def find_contact():
    find = input('Введите элемент для поиска :')
    return find


def end_program():
    print('Программа завершенна ')
