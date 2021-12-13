from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Games'
urlpatterns= [
    #index page
    path('', views.index, name='index'),
    # game list
    path('Games/', views.games, name='games' ),
    # game details
    path('Games/<int:game_id>', views.game, name='game'),
    # loan game page
    path('loan_game/', views.loan_game, name='loan_game'),
    # add new game
    path('new_board_game/', views.new_game, name='new_game'),
    path('image_upload', views.image_view, name='image_upload'),
    path('success', views.success, name='success'),
]

urlpatterns += staticfiles_urlpatterns()