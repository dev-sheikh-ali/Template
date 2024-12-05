from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=255, default="Payments tool for software companies")
    subtitle = models.TextField(default="From checkout to global sales tax compliance, companies around the world use Flowbite to simplify their payment stack.")
    button_text = models.CharField(max_length=100, default="Get started")
    button_url = models.URLField(max_length=200, default="#")
    secondary_button_text = models.CharField(max_length=100, default="Speak to Sales", null=True, blank=True)
    secondary_button_url = models.URLField(max_length=200, default="#", null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True, default="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/phone-mockup.png")

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=255, default="Feature Title")
    description = models.TextField(default="Feature description.")
    icon_svg = models.TextField(help_text="Paste SVG content here for the icon", default="")
    link_text = models.CharField(max_length=100, default="Learn more")
    link_url = models.URLField(max_length=500, default="#")

    def __str__(self):
        return self.title

class Newsletter(models.Model):
    title = models.CharField(max_length=255, default="Sign up for our newsletter")
    description = models.TextField(default="Stay up to date with our latest announcements, exclusive discounts, and upcoming events. Sign up now!")
    terms_of_service_url = models.URLField(max_length=500, default="#")
    privacy_policy_url = models.URLField(max_length=500, default="#")

    def __str__(self):
        return self.title

class NewsletterSubscription(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class NavbarBanner(models.Model):
    message = models.CharField(max_length=255, default="We have launched Flowbite Blocks featuring over 450+ website sections!")
    link_text = models.CharField(max_length=100, default="Check it out")
    link_url = models.URLField(max_length=500, default="#")
    svg_icon = models.TextField(help_text="Paste SVG content here for the icon", default="")
    is_active = models.BooleanField(default=True, help_text="Toggle to enable or disable this banner")

    def __str__(self):
        return self.message
