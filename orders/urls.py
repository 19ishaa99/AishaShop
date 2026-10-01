
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet # mpesa_callback

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('mpesa/callback/', mpesa_callback, name='mpesa-callback'),
]
