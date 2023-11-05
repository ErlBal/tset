from django.urls import path
from . import views

urlpatterns = [
    path('game_list_parser/', views.ParserGameListView.as_view()),
    path('start_parsing/', views.ParserFormView.as_view()),
]