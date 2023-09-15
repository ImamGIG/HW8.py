# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def interface_contact(phone_list_name_file = 'phonebook.txt'):
    interface_contact = int(input('Введите 1 для поиска \nВведите 2 для добавления контакта \nВведите 3 для изменеия контакта \nВведите 4 для удаления контакта \nВведите 5 для вывода всех контактов \nВведите 0 для выхода:\n'))
    while interface_contact != 0:
        if interface_contact == 1:
            find_contact()
        elif interface_contact == 2:
            write_contact()
        elif interface_contact == 3:
            update_contact()
        elif interface_contact == 4:
            delete_contact()
        else:
            print_contacts()
            print()
        interface_contact = int(input('\nВведите 1 для поиска \nВведите 2 для добавления контакта \nВведите 3 для изменения контакта \nВведите 4 для удаления контакта \nВведите 5 для вывода всех контактов \nВведите 0 для выхода:\n'))


def write_contact(phone_list_name_file = 'phonebook.txt'):
    with open(phone_list_name_file, 'a', encoding='UTF-8') as phone_list:
        last_name = input('Введите фамилию: ').title()        
        first_name = input('Введите имя: ').title()
        phone = input('Введите номер телефона в международном формате: ')
        while len(phone) != 11 or not phone.isdigit():
            print('Вы ввели неправильный телефон')
            phone = input('Введите номер телефона в международном формате (11 цифр): ')
        phone_list.write('\n' + last_name + ', ' +  first_name + ', ' +  phone)


def find_contact(phone_list_name_file = 'phonebook.txt'):
    with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list:
        find_name = input('Поиск: ').title()
        lines = phone_list.readlines()
        none_contact = True
        for i in lines:
            if find_name in i:
                print('Контакт найден:', i, end = '')
                none_contact = False
        if none_contact:
            print('Контакт не найден.')


def print_contacts(phone_list_name_file = 'phonebook.txt'):
    with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list:
        lines = phone_list.readlines()
        for i in lines:
            print(i, end = '')


def update_contact(phone_list_name_file = 'phonebook.txt'):
    last_name = input('Введите фамилию контакта, который хотите изменить: ').title()
    first_name = input('Введите имя контакта, который хотите изменить: ').title()
    with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list:
        lines = phone_list.readlines()
    found_contact = False
    for i in range(len(lines)):
        contact_data = lines[i].strip().split(',')
        contact_last_name = contact_data[0].strip()
        contact_first_name = contact_data[1].strip()
        if contact_last_name == last_name and contact_first_name == first_name:
            new_last_name = input('Введите новую фамилию контакта: ').title()
            new_first_name = input('Введите новое имя контакта: ').title()
            new_phone = input('Введите новый номер телефона контакта в международном формате: ')
            while len(new_phone) != 11 or not new_phone.isdigit():
                print('Вы ввели неправильный телефон')
                new_phone = input('Введите новый номер телефона контакта в международном формате (11 цифр): ')
            contact_data[0] = new_last_name
            contact_data[1] = new_first_name
            contact_data[2] = new_phone
            lines[i] = ', '.join(contact_data) + '\n'
            found_contact = True
            break
    if found_contact:
        with open(phone_list_name_file, 'w', encoding='UTF-8') as phone_list:
            phone_list.writelines(lines)
        print('Контакт успешно обновлен.')
    else:
        print('Контакт не найден.')


def delete_contact(phone_list_name_file = 'phonebook.txt'):
    find_name_1 = input('Введите фамилию контакта, который хотите удалить: ').title()
    find_name_2 = input('Введите имя контакта, который хотите удалить: ').title()
    with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list:
        lines = phone_list.readlines()
    with open(phone_list_name_file, 'w', encoding='UTF-8') as phone_list:
        contact_found = False
        for line in lines:
            contact = line.strip().split(', ')
            if (find_name_1 not in contact[0]) or (find_name_2 not in contact[1]):
                phone_list.write(line)
            else:
                contact_found = True
        if contact_found:
            print('Контакт успешно удален.')
        else:
            print('Контакт не найден.')


interface_contact()