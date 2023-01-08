import os
import urequests


API_KEY = 'AIzaSyCiSr9kP46zvq8PbJHOqX95LXRXpsX7RMc'
PROJECT_ID = 'tea-alert-default-rtdb'
TOKEN_REFRESH_URL = f'https://securetoken.googleapis.com/v1/token?key={API_KEY}'
REALTIME_DB_URL = f'https://{PROJECT_ID}.firebaseio.com'

print(TOKEN_REFRESH_URL)


def refresh_token():
    token_file = open('data/token', 'r')
    token = token_file.read().strip()
    token_file.close()

    json_res = urequests.post(TOKEN_REFRESH_URL, json={
        'grant_type': 'refresh_token',
        'refresh_token': token,
    }).json()
    refresh_token, access_token, uid = json_res['refresh_token'], json_res['access_token'], json_res['user_id']

    token_file = open('data/token', 'w')
    token_file.write(refresh_token)
    token_file.close()

    return uid, access_token


def write_temp(token, uid, temp):
    json_res = urequests.post(f'{REALTIME_DB_URL}/temperature/{uid}.json?auth=' + token, json={
        'temperature': temp,
        'timestamp': {'.sv': 'timestamp'},
    })
    print('Test', json_res)
    json_res = json_res.json()
    return json_res
