from django.contrib import admin
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from vehiculo import views as views

router = DefaultRouter()
router.register(r'vehiculo', views.VehiculoViewSet, basename='vehiculo')
router.register(r'arreglo', views.ArregloViewSet, basename='arreglos')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
]