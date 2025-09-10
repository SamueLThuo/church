from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, SermonViewSet, DonationViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'sermons', SermonViewSet)
router.register(r'donations', DonationViewSet)
router.register(r'messages', ContactMessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
