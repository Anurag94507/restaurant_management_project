from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import response
from rest_framework import status

from .models import Menucategory, MenuItem
from .serializers import MenucategorySerializer, MenuItemSerializer

class MenucategoryListAPIView(generics.ListAPIView):
    """
    API endpoint to list all menu categories.
    Only Get is allowed (read-only list).
    """
    queryset = Menucategory.objects.all()
    serializer_class = MenucategorySerializer

class MenuItemSearchAPIView(generics.ListAPIView):
    """
    API endpoint to search menu items by name (using query param 'search').
    """
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        qs = MenuItem.objects.all()
        search_term = self.request.query_params.get('search', None)
        if search:
            qs =qs.filter(name_icontains=search)
        return qs