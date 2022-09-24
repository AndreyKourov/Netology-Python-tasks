documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


#### p  - спросит номер документа и выведет имя человека, которому он принадлежит
def get_doc(doc):
    dogi = {}
    input_p = input('ФИО P.Введите номер документа: ')
    for doc_from_list in doc:
        if doc_from_list['number'] == input_p:
            dogi = doc_from_list
            print(dogi['name'])


#### s  -  спросит номер документа и выведет номер полки, на которой он находится;
def get_direct(direct):
    input_dir = (input('Полка S. Введите номер додокумента: '))
    for key_dict, val_dict in direct.items():
        for list_val_dict in val_dict:
            if list_val_dict == input_dir:
                print(f'Введенный документ находится на полке: {key_dict}')


#### l  -  выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
def get_list(doc):
    for k in doc:
        print(k["type"], k["number"], k["name"])


#### a  -  обавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_doc(doc, direct):
    inp_type = input('Введите тип документа: ')
    inp_number = input('Введите номер документа: ')
    inp_name = input('Введите имя владельца: ')
    inp_shelf = input('Введите полку: ')
    documents.append({"type": inp_type, "number": inp_number, "name": inp_name})
    if inp_shelf == '1':
        directories['1'].append(inp_number)
    elif inp_shelf == '2':
        directories['2'].append(inp_number)
    elif inp_shelf == '3':
        directories['3'].append(inp_number)
    else:
        print('Вы указали не существующую полку')
    print(documents)
    print(directories)

####  d   -  УДАЛЕНИЕ ПО НОМЕМУ ДОКУМЕНАТ
def def_del_doc_dir(doc, direct):
    del_number = input('Введите номер документа: ')
    for list in doc:
        for k, v in list.items():
            if del_number == v:
                list.clear()
                print(doc)
                break
    for k_test_doc, v_test_dir in direct.items():
        for number_in_value in v_test_dir:
            if del_number == number_in_value:
                v_test_dir.remove(number_in_value)
                print(direct)
                break


####  m  -   спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
def move_date(direct):
    move_number = input('Введите номер документа: ')
    move_shelf = input('Введите номер полки: ')
    try:
        direct[move_shelf]
    except KeyError:
        print('Вы ввели не существующую полку')
        return
    exist = False
    for key in direct:
        if move_number in direct[key]:
            direct[key].remove(move_number)
            direct[move_shelf].append(move_number)
            print(direct)
            exist = True
            break
    if exist == False:
        print('Вы ввели не существующий документ')


#####  as  - спросит номер новой полки и добавит ее в перечень.
def add_shelf(direct):
    number_new_shelf = input('Введите номер новой полки: ')
    new_list_in_new_shelf = []
    if number_new_shelf in directories:
        print('Такая полка уже существует')
    else:
        directories[number_new_shelf] = new_list_in_new_shelf
        print(directories)


def user_cmd (doc , direct):
    while True:
        user_input = input('Введите комманду: ')
        if user_input == 'p':   # people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
            get_doc(doc)
        ##
        elif user_input == 's':   # shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
            get_direct(direct)
        ##
        elif user_input == 'l':   # list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
            get_list(doc)
        ##
        elif user_input == 'a':   # add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
            add_doc(doc, direct)
        ##
        elif user_input == 'd': # УДАЛЕНИЕ ПО НОМЕМУ ДОКУМЕНАТ
            def_del_doc_dir(doc, direct)
        ##
        elif user_input == 'm': #  m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
            move_date(direct)
        ##
        elif user_input == 'as': # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
            add_shelf(direct)
        ##
        elif user_input == 'q':
            break

user_cmd(documents, directories)
