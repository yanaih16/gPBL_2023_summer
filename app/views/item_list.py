from django.shortcuts import render
from django.views.generic import ListView
from ..models import Item

class ItemList(ListView):
    model = Item
    context_object_name = "item_list"
    template_name = "item_list/item_list.html"