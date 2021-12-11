from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Games'
urlpatterns= [
    path('', views.index, name='index'),
    path('Games/', views.games, name='games' ),
    path('Games/<int:game_id>', views.game, name='game'),
    path('Games/<int:game_id>', views.edit_game, name='edit_game'),
    path('new_board_game/', views.new_game, name='new_game'),
    path('image_upload', views.image_view, name='image_upload'),
    path('success', views.success, name='success'),
]

urlpatterns += staticfiles_urlpatterns()