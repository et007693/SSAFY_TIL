import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def ranking():
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
        # music_list.append([music['name'], music['album']['release_date']]) # 노래 제목, 발매일
        music_list.append(music['album']['release_date'])

    # 발매일 기준으로 sort한 list에서 노래 제목 추출
    # music_list = [music[0] for music in sorted(music_list, key = lambda x : x[1], reverse=True)] 
    music_list.sort(reverse=True)
    return music_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    ['2023-06-09', '2023-05-22', '2023-05-12', '2023-05-08', '2023-05-01']
    """
