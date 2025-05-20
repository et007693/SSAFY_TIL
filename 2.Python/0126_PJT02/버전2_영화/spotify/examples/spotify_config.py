"""
Spotify에 요청을 보내기 위한 Header파일
"""

import requests

API_URL = 'https://api.spotify.com/v1'
data = {
    'grant_type': 'client_credentials',
    'client_id': API_CLIENT_ID,
    'client_secret': API_CLIENT_SECRET,
}


def getHeaders():
    secure_key = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        data=data,
    ).json()
    # print('access token: ', secure_key.get('access_token'))

    access_token = secure_key.get('access_token')

    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    return headers
