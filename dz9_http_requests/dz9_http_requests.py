import requests
from pprint import pprint

HEADERS = {'Authorization': '2619421814940190'}

# resp = requests.get('https://superheroapi.com/api/2619421814940190/')
# pprint(resp.json())
# resp.raise_for_status()
''''''
# Так можно было найти по id шнику
# resp1 = requests.get('https://superheroapi.com/api/2619421814940190/642')
resp_hulk_name = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
data_hulk = resp_hulk_name.json()['results']

resp_cap_name = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain America')
data_cap = resp_cap_name.json()['results']

resp_thanos_name = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')
data_thanous = resp_thanos_name.json()['results']


def cap_intelligence(data):
    for pwrstrs_cap in data:
        global cap_int
        cap_int = {}
        cap_int['Captain America'] = pwrstrs_cap['powerstats']['intelligence']
        return cap_int


def thanos_intelligence(data):
    for pwrstrs_thanos in data:
        global thanos_int
        thanos_int = {}
        thanos_int['Thanos'] = pwrstrs_thanos['powerstats']['intelligence']
        return thanos_int


def hulk_intelligence(data):
    hulk_dict = {}
    for d_h in data:
        hulk_dict[f'{d_h["name"]}'] = d_h['id']

    tru_hulk = ''
    for k , v in hulk_dict.items():
        if k == 'Hulk':
            tru_hulk = v

    resp_hulk_id = requests.get(f'https://superheroapi.com/api/2619421814940190/{tru_hulk}')
    global hulk_int
    hulk_int = {}
    hulk_int['Hulk'] = resp_hulk_id.json()['powerstats']['intelligence']
    return hulk_int


def dict_all_intelligence(hulk, cap, thanos):
    global all_dict
    all_dict = {}
    all_dict['Hulk'] = int(hulk['Hulk'])
    all_dict['Captain America'] = int(cap['Captain America'])
    all_dict['Thanos'] = int(thanos['Thanos'])

    x = max(all_dict, key=all_dict.get)
    print(f'{x} самый умный')

dict_all_intelligence(hulk_intelligence(data_hulk), cap_intelligence(data_cap), thanos_intelligence(data_thanous))