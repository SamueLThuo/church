# dbserver/api_views.py
from rest_framework import viewsets
from .models import Event, Sermon, Donation, ContactMessage
from .Serializers import EventSerializer, SermonSerializer, DonationSerializer, ContactMessageSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all().order_by('-created_at')
    serializer_class = DonationSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer





from django.shortcuts import render
from dbserver.models import Event, Sermon, Donation, ContactMessage
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def custom_admin_dashboard(request):
    context = {
        "events_count": Event.objects.count(),
        "sermons_count": Sermon.objects.count(),
        "messages_count": ContactMessage.objects.count(),
        "users_count": CustomUser.objects.count(),
        "total_donations": Donation.objects.aggregate(total=models.Sum('amount'))["total"] or 0,
        "donations": Donation.objects.order_by('-created_at')[:5],
    }
    return render(request, "admin/dashboard.html", context)

