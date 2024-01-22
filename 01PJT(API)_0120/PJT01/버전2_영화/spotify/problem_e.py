import json

def dec_artists(artists):
    dec_artists = []

    for artist in artists:
        id = artist['id']
        artist_detail = json.load(open(f'data/artists/{id}.json', encoding='utf-8'))
        total = int(artist_detail['followers']['total'])

        if total >= 10000000:
            dec_artists.append({
                'name' : artist_detail['name'],
                'uri-id' : artist_detail['uri'].split(':')[2]
            })

    return dec_artists

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
