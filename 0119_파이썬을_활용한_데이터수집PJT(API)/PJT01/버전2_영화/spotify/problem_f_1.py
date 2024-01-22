"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    artists = []

    for artist in artists_list:
        id = artist['id']
        artist_detail = json.load(open(f'data/artists/{id}.json', encoding='utf-8'))
        total = int(artist_detail['followers']['total'])

        if 5000000 <= total < 10000000:
            artists.append({
                'name' : artist_detail['name'],
                'followers' : total
            })

    return artists

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
