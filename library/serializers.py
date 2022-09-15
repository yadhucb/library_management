from rest_framework import serializers
from library.models import User, Book, CheckOut

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
        'id',
        'username',
        'mobile',
        'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class BookSerializer(serializers.ModelSerializer):

    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'qty', 'is_available')
    
    def get_is_available(self, instance):
        if instance.is_available:
            return 'In stock'
        else:
            return 'Out of stock'

class CheckOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckOut
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
