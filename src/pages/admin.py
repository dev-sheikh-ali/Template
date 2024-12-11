from django.contrib import admin
from .models import CompanyInfo, Address, ContactUs

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'linkedin_url')
    fields = ('name', 'icon_svg', 'description', 'linkedin_url')
    search_fields = ('name', 'linkedin_url')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    fields = ('name', 'icon_svg', 'description', 'address')
    search_fields = ('name', 'address')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email')
    fields = ('name', 'icon_svg', 'description', 'contact_email')
    search_fields = ('name', 'contact_email')
