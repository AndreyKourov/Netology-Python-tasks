
with open('file.txt', 'r') as f:
    data = f.read()
    # print(data.split())

def omelet(file):
    file_list = file.split('\n')

    # egg = file_list[2].split(' | ')
    # milk = file_list[3].split(' | ')
    # tomato = file_list[4].split(' | ')
    # list_product = [egg, milk, tomato]

    # cook_book_1 = {}
    # while list_product[0] <= list_product[2]:
    #     i = 0
    #     i += 1
    #     cook_book_1 = {
    #         file_list[0]: [
    #             {'ingredient_name': list_product[i][0], 'quantity': list_product[i][1], 'measure': list_product[i][2]}
    #         ]
    #     }


    # for list_in_list in list_product:
    #     i = 0
    #     i = i + 1
    #     dict_oml = {'ingredient_name': list_in_list[i][0], 'quantity': list_in_list[i][1], 'measure': list_in_list[i][2]}
    #
    # cook_book_1 = {
    #     file_list[0]: [
    #         dict_oml
    #     ]
    # }
    # print(cook_book_1)

    # '''
    egg = file_list[2].split(' | ')
    dict_egg = {'ingredient_name': egg[0], 'quantity': egg[1], 'measure': egg[2]}

    milk = file_list[3].split(' | ')
    dict_milk = {'ingredient_name': milk[0], 'quantity': milk[1], 'measure': milk[2]}

    tomato = file_list[4].split(' | ')
    dict_tomato = {'ingredient_name': tomato[0], 'quantity': tomato[1], 'measure': tomato[2]}

    cook_book_1 = {
        file_list[0]: [
            dict_egg, dict_milk, dict_tomato
        ]
    }
    # print(cook_book_1)
    return cook_book_1

omelet(data)

def duck(file):
    file_list = file.split('\n')
    # print(file_list[6])
    duck_list = file_list[8].split('|')
    dick_duck = {'ingredient_name': duck_list[0], 'quantity': duck_list[1], 'measure': duck_list[2]}

    whater = file_list[9].split('|')
    dick_whater = {'ingredient_name': whater[0], 'quantity': whater[1], 'measure': whater[2]}

    honey = file_list[10].split('|')
    dick_honey = {'ingredient_name': honey[0], 'quantity': honey[1], 'measure': honey[2]}

    soy_sauce = file_list[11].split('|')
    dick_soy = {'ingredient_name': soy_sauce[0], 'quantity': soy_sauce[1], 'measure': soy_sauce[2]}

    cook_book_2 = {
        file_list[6]: [
            duck_list, dick_whater, dick_honey, dick_soy
        ]
    }
    # print(cook_book_2)
    return cook_book_2

duck(data)

def baked_potato(file):
    file_list = file.split('\n')
    # print(file_list)
    # print(file_list[13])
    potato = file_list[15].split('|')
    dick_potato = {'ingredient_name': potato[0], 'quantity': potato[1], 'measure': potato[2]}

    garlic = file_list[16].split('|')
    dick_garlic = {'ingredient_name': garlic[0], 'quantity': garlic[1], 'measure': garlic[2]}

    cheese = file_list[17].split('|')
    dick_cheese = {'ingredient_name': cheese[0], 'quantity': cheese[1], 'measure': cheese[2]}

    cook_book_3 = {
        file_list[13]: [
            dick_potato, dick_garlic, dick_cheese
        ]
    }
    # print(cook_book_3)
    return cook_book_3

baked_potato(data)

def fahitos(file):
    file_list = file.split('\n')
    # print(file_list[19])
    beef = file_list[21].split('|')
    dick_beef = {'ingredient_name': beef[0], 'quantity': beef[1], 'measure': beef[2]}

    pepper = file_list[22].split('|')
    dick_pepper = {'ingredient_name': pepper[0], 'quantity': pepper[1], 'measure': pepper[2]}

    lavash = file_list[23].split('|')
    dick_lavash = {'ingredient_name': lavash[0], 'quantity': lavash[1], 'measure': lavash[2]}

    wine = file_list[24].split('|')
    dick_wine = {'ingredient_name': wine[0], 'quantity': wine[1], 'measure': wine[2]}

    tomato = file_list[25].split('|')
    dick_tomato = {'ingredient_name': tomato[0], 'quantity': tomato[1], 'measure': tomato[2]}

    cook_book_4 = {
        file_list[19]: [
            dick_beef, dick_pepper, dick_lavash, dick_wine, dick_tomato
        ]
    }
    # print(cook_book_4)
    return cook_book_4

fahitos(data)

def cook_book(one_book, two_book, three_book, four_book):
    for key_omlete, val_omlete in one_book.items():
        name_omlet = key_omlete
        list_omlet = val_omlete

    for key_duck, val_duck in two_book.items():
        name_duck = key_duck
        list_duck = val_duck

    for key_potato, val_potato in three_book.items():
        name_potato = key_potato
        list_potato = val_potato

    for key_fahitos, val_fahitos in four_book.items():
        name_fahitos = key_fahitos
        list_fahitos = val_fahitos

    cook_book = {
        name_omlet : list_omlet,
        name_duck : list_duck,
        name_potato : list_potato,
        name_fahitos: list_fahitos
    }
    print(cook_book)

cook_book(omelet(data), duck(data), baked_potato(data), fahitos(data))
