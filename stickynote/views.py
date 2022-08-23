from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import StickynoteInput
from .serializers import StickynoteInputSerializer

@api_view(["GET", "POST"])
def post_get(request):
    if request.method == "GET":
        links = StickynoteInput.objects.all()
        serializer = StickynoteInputSerializer(links, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StickynoteInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def update_link(request, id):
    try:
        Stickynote = StickynoteInput.objects.get(pk=id)
    except Stickynote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StickynoteInputSerializer(Stickynote)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StickynoteInputSerializer(Stickynote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        Stickynote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
