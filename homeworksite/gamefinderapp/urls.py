from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:game_id>/results/', views.results, name = 'results'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)