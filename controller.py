import view as v
import model as m


def start():
    choise = ''
    while choise != '8':
        choise = v.main_menu()
        match choise:
            case '1':
                m.open_file()
                v.information('\n Файл успешно открыт\n')
            case '2':
                m.save_file()
                v.information('\n Файл успешно сохранён\n')
            case '3':
                pb = m.get_phone_book()
                v.show_contacts(pb)
            case '4':
                new_contact = list(v.create_new_contact())
                m.add_new_contact(new_contact)
                v.information(f'\n Контакт {new_contact[0]} успешно создан\n')
            case '5':
                del_name = v.select_contact('Введите удаляемый контакт: ')
                contact = m.get_contact(del_name)
                if contact:
                    confirm = v.delete_confirm(contact[0][0])
                    if confirm:
                        m.delete_contact(contact[0])
                        v.information(f'\n Контакт {contact[0][0]} успешно удалён\n')
                elif contact ==[]:
                    v.empty_request()
                else:
                    v.many_request()
            case '6':
                name = v.select_contact('Введите изменяемый контакт: ')
                contact = m.get_contact(name)
                if contact:
                    changed_contact=v.change_contact()
                    m.change_contact(contact[1],list(changed_contact))
                    v.information(f'\n Контакт {contact[0][0]} успешно изменён\n')
                elif contact ==[]:
                    v.empty_request()
                else:
                    v.many_request()
            case '7':
                find = v.find_contact()
                result = m.search_contact(find)
                v.show_contacts(result)
            case '8':
                v.end_program()
                break
            case _:
                v.input_error()
        