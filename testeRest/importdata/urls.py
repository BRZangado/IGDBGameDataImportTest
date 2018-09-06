from django.urls import include, path
from .views import IgDBView,UserViewSet

urlpatterns = [
    path('get_igdb_games_list/', IgDBView.as_view(), name="get_igdb_games"),
    path('teste/', UserViewSet.as_view({'get': 'list'}), name="teste"),
]