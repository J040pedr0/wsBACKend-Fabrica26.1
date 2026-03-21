from django.urls import path
from . import views

urlpatterns = [
    path('', views.CollectionListCreateView.as_view(), name='collection-list'),
    path('<int:pk>/', views.CollectionDetailView.as_view(), name='collection-detail'),
    path('characters/', views.CharacteristicListCreateView.as_view(), name='character-list'),
    path('characters/<int:pk>/', views.CharacteristicDetailView.as_view(), name='character-detail'),
    path('favorites/', views.FavoriteListCreateView.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDeleteView.as_view(), name='favorite-delete'),
    path('external/search/', views.search_rick_and_morty, name='search-rick-morty'),
   path('external/import/', views.import_characters_from_api, name='import-character'),

]