from django.urls import path
from .views import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

]