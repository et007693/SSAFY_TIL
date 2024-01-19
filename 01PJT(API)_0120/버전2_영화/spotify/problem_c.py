import json
from pprint import pprint

def artist_info(artists, genres):
    artist_info = []

    for artist in artists:
        genres_names = []
        for id in artist['genres_ids']:
            for genre in genres:
                if genre['id'] == id:
                    genres_names.append(genre['name'])

        artist_info.append({
            'id' : artist['id'],
            'name' : artist['name'],
            'images' : artist['images'],
            'type' : artist['type'],
            'genres_names' : genres_names,
                    })
        
    return artist_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
