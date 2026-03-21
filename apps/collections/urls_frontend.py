from django.urls import path
from . import views_frontend

urlpatterns = [
    path('', views_frontend.home_view, name='home'),
    path('login/', views_frontend.login_view, name='login'),
    path('register/', views_frontend.register_view, name='register'),
    path('logout/', views_frontend.logout_view, name='logout'),
    path('collections/', views_frontend.my_collections_view, name='my_collections'),
    path('collections/create/', views_frontend.create_collection_view, name='create_collection'),
    path('collections/<int:pk>/', views_frontend.collection_detail_view, name='collection_detail'),
    path('collections/<int:pk>/edit/', views_frontend.edit_collection_view, name='edit_collection'),
    path('collections/<int:pk>/delete/', views_frontend.delete_collection_view, name='delete_collection'),
    path('search/', views_frontend.search_characters_view, name='search_characters'),
    path('import/', views_frontend.import_character_view, name='import_character'),
    path('collections/<int:collection_id>/remove/<int:character_id>/', views_frontend.remove_character_from_collection, name='remove_character_from_collection'),
]
