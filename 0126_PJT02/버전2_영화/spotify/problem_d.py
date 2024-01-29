import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
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



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_related_artists("NewJeans"))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists("OldShirts"))
    # None
