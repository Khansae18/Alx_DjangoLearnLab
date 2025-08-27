from rest_framework.views import APIView

class BookList(APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

