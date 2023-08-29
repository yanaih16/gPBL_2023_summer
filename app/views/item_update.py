from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ..models import Item
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'text', 'value', 'image']  # 必要なフィールドのみを指定


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/item_update.html'
    success_url = reverse_lazy("item_list")  # 成功時のリダイレクト先を指定します。