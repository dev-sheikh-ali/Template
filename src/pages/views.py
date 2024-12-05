# src/pages/views.py

from django.shortcuts import render
from django.views.generic.base import View

class CustomErrorView(View):
    status_code = 500  # Default status code if none is provided

    def get(self, request, exception=None):
        return render(request, "pages/errors.html", {"status_code": self.status_code}, status=self.status_code)

    @classmethod
    def as_view(cls, **initkwargs):
        # Accept 'status_code' as a keyword argument and set it as a class attribute
        if 'status_code' in initkwargs:
            cls.status_code = initkwargs.pop('status_code')
        return super().as_view(**initkwargs)

# Add views for About Us, Contact, and Services pages
def about_us(request):
    return render(request, "pages/AboutUsPage.html")

def contact(request):
    return render(request, "pages/ContactPage.html")

def services(request):
    return render(request, "pages/ServicesPage.html")
