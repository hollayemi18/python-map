from django.urls import path
from main import views


urlpatterns = [
    path('', views.show, name="show"),
    path('emp', views.emp),
    path('map?p<id>/', views.user_map, name="map")
]
