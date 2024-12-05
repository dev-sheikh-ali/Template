from django.urls import path
from allauth.account.views import (
    LoginView,
    SignupView,
    PasswordResetView,
    PasswordChangeView,
    PasswordSetView,  # Import the PasswordSetView
    EmailVerificationSentView,
    LogoutView,
)
from allauth.socialaccount.views import ConnectionsView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Allauth Views
    path('login/', LoginView.as_view(template_name='account/login.html'), name='account_login'),
    path('signup/', SignupView.as_view(template_name='account/signup.html'), name='account_signup'),
    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset.html'), name='account_reset_password'),
    path('password-change/', PasswordChangeView.as_view(template_name='account/password_change.html', success_url=reverse_lazy('home')), name='account_change_password'),
    path('password-set/', PasswordSetView.as_view(template_name='account/password_change.html', success_url=reverse_lazy('home')), name='account_set_password'),  # Updated to use the same template
    path('email-verification-sent/', EmailVerificationSentView.as_view(template_name='account/email_verification_sent.html'), name='account_email_verification_sent'),
    path('confirm-email/<str:key>/', EmailVerificationSentView.as_view(template_name='account/email_verification_sent.html'), name='account_confirm_email'),
    path('social-connections/', ConnectionsView.as_view(template_name='account/socialaccount_connections.html'), name='social_connections'),
    path('logout/', LogoutView.as_view(), name='account_logout'),

    # Custom Views
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('delete-account/', views.delete_account_view, name='delete_account'),
    path('google-login/', views.google_login_view, name='google_login'),
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
]
