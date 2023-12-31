from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Tag, Item, User, Item_Tag, Matching, Review
import json
from gensim.models import KeyedVectors
import operator

model_dir = "./word2vec/entity_vector.model.bin"
model = KeyedVectors.load_word2vec_format(model_dir, binary=True)


@login_required
def select_tags(request):
    tag_list = Tag.objects.values("id", "name")
    context = {
        "title": "タグ設定",
        "tag_list": tag_list,
    }
    return render(request, "tag/select_tags.html", context)


def matching(request):
    if request.method == "POST":
        tag_id_list = request.POST.getlist("tags")
        post_tags = []
        for tag_id in tag_id_list:
            tag = Tag.objects.get(id=tag_id)
            post_tags.append(tag.name)
        data_list = Item.objects.all()
        data = []
        for item in data_list:
            user = User.objects.get(id=item.user.id)
            if request.user == user:
                continue
            reviews = Review.objects.filter(rater=item.user)
            score = 0
            num = 0
            for review in reviews:
                score += review.score
                num += 1
            if num != 0:
                score /= num
            item_tags = Item_Tag.objects.filter(item=item.id)
            matchs = Matching.objects.filter(item=item.id)
            f = False
            for match in matchs:
                if match.seller == request.user:
                    f = True
            if f:
                continue
            count = 0
            per = 0.0
            for item_tag in item_tags:
                tag = Tag.objects.get(id=item_tag.tag.id)
                for post_tag in post_tags:
                    per += model.similarity(tag.name, post_tag)
                    count += 1
            per /= count
            data.append(
                {
                    "item_id": item.id,
                    "user_id": user.id,
                    "user": user.username,
                    "score": score,
                    "name": item.name,
                    "text": item.text,
                    "image": item.image.url,
                    "value": item.value,
                    "per": per,
                }
            )
        a = sorted(data, key=operator.itemgetter("per"), reverse=True)
        return render(request, "tag/matching.html", {"items": json.dumps(a)})
    else:
        return redirect("select_tags")


def match_succes(request):
    if request.method == "POST":
        seller = User.objects.get(id=request.user.id)
        buyer = User.objects.get(id=request.POST["user_id"])
        item = Item.objects.get(id=request.POST["item_id"])
        match = Matching(
            seller=seller,
            buyer=buyer,
            item=item,
        )
        match.save()
        return render(request, "tag/succes.html", {"matching": match})
