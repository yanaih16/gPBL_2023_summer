from django.shortcuts import render

def index(request):
    content = {
        "title": "MatchMarket",
    }
    return render(request, "index.html", content)