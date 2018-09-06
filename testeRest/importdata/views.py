import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets

from .models import IGDBGame, Genre
from .serializers import IGDBGameSerializerCreate, IGDBGameSerializerList

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IGDBGame.objects.all()
    serializer_class = IGDBGameSerializerList

class IgDBView(APIView):

    '''
            View that calls IGDB API
            and return some relevant
            information about a game
    '''

    def get(self, request, format=None):

        header = {'user-key': 'a3dd85f2cf6c0a5de9fdb6c927c40516',
                  'Accept': 'application/json'}
        url = 'https://api-endpoint.igdb.com/games/?fields=id,name,hypes,popularity,aggregated_rating,time_to_beat,genres,external&filter[rating][gte]=60&order=popularity:desc&limit=50&offset=0'
        data = requests.get(url, headers=header)
        ndata = data.json()

        for game_data in ndata:
            
            filtered_data = self.filter_data(game_data)
            self.save_games(filtered_data)

        return Response(data=ndata)


    def save_games(self, game_filtered_data):

        new_game = IGDBGame(
            id=game_filtered_data['id'],
            name=game_filtered_data['name'],
            hypes=game_filtered_data['hypes'],
            popularity=game_filtered_data['popularity'],
            aggregated_rating=game_filtered_data['aggregated_rating'],
            time_to_beat=game_filtered_data['time_to_beat'],
            external=game_filtered_data['external']
        )

        new_game.save()

        genres = self.get_genres(game_filtered_data['genres'])

        for genre in genres:
            new_game.genres.add(genre)

        new_game.save()

        print("Jogo Salvo com sucesso:" + new_game.name)

    def get_genres(self, genre_id_list):

        genres = []

        for id in genre_id_list:

            header = {'user-key': 'a3dd85f2cf6c0a5de9fdb6c927c40516',
                      'Accept': 'application/json'
                      }
            url = 'https://api-endpoint.igdb.com/genres/{}?fields=name'.format(
                id)
            data = requests.get(url, headers=header)
            ndata = data.json()

            genre = Genre(
                id=int(ndata[0]['id']),
                name=ndata[0]['name']
            )

            genre.save()

            genres.append(genre)

        return genres

    def filter_data(self, game_dict):

        if 'id' in game_dict:
            id = int(game_dict['id'])
        else:
            id = None

        if 'name' in game_dict:
            name = game_dict['name']
        else:
            name = None

        if 'hypes' in game_dict:
            hypes = int(game_dict['hypes'])
        else:
            hypes = None

        if 'popularity' in game_dict:
            popularity = float(game_dict['popularity'])
        else:
            popularity = None

        if 'aggregated_rating' in game_dict:
            aggregated_rating = float(game_dict['aggregated_rating'])
        else:
            aggregated_rating = None

        if 'time_to_beat' in game_dict:
            if 'normally' in game_dict['time_to_beat']:
                time_to_beat = float(game_dict['time_to_beat']['normally'])
            else:
                time_to_beat = None
        else:
            time_to_beat = None

        if 'external' in game_dict:
            external = game_dict['external']['steam']
        else:
            external = None

        filtered_data = {
            'id': id,
            'name': name,
            'hypes': hypes,
            'popularity': popularity,
            'aggregated_rating': aggregated_rating,
            'time_to_beat': time_to_beat,
            'external':external,
            'genres': game_dict['genres']
        }

        return filtered_data
