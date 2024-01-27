import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_popular_tracks():
    # 여기에 코드를 작성합니다.
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
        if music['popularity'] >= 90:
            music_list.append(music['name'])
            
    
    return music_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_popular_tracks())
    """
    ['Cupid - Twin Ver.', 'Take Two', 'Like Crazy', 'MONEY', 'OMG', 'Like Crazy']
    """
