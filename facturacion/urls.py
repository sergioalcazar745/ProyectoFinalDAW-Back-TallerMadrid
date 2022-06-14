"""Users URLs."""

# Django
from django.urls import include, path
import facturacion

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from facturacion import views as fact_views

router = DefaultRouter()
router.register(r'facturacion', fact_views.GastoViewSet, basename='facturacion')


urlpatterns = [
    path('', include(router.urls)),
]