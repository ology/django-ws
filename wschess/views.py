from django.shortcuts import render

def index(request):
    if request.method == "POST":
        newPos = request.POST.get('newPos')
    else:
        newPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    context = { "newPos": newPos, }
    return render(request, "wschess/index.html", context)

def lobby(request):
    return render(request, 'wschess/lobby.html')
