# import math
# import pprint
# from typing import Tuple

# print('Hello World!')


# def foo(x: int) -> Tuple[int, float]:
#     return x, math.pi


# pprint.pprint('Hello')

# print(foo(4))


############

# import requests

# api_url = 'http://numbersapi.com/43'

# response = requests.get(api_url)

# if response.status_code == 200:
#     print(response.text)

# else:
#     print(response.status_code)

##########

import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '' # ваш токен
TEXT = 'Ура, классный апдейт!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attemp =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1