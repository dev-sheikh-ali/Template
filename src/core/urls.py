from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import urls as pages_urls
from pages.views import CustomErrorView

# Custom error handlers
handler400 = CustomErrorView.as_view(status_code=400)
handler403 = CustomErrorView.as_view(status_code=403)
handler404 = CustomErrorView.as_view(status_code=404)
handler500 = CustomErrorView.as_view(status_code=500)

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