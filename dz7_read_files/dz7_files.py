cook_book = {
    'name_of_the_dish' : [
        {'ingredient_name': '', 'quantity': 0, 'measure': ''}
    ]
}
d = {}
with open('file.txt', 'r') as f:
    # for l in f:
    #     print(l.strip())

    list_readlines = f.readlines()
    cook_book = { list_readlines[0].strip() : [ {'ingredient_name': list_readlines[2].strip(), 'quantity': list_readlines[3].strip(), 'measure': list_readlines[4].strip()} ] }
    print(cook_book)
    print(list_readlines)

    for key, value in cook_book.items():
        for list_value in value:
            print(value)
