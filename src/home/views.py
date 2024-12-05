from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HeroSection, Feature, Newsletter, NewsletterSubscription, NavbarBanner
from .forms import NewsletterSubscriptionForm

def home_view(request):
    hero_section = HeroSection.objects.first()
    features = Feature.objects.all()
    newsletter = Newsletter.objects.first()
    navbar_banner = NavbarBanner.objects.filter(is_active=True).first()

    form = NewsletterSubscriptionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        if not NewsletterSubscription.objects.filter(email=email).exists():
            form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
        else:
            messages.info(request, 'You are already subscribed to our newsletter.')
        return redirect('home')

    context = {
        'hero_section': hero_section,
        'features': features,
        'newsletter': newsletter,
        'form': form,
        'banner': navbar_banner,
    }
    return render(request, 'home/home.html', context)
