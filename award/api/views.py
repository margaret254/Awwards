from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from award.models import AwardPost
from award.api.serializers import AwardPostSerializers

@api_view(['GET',])
def api_detail_award_view(request, slug):

    try:
        award_post = AwardPost.objects.get(slug=slug)
    except AwardPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AwardPostSerializer(award_post)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_award_view(request, slug):

    try:
        award_post = AwardPost.objects.get(slug=slug)
    except AwardPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AwardPostSerializer(award_post,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successful"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def api_delete_award_view(request, slug):

    try:
        award_post = AwardPost.objects.get(slug=slug)
    except AwardPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = award_post.delete()
        data = {}
        if operation:
            data["sucess"] = "Delete successful"
        else:
            data["failure"] = "Delete failed"      
        return Response(data=data)

@api_view(['POST',])
def api_create_award_view(request):
    account = Account.objects.get(pk=1)

    award_post = AwardPost(author=account)

    if request.method == "POST":
        serializer = AwardPostSerializer(award_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)


    