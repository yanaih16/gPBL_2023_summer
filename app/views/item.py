from django.shortcuts import render
from django.db.models import Max
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from ..models import Item
from ..models import User
from ..forms.item import ItemAdd


# Create your views here.
@login_required
def item_add(request):
    if request.POST:
        user = User.objects.get(id=request.user.id)
        item = Item(
            name=request.POST["name"],
            value=request.POST["value"],
            image=request.POST["image"],
            text=request.POST["text"],
            user_id=user,
        )
        item.save()
        context = {
            "title": "追加処理完了",
        }

        return render(request, "item/add_succes.html", context)
    context = {
        "title": "商品追加",
        "form": ItemAdd()
    }
    return render(request, "item/add.html", context)