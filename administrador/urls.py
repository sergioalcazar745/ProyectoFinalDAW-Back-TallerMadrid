"""Admin URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from administrador import views as administrador_views

router = DefaultRouter()
router.register(r'administrador', administrador_views.AdminViewSet, basename='administrador'),
router.register(r'administradorOut', administrador_views.AdminOutViewSet, basename='administradorOut'),

urlpatterns = [
    path('', include(router.urls)),
]