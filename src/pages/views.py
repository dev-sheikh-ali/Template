# src/pages/views.py

from django.shortcuts import render , redirect
from django.views.generic.base import View
from home.models import TeamMember
from django.contrib import messages
from .forms import ContactForm
from utils.views import contact_web_owner
from django.conf import settings 
from .models import CompanyInfo, Address, ContactUs




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
    team_members = TeamMember.objects.all()
    return render(request, "pages/AboutUsPage.html", {"team_members": team_members})

def contact(request):
    form = ContactForm(request.POST or None)
    
    # Fetch all the entries for the dynamic sections
    company_infos = CompanyInfo.objects.all()
    addresses = Address.objects.all()
    contact_infos = ContactUs.objects.all()
    
    if request.method == "POST":
        if contact_web_owner(request, form, recipient_email=settings.SUPPORT_TEAM_EMAIL):
            form = ContactForm()  # Reset the form after a successful submission
        else:
            pass  # Errors handled by the utility function

    return render(request, "pages/ContactPage.html", {
        "form": form,
        "company_infos": company_infos,
        "addresses": addresses,
        "contact_infos": contact_infos,
        
    })

def services(request):
    return render(request, "pages/ServicesPage.html")
