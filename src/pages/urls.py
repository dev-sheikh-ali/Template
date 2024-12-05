# src/pages/urls.py

from django.urls import path
from .views import CustomErrorView, about_us, contact, services 

# Custom error handlers using the class-based view
handler400 = CustomErrorView.as_view(status_code=400)
handler403 = CustomErrorView.as_view(status_code=403)
handler404 = CustomErrorView.as_view(status_code=404)
handler500 = CustomErrorView.as_view(status_code=500)

urlpatterns = [
    path('about/', about_us, name='about_us'),          # About Us page
    path('contact/', contact, name='contact'),          # Contact page
    path('services/', services, name='services'),       # Services page
    # Optionally add other page-related routes here.
]
