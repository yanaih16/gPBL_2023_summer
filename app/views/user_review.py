from django.shortcuts import render, redirect
from django.db.models import Avg
from ..models import Review, Matching
from ..forms.review import ReviewForm


def rate_seller(request, matching_id):
    matching = Matching.objects.get(id=matching_id)
    seller = matching.seller
    buyer = matching.buyer
    if request.method == "POST":
        score = int(request.POST["score"])
        text = request.POST["text"]
        check = Review.objects.filter(rater=buyer, evaluator=seller)
        if check:
            review = Review.objects.get(rater=buyer, evaluator=seller)
            review.score = score
            review.text = text
            review.save()
            return redirect("match")
        review = Review.objects.create(
            rater=buyer, evaluator=seller, score=score, text=text
        )
        review.save()
        # Calculate average rating for the seller
        average_rating = Review.objects.filter(evaluator=seller).aggregate(
            Avg("score")
        )["score__avg"]
        seller.average_rating = average_rating
        seller.save()

        return redirect("match")

    return render(request, "review/review.html", {"matching": matching})
