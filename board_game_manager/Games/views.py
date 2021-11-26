from django.shortcuts import render, redirect
from .models import BoardGame, LendedGames
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'Games/index.html')


@login_required
def games(request):
    games = BoardGame.objects.order_by('name')
    context = {'games' : games}
    return render(request, 'Games/Games_page.html', context)


@login_required
def game(request, game_id):
    """Show a single game and its log."""
    game = BoardGame.objects.get(id=game_id)

    game_log = game.lendedgames_set.order_by('-date_lended')
    context = {'logs' : game_log}
    return render(request, 'Games/Board_Game_page.html', context)


@login_required
def game_log(request):
    log = LendedGames.objects.order_by('date_lended')
    context = {'logs' : log}
    return render(request, 'INSERT HTML HERE', context)


@login_required
def new_game(request):
    ''' Add a new game '''
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.loaned = False
            new_game.save()
            return redirect('Games:games')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'Games/new_board_game.html', context)


@login_required
def edit_game(request, game_id):
    """Edit an existing game."""
    game = BoardGame.objects.filter(owner=request.user).get(id=game_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current BoardGame.
        form = BoardGameForm(instance=game)
    else:
        # POST data submitted; process data.
        form = BoardGameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('INSERT PATH HERE', book_id=game.id)

    context = {'board_game': game, 'form': form}
    return render(request, 'INSERT HTML HERE', context)


@login_required
def loan_game(request, game_id):
    game = BoardGame.objects


@login_required
def image_view(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
        
        else:
            form = BoardGameForm()

        context = {'form': form}
        return render(request, 'image.html', context)


@login_required
def success(request):
    return HttpResponse('successfully uploaded')

'''
Games
@user
Game
@user
Add games
@user
Edit games
    -delete game
@user
Lend games
@user
User page
    -edit user profile
'''