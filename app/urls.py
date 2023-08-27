from django.urls import path
from .views import top
from .views import user, item_list

urlpatterns = [
    path("", top.index, name="index"),
    path("login", user.login_user, name = "login"),
    path("logout", user.logout_user, name = "logout"),
    path("register", user.register_user, name = "register"),
    path("item_list", item_list.ItemList.as_view(), name="item_list"),
]