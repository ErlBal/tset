from django.urls import path
from . import views

urlpatterns = [
    path('game_list/', views.GameListViews.as_view(), name='gameList'),
    path('game_detail/<int:id>/', views.GameDetailInfo.as_view(), name='detail'),
    path('game_detail/<int:id>/delete/', views.DeleteGameView.as_view(), name='delete'),
    path('game_detail/<int:id>/update/', views.UpdateGameView.as_view(), name='update'),
    path('create_game/', views.GameCreateView.as_view(), name='createGame'),
    path('search/', views.Search.as_view(), name='search'),
    path('create_review/', views.FormCommentView.as_view(), name='createReview')
]