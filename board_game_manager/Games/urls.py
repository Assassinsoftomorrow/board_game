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
    # edit game details
    path('edit_game/<int:game_id>', views.edit_game, name='edit_game')
]

urlpatterns += staticfiles_urlpatterns()