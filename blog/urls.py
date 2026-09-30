from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
# router.register(r'', landing_page, basename='landing-page')

urlpatterns = [
    path('', include(router.urls)),
]