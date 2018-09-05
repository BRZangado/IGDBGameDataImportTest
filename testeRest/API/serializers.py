from importdata.models import IGDBGame, Genre
from rest_framework import serializers


class IGDBGenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = ['name']


class IGDBGameSerializer(serializers.ModelSerializer):

	genres = serializers.SlugRelatedField(
		read_only=True,
		many=True,
		slug_field='name'
	)

	class Meta:

		model = IGDBGame
		fields = ['id','name','hypes','popularity',
					'aggregated_rating', 'time_to_beat', 'genres']