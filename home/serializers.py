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
    category = MenuCategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'category']