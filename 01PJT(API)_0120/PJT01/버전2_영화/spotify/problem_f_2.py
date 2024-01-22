"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint

def acoustic_artists():
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    artists = []

    for artist in artists_list:
        genres_names = []
        for id in artist['genres_ids']:
            for genre in genres_list:
                if genre['id'] == id:
                    genres_names.append(genre['name'])
        if 'acoustic' in genres_names:
            artists.append(artist['name'])

    return artists

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())
