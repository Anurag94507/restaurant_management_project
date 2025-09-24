from django.urls import path
from .views import MenuCategoryListAPIView

app_name = 'home'

urlpatterns = [
    path('api/categories', MenuCategoryListAPIView(), name='api-menu-categories'),
]