from .models import IGDBGame, Genre
from rest_framework import serializers


class IGDBGenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = ['name']


class IGDBGameSerializer(serializers.ModelSerializer):

	class Meta:

		model = IGDBGame
		fields = ['id','name','hypes','popularity',
					'aggregated_rating', 'time_to_beat']

	def create(self, validated_data):

		game = IGDBGame.objects.create(**validated_data)
		genres = self.get_genres(validated_data['genres'])
		for genre in genres:
			game.genres.add(genre)
		return blogs

	def get_genres(self, genre_id_list):

		genres = []

		for id in genre_id_list:

			header = {'user-key': '9c3039ea4ad4cb83bfb126100764c483',
                      'Accept': 'application/json'
			}

			url = 'https://api-endpoint.igdb.com/genres/{}?fields=name'.format(id)
			data = requests.get(url, headers=header)
			ndata = data.json()

			genre = Genre(
                id=int(ndata[0]['id']),
                name=ndata[0]['name']
            )
			genre.save()
			genres.append(genre)

		return genres