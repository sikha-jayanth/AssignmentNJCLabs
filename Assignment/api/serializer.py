from rest_framework import serializers
from .models import Book


#creating a serializer for model Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'