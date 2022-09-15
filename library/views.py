from ast import Delete
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from library.permissions import IsAdminOnly
from library.models import User, Book, CheckOut
from library.serializers import UserSerializer, BookSerializer, CheckOutSerializer

class CreateStudentView(generics.CreateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer

class ListStudentView(generics.ListAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_admin = False)

class SingleStudentView(generics.RetrieveAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_admin = False)

class UpdateStudentView(generics.UpdateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_admin = False)

class DeleteUserView(generics.DestroyAPIView):
    permission_classes = (IsAdminOnly,)
    queryset = User.objects.filter(is_admin = False)

class CreateBookView(generics.CreateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = BookSerializer

class ListBookView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class SingleBookView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UpdateBookView(generics.UpdateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBookView(generics.DestroyAPIView):
    permission_classes = (IsAdminOnly,)
    queryset = Book.objects.all()

class CreateCheckoutView(generics.CreateAPIView):
    permission_classes = (IsAdminOnly,)

    def create(self, request, *args, **kwargs):
        serializer = CheckOutSerializer(data=request.data)
        try:
            book = Book.objects.get(id = request.data.get('book'))
            required_qty = request.data.get('qty')

            if not book.is_available:
                return Response('This book is Out of stock')
            if required_qty>book.qty:
                return Response('Quantity should be less than or equal to the available quantity')

            elif serializer.is_valid():
                book.qty-=required_qty
                book.save()
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response('No such book available')

class ListCheckoutView(generics.ListAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = CheckOutSerializer
    queryset = CheckOut.objects.all()

class SingleCheckoutView(generics.RetrieveAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = CheckOutSerializer
    queryset = CheckOut.objects.all()

class UpdateCheckoutView(generics.UpdateAPIView):
    permission_classes = (IsAdminOnly,)

    def update(self, request, *args, **kwargs):
        
        try:
            book = Book.objects.get(id = request.data.get('book'))
            instance = CheckOut.objects.get(id=kwargs.get('pk'))
            serializer = CheckOutSerializer(data=request.data, instance=instance)
            required_qty = request.data.get('qty')
            if not book.is_available and required_qty > instance.qty:
                return Response('This book is Out of stock')
            if required_qty>book.qty+instance.qty:
                return Response('Quantity should be less than or equal to the available quantity')

            elif serializer.is_valid():
                if required_qty > instance.qty:
                    book.qty-=required_qty - instance.qty
                    book.save()
                elif required_qty < instance.qty:
                    book.qty+= instance.qty - required_qty
                    book.save()
                
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response('No such book available')

class DeleteCheckoutView(generics.DestroyAPIView):
    permission_classes = (IsAdminOnly,)
    queryset = CheckOut.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id = request.data.get('book'))
            instance = CheckOut.objects.get(id=kwargs.get('pk'))
            book.qty+=instance.qty
            book.save()
            instance.delete()
            return Response('Deleted')
        except:
            return Response('No such book available')




