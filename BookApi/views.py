from django.shortcuts import render

from .models import Book

from rest_framework.response import Response

from rest_framework.decorators import api_view

from .serializers import BookSerializer


# Create your views here.

@api_view(['GET'])
def ShowAllBook(request):
    book = Book.objects.all()
    serializers = BookSerializer(book, many=True)
    
    return Response(serializers.data)


@api_view(['GET'])
def ViewBook(request, pk):
    book= Book.objects.get(id=pk)
    serializers = BookSerializer(book, many=False)

    return Response (serializers.data)

@api_view(['POST'])
def CreateBook(request):
    serializers = BookSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()

    return Response (serializers.data)


@api_view(['POST'])
def UpdateBook(request, pk):
    book = Book.objects.get(id=pk)
    serializers = BookSerializer(instance=book, data=request.data)
    if serializers.is_valid():
        serializers.save()

    return Response (serializers.data)


@api_view(['GET'])
def DeleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response('You have successfully deleted this Book from the Database')

