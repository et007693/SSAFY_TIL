import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def ranking():
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
        # music_list.append([music['name'], music['album']['release_date']]) # 노래 제목, 발매일
        music_list.append(music['album']['release_date'])

    # music_list = [music[0] for music in sorted(music_list, key = lambda x : x[1], reverse=True)] 
    music_list.sort(reverse=True)
    return music_list


if __name__ == '__main__':

    pprint(ranking())
