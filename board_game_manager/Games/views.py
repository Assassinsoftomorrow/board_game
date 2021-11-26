from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'Games/index.html')
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