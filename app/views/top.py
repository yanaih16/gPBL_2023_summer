from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from ..models import Item
from django.db.models import Max
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    html = "<h1>myappのウェルカムページです</h1>"
    return render(request, "index.html")