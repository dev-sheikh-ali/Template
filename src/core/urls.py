# core/urls.py
from django.contrib import admin
from django.urls import path, include
from pages import urls as pages_urls

# Custom error handlers imported from pages.urls
handler400 = pages_urls.handler400
handler403 = pages_urls.handler403
handler404 = pages_urls.handler404
handler500 = pages_urls.handler500

urlpatterns = [
    path('admin/', admin.site.urls),                         # Admin panel
    path('accounts/', include('allauth.urls')),              # Django Allauth URLs
    path('auth/', include('custom_auth.urls')),              # Custom authentication app URLs
    path('', include('home.urls')),                          # Home app URLs (homepage and static pages)
    path('pages/', include('pages.urls')), 
    
]
