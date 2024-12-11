from django.db import models
from django.conf import settings

class BaseSection(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    icon_svg = models.TextField(
        verbose_name="SVG Icon",
        help_text="Paste the SVG content here for the icon",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True,
        help_text="Optional description for this section."
    )

    class Meta:
        abstract = True

class CompanyInfo(BaseSection):
    linkedin_url = models.URLField(
        verbose_name="LinkedIn URL",
        blank=True,
        null=True,
        help_text="LinkedIn profile URL for the company."
    )

    class Meta:
        verbose_name = "Company Info"
        verbose_name_plural = "Company Infos"

    def __str__(self):
        return f"Company Information - {self.name}"

class Address(BaseSection):
    address = models.TextField(
        verbose_name="Address",
        help_text="Physical address of the company."
    )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"Address - {self.name}"

class ContactUs(BaseSection):
    contact_email = models.EmailField(
        verbose_name="Contact Email",
        help_text="Email address for contact purposes.",
        default=settings.SUPPORT_TEAM_EMAIL,
    )

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"Contact Us - {self.name}"
