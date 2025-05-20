import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_tracks():
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    params = {
        'q' : 'genres:"k-pop"',
        'type' : 'track',
        'market': 'KR',
        'limit': 20,
    }

    music_list = []
    
    response = requests.get(f'{URL}/search', headers=headers, params=params).json()

    for music in response['tracks']['items']:
        music_list.append(music['name'])

    return music_list

if __name__ == '__main__':
    """
    장르가 k-pop인 음악트랙 20개 가져오기
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_tracks())
    """
    ['Cupid - Twin Ver.',
    'Take Two',
    'Like Crazy',
    'MONEY',
    'OMG',
    'Like Crazy',
    'Ditto',
    'Bite Me',
    'FLOWER',
    'UNFORGIVEN (feat. Nile Rodgers)',
    'Super',
    'Hype Boy',
    'The Planet',
    'Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]',
    'Like Crazy (English Version)',
    'Cupid',
    'Run BTS',
    'Eve, Psyche & The Bluebeard’s wife',
    'Tally',
    'Spicy']
    """
