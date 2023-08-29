from django.shortcuts import render, redirect
from ..models import Review, Matching
from django.contrib.auth.decorators import login_required

@login_required
def review(request, matching_id):
    matching = Matching.objects.get(id=matching_id)
    if request.method == 'POST':
        score = request.POST['score']
        text = request.POST['text']
        Review.objects.create(rater=request.user, evaluator=matching.seller, score=score, text=text)
        return redirect('top')
    return render(request, 'review.html', {'matching': matching})
