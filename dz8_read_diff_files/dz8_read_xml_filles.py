import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='UTF-8')

tree = ET.parse('newsafr.xml', parser)

root = tree.getroot()

xml_desc = root.findall("channel/item/description")

''''''
# Создаем список из слов ( используем  split  что бы из СТРОКИ сделать СПИСОК из слов )
def split_desc_xml(xml_desc):
    global split_worlds
    for desc in xml_desc:
        split_worlds = desc.text.split()
    # print(split_worlds)

split_desc_xml(xml_desc)

# Фильтруем и получаем список только из тех слов в которых больше 6 букв
def list_6_worlds(split_worlds):
    global list_6_worlds
    list_6_worlds = []
    for desc in split_worlds:
        if len(desc) > 6:
            list_6_worlds.append(desc)
    # print(list_6_worlds)

list_6_worlds(split_worlds)

# Создаем словарь где ключь - это слово, а значение это колл-во сколько оно встречается.
# Затем сравниваем сколько раз видно это слово и выводим только те что встречаются 10 раз
def ten_words(list_6_worlds):
    ten_words = {}
    for x in list_6_worlds:
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

ten_words(list_6_worlds)