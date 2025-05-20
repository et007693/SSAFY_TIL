import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    params = {
        'q' : '',
        'type' : 'artist',
        'market': 'KR',
        'limit': 1,
    }
    params['q'] = f'artist:{name}'
    response = requests.get(f'{URL}/search', headers=headers, params=params).json()

    try:
        singer_id = response['artists']['items'][0]['id']

        url = f'/artists/{singer_id}/related-artists'
        response = requests.get(f'{URL}{url}', headers=headers).json()
        related_artists = [artist['name'] for artist in response.get('artists', [])]

        return related_artists
   
    except:

        return



if __name__ == '__main__':

    pprint(get_related_artists("NewJeans"))

    pprint(get_related_artists("OldShirts"))