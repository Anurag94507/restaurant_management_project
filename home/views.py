from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Menucategory
from .serializers import MenucategorySerializers

class MenucategoryListAPIView(generics.ListAPIView):
    """
    API endpoint to list all menu categories.
    Only Get is allowed (read-only list).
    """
    queryset = Menucategory.objects.all()
    serializer_class = MenucategorySerializer