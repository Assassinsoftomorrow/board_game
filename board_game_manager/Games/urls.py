from django.urls import path

from . import views

app_name = 'Games'
urlpatterns= [
    path('', views.index, name='index'),
    path('Games/', views.games, name='games' ),
    path('Games/<int:game_id>', views.game, name='game'),
    path('new_board_game/', views.new_game, name='new_game'),
    path('image_upload', views.image_view, name='image_upload'),
    path('success', views.success, name='success'),
]
