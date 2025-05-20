import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    params = {
        # 'q' : '',
        'type' : 'track',
        'market': 'KR',
        'limit': 1,
    }

    # trakc_id
    params['q'] = f'track:{track}'
    response = requests.get(f'{URL}/search', headers=headers, params=params).json()
    track_id = response['tracks']['items'][0]['id']

    # artist_id
    params['q'], params['type'] = f'artist:{artist}', 'artist'
    response = requests.get(f'{URL}/search', headers=headers, params=params).json()
    artist_id = response['artists']['items'][0]['id']

    # # 추천 곡 뽑기 위한 parameter 설정
    recommend_list = []
    rec_params = {
        'seed_artists' : artist_id,
        'seed_tracks' : track_id,
        'seed_genres' : genre
    }
    response = requests.get(f'{URL}/recommendations', headers=headers, params=rec_params).json()
    for music in response['tracks']:
        recommend_list.append(music['name'])

    return recommend_list


if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('Hype Boy', 'BTS', 'acoustic'))
