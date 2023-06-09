from django.urls import path
from main import views


urlpatterns = [
    path('', views.show, name="show"),
    path('emp', views.emp)
]
