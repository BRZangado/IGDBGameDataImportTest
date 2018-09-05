from .models import IGDBGame, Genre
from rest_framework import serializers


class IGDBGenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = '__all__'


class IGDBGameSerializer(serializers.ModelSerializer):

	genres = IGDBGenreSerializer(read_only=True, many=True)

	class Meta:

		model = IGDBGame
		fields = ['id','name','hypes','popularity',
					'aggregated_rating', 'time_to_beat', 'genres']