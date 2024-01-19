import json

def max_polularity(artists):
    name = []
    popularity = []

    for artist in artists:
        id = artist['id']
        artist_detail = json.load(open(f'data/artists/{id}.json', encoding='utf-8'))
        name.append(artist_detail['name'])
        popularity.append(artist_detail['popularity'])

    best = name[popularity.index(max(popularity))]
    return best

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
