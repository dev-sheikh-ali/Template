from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
    path('pages/', include('pages.urls')),                   # Static pages URLs
    path('blog/', include('blog.urls')),                     # Blog app URLs
    path('ckeditor5/', include('django_ckeditor_5.urls')),   # CKEditor 5 URLs
]

# Static and media file serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
