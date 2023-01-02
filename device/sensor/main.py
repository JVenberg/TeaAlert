import os
import requests


API_KEY = os.environ.get('API_KEY')
PROJECT_ID = os.environ.get('PROJECT_ID')
TOKEN_REFRESH_URL = f'https://securetoken.googleapis.com/v1/token?key={API_KEY}'
REALTIME_DB_URL = f'https://{PROJECT_ID}.firebaseio.com'


def refresh_token():
    with open('/data/token', 'r') as f:
        token = f.read().strip()
    json_res = requests.post(TOKEN_REFRESH_URL, json={
        'grant_type': 'refresh_token',
        'refresh_token': token,
    }).json()
    refresh_token, access_token, uid = json_res['refresh_token'], json_res['access_token'], json_res['user_id']
    with open('/data/token', 'w') as f:
        f.write(refresh_token)
    return uid, access_token


def write_temp(token, uid, temp):
    json_res = requests.post(f'{REALTIME_DB_URL}/temperature/{uid}.json?auth=' + token, json={
        'temperature': temp,
        'timestamp': {'.sv': 'timestamp'},
    }).json()
    print(json_res)


uid, token = refresh_token()
for i in range(10):
    write_temp(token, uid, i)
