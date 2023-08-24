from django.urls import path
from .views import top
from .views import user
from .views import item

urlpatterns = [
    path("", top.index, name="index"),
    path("login", user.login_user, name = "login"),
    path("logout", user.logout_user, name = "logout"),
    path("register", user.register_user, name = "register"),
    path("item/add", item.item_add, name="item_add"),
]