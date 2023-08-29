from django.views.generic import UpdateView
from django.urls import reverse_lazy
from ..models import Item
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'text', 'value', 'image']  # 必要なフィールドのみを指定
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"



class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/item_update.html'
    success_url = reverse_lazy("item_list")  # 成功時のリダイレクト先を指定します。

    # ログイン中のユーザーのみアクセス可能
    def get_queryset(self):
        return Item.objects.filter(user_id=self.request.user)