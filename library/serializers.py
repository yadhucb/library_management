from rest_framework import serializers
from library.models import User, Book, CheckOut

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
        'username',
        'mobile',
        'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class BookSerializer(serializers.ModelSerializer):
    available_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'
    
class CheckOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckOut
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
