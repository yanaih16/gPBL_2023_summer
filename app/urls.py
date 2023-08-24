from django.urls import path
from .views import top

urlpatterns = [
    path("", top.index, name="index"),
]