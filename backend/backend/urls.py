# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dbserver.urls')),  # Include dbserver API routes
    path('', include('accounts.urls')),  # Include accounts API
    
]
