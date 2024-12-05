from django.urls import path
from allauth.account.views import (
    LoginView,
    SignupView,
    PasswordResetView,
    PasswordChangeView,
    EmailVerificationSentView,
    LogoutView,
)
from allauth.socialaccount.views import ConnectionsView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from . import views

# Custom ConfirmEmailView to redirect users to complete their profile
from allauth.account.views import ConfirmEmailView
class CustomConfirmEmailView(ConfirmEmailView):
    def get_success_url(self):
        # Redirect users to the profile page after confirming their email
        return reverse_lazy('profile')

urlpatterns = [
    # Allauth Views
    path('login/', LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('signup/', SignupView.as_view(template_name='account/signup.html'), name='account_signup'),
    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset.html'), name='account_reset_password'),
    path('password-change/', PasswordChangeView.as_view(template_name='account/password_change.html', success_url=reverse_lazy('home')), name='account_change_password'),
    path('email-verification-sent/', EmailVerificationSentView.as_view(template_name='account/email_verification_sent.html'), name='account_email_verification_sent'),
    path('confirm-email/<str:key>/', CustomConfirmEmailView.as_view(template_name='account/confirm_email.html'), name='account_confirm_email'),
    path('social-connections/', ConnectionsView.as_view(template_name='account/socialaccount_connections.html'), name='social_connections'),
    path('logout/', LogoutView.as_view(), name='account_logout'),

    # Custom Views
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('delete-account/', views.delete_account_view, name='delete_account'),
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
]
