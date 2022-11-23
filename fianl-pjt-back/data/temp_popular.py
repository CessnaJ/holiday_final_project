# 초기 데이터 생성을 위한 파일

import json
import requests
from secret import TMDB_API_KEY
# git ignore처리함.


movies = []
base_tmdb_url = 'https://api.themoviedb.org/3/movie/popular'

for page in range(1,2):
    params = {'api_key': TMDB_API_KEY,
        'language': 'ko-KR',
        'page': page
        }

    result = requests.get(base_tmdb_url, params=params)
    data = result.json()['results']

    for object in data:
        if object.get('poster_path'):
            if object.get('adult') == False:
                movie = {
                    'model': 'movies.popular',
                    'pk': object.get('id'),
                    'fields': {
                        # 'genres': object.get('genre_ids'),
                        'title': object.get('title'),
                        'original_title':object.get('original_title'),
                        'overview': object.get('overview'),
                        'poster_path': object.get('poster_path'),
                        'release_date': object.get('release_date'),
                        'vote_count': object.get('vote_count'),
                        'vote_average': object.get('vote_average'),
                        'backdrop_path': object.get('backdrop_path')
                    }
                }
                movies.append(movie)
    movies.sort(key=lambda x: x['fields']['vote_count'], reverse=True)


with open('temp_populardata.json', 'w', encoding='utf-8') as file:
	json.dump(movies, file, ensure_ascii=False)