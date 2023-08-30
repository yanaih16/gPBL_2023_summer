from django.urls import path
from .views import top
from .views import item_list
from .views import user
from .views import item
from .views import chat
from .views import tag
from .views import item_update

urlpatterns = [
    path("", top.index, name="index"),
    path("login", user.login_user, name = "login"),
    path("logout", user.logout_user, name = "logout"),
    path("register", user.register_user, name = "register"),
    path("item_list/", item_list.ItemList.as_view(), name="item_list"),
    path("item/add", item.item_add, name="item_add"),
    path('com', chat.com, name='com'),
    path('receive_data', chat.receive_data, name='receive_data'),
    path('chat/<id>',chat.chat,name='chat'),
    path('user',chat.all_user,name='all_user'),
    path("item/tag/<int:item_id>", item.item_tag_add, name="item_tag_add"),
    path("select_tags/", tag.select_tags, name="select_tags"),
    path('item_list/<int:pk>/', item_update.ItemUpdateView.as_view(), name='item_edit'),
    path('match', tag.matching, name='match'),
    path('match/succes', tag.match_succes, name='match_succes'),
    path('item_list/<int:pk>/edit', item_update.ItemUpdateView.as_view(), name='item_edit'),
]