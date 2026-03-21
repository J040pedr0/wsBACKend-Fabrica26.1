from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.Registerview.as_view(), name='register'),
    path('me/', views.UserDetailview.as_view(), name='user-detail'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]