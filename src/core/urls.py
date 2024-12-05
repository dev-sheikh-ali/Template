from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500
from pages.views import CustomErrorView

# Custom error handlers using the class-based view
handler400 = CustomErrorView.as_view(status_code=400)
handler403 = CustomErrorView.as_view(status_code=403)
handler404 = CustomErrorView.as_view(status_code=404)
handler500 = CustomErrorView.as_view(status_code=500)

urlpatterns = [
    path('admin/', admin.site.urls),                         # Admin panel
    path('accounts/', include('allauth.urls')),              # Django Allauth URLs
    path('auth/', include('custom_auth.urls')),              # Custom authentication app URLs
    path('', include('home.urls')),                          # Home app URLs (for the homepage and static pages)
]
