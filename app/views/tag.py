from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Tag, Item, User
import json
from django.http import JsonResponse

@login_required
def select_tags(request):
    if request.method == 'POST':
        data_list = Item.objects.all()
        data = []
        for item in data_list:
            user = User.objects.get(id=item.user.id)
            if request.user == user : 
                continue
            print(item.image.url)
            data.append({
                "id" : item.id,
                "user" : user.username,
                'name' : item.name, 
                'text' : item.text, 
                'image' : item.image.url,
                'value' : item.value,
            })
        return render(request, 'tag/matching.html', {'items': json.dumps(data)})
    else:
        tag_list = Tag.objects.values("id", "name")
        context = {
            "title": "タグ設定",
            "tag_list": tag_list,
        }
        return render(request, 'tag/select_tags.html', context)
