from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Item

class ItemList(LoginRequiredMixin, ListView):
    template_name = "item/item_list.html"
    queryset = Item.objects.order_by("-created_at")

    # ログイン中のユーザーのみアクセス可能
    def get_queryset(self):
        return Item.objects.filter(user_id=self.request.user)
