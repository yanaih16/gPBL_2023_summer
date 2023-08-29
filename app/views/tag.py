from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import Tag, Item

@login_required
def select_tags(request):
    if request.method == 'POST':
        selected_tags = request.POST.getlist('tags')
        items = Item.objects.filter(item_tag__tag_id__in=selected_tags).distinct()
        return render(request, 'matching.html', {'items': items})
    else:
        tags = Tag.objects.all()
        return render(request, 'select_tags.html', {'tags': tags})

