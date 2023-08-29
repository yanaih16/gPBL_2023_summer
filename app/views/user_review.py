from django.shortcuts import get_object_or_404
from ..models import Review, Matching, User
from ..serializers import ReviewSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_review(request):
    rater_id = request.data.get('rater')
    evaluator_id = request.data.get('evaluator')
    score = int(request.data.get('score', 0))
    text = request.data.get('text', '')

    if rater_id is None or evaluator_id is None or score < 1 or score > 5:
        return Response({'error': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        rater = User.objects.get(pk=rater_id)
        evaluator = User.objects.get(pk=evaluator_id)
    except User.DoesNotExist:
        return Response({'error': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)

    review = Review.objects.create(rater=rater, evaluator=evaluator, score=score, text=text)
    serializer = ReviewSerializer(review)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_reviews(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)

    reviews_received = Review.objects.filter(evaluator=user)
    serializer = ReviewSerializer(reviews_received, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
