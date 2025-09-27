from rest_framework import serializers
from .models import MenuCategory, MenuItem

class MenuCategorySerializers(serializers.ModelSerializer):
    class Meta :
        model =MenuCategory
        fields =['id', 'name']

class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for MenuItem model - used for listing and searching menu items.
    """
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category']