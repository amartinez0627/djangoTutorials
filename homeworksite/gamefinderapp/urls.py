from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('<string:console_param>/<string:genre_param>/<int:age_param>/results/', views.results, name = 'results'),
] 