import requests
from pprint import pprint

# токен выглядит https://oauth.vk.com/blank.html#access_token=БЕРЕТСЯ ТОЛЬКО ЭТА ЧАСТЬ ОСТАЛЬНОЕ НЕ НУЖНО&expires_in=86400&user_id=16273871&state=123456
token = 'ТУТ УКАЗЫВАЕТСЯ ТОКЕН . ПРИМЕР ТОКЕНА ВЫШЕ'

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token' : self.token,
            'v' : self.version
        }
        self.owner_id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']

    def get_followers(self, user_id = None):
        if user_id is None:
            user_id = self.owner_id
        followers_url = self.url + 'friends.get'
        followers_params = {
            'count' : 1000,
            'user_id' : user_id
        }
        res = requests.get(followers_url, params={**self.params, **followers_params})
        return res.json()

vk_client = VkUser(token, '5.131')
# pprint(vk_client.get_followers()) ['response']['items']
followers_list = vk_client.get_followers()['response']['items']
followers_list2 = vk_client.get_followers('54618709')['response']['items']

# pprint(followers_list)
# pprint(followers_list2)

same_follower_list = list(set(followers_list) & set(followers_list2) )
pprint(same_follower_list)





