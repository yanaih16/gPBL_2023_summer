from django.urls import path
from .views import top
from .views import item_list
from .views import user
from .views import item
from .views import item_update
from .views import user_review

urlpatterns = [
    path("", top.index, name="index"),
    path("login", user.login_user, name = "login"),
    path("logout", user.logout_user, name = "logout"),
    path("register", user.register_user, name = "register"),
    path("item_list/", item_list.ItemList.as_view(), name="item_list"),
    path("item/add", item.item_add, name="item_add"),
    path("item/tag/<int:item_id>", item.item_tag_add, name="item_tag_add"),
    path('item_list/<int:pk>/', item_update.ItemUpdateView.as_view(), name='item_edit'),
    path('add_review/', user_review.add_review, name='add_review'),
    path('get_reviews/<int:user_id>/', user_review.get_reviews, name='get_reviews'),
]