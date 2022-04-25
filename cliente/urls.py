from django.contrib import admin
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from cliente import views as cliente_views
from cliente.views import *


router = DefaultRouter()
router.register(r'cliente', cliente_views.ClienteViewSet, basename='cliente')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)), 

]