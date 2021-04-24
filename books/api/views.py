from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import generics, viewsets

#API for Get All Books
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    book       = Book.objects.all()
    serializer = BookSerializer(instance=book, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

#API for Get a Book
@api_view(['GET'])
def book(request, id):
    try:
        book       = Book.objects.get(pk=id)
        serializer = BookSerializer(instance=book, many=False)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response(data={
        'success' : False,
        'errors' : 'Book Not Found'
        }, status=status.HTTP_404_NOT_FOUND)

#API for Create Book
@api_view(['POST'])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'success' : True,
            'message' : 'Book has been successfully added'
        },status= status.HTTP_201_CREATED)
    return Response(data={
        'success' : False,
        'errors' : serializer.errors
    }, status=status.HTTP_404_BAD_REQUEST)

#API for Delete Book
@api_view(['DELETE'])
def delete(request, id):
    try:
        book       = Book.objects.get(pk=id)
        # serializer = BookSerializer(instance=book, many=False)
        if book:
            book.delete()
            return Response(data={
                'success' : True,
                'message' : 'Book has been successfully deleted'
            },status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response(data={
        'success' : False,
        'errors' : 'Book Not Found'
        }, status=status.HTTP_404_NOT_FOUND)

#API for Update Book
@api_view(['PUT'])
def update(request, id):
    try:
        book       = Book.objects.get(pk=id)
        serializer = BookSerializer(data=request.data, instance=book)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                'success' : True,
                'message' : 'Book has been successfully Updated'
            },status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response(data={
        'success' : False,
        'errors' : 'Book Not Found'
        }, status=status.HTTP_404_NOT_FOUND)

#=====================Implementing of Generic Classes================================#
class RUDBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#=====================================================================================#

#===================================Apply of ViewSet==================================#
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#=====================================================================================#