import json
from pprint import pprint

with open('newsafr.json') as f:
    json_data = json.load(f)


json_value = json_data['rss']['channel']['items']

# Получаем все слова из нашего json
def description(json_value):
    for list_json in json_value:
        for k_json, val_json in list_json.items():
            if k_json == 'description':
                list_desc_json = val_json

    global split_list_desc_json
    split_list_desc_json = list_desc_json.split()
    # print(split_list_desc_json)

description(json_value)

# Получаю все слова в которых букв больше 6
def list_6_world(split_list_desc_json):
    global list_6_world
    list_6_world = []
    for found_count in split_list_desc_json:
        if len(found_count) > 6:
            list_6_world.append(found_count)
    # print(list_6_world)

list_6_world(split_list_desc_json)

# Ищем слова которые повторяются 10 раз
def ten_words(list_6_world):
    ten_words = {}
    for x in list_6_world:
        if ten_words.get(x, 'w') != 'w':
            ten_words[x] += 1
        else:
            ten_words[x] = 1

    for key, val in ten_words.items():
        if val == 10:
            print(key)
        else:
            print('Нет 10 похожих слов')
            break

ten_words(list_6_world)

'''
d = {}
for x in list_6_world:
    try:
        d[x] +=1
    except KeyError:
        d[x] = 1

print(d)
'''
