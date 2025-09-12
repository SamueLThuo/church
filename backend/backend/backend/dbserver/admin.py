# dbserver/admin.py
from django.contrib import admin
from .models import Event, Sermon, Donation, ContactMessage

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'date', 'time', 'created_at']
    search_fields = ['title', 'location']

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'preacher', 'date']
    search_fields = ['title', 'preacher']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'amount', 'created_at']
    search_fields = ['name', 'email']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']


