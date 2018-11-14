from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('<int:game_id>/results/', views.results, name = 'results'),
] 