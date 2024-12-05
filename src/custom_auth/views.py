from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from allauth.socialaccount.providers.google.views import oauth2_login
import logging

logger = logging.getLogger(__name__)


# Update Profile View
@login_required
def update_profile_view(request):
    """
    View for updating user profiles.
    """
    if request.method == 'POST':
        try:
            user = request.user
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            date_of_birth_str = request.POST.get('date_of_birth')
            user.date_of_birth = parse_date(date_of_birth_str)  # Convert date string to a valid date object
            user.gender = request.POST.get('gender')
            user.bio = request.POST.get('bio')
            user.consent_given = True  # Consent is always given by default

            # Logging the values to check before saving
            logger.info(f"Updating profile for user {user.id}: first_name={user.first_name}, last_name={user.last_name}, date_of_birth={user.date_of_birth}, gender={user.gender}, bio={user.bio}, consent_given={user.consent_given}")

            user.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('home')
        except Exception as e:
            logger.error(f"Error updating profile for user {request.user.id}: {e}")
            messages.error(request, "There was an error updating your profile. Please try again.")
            return redirect('update_profile')

    return render(request, 'account/update_profile.html')
@login_required
def delete_account_view(request):
    """
    View to delete the user's account.
    """
    if request.method == 'POST':
        user = request.user
        user.delete()  # Perform the actual account deletion
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('home')

    return render(request, 'account/delete_account.html')

def google_login_view(request):
    if request.method == 'GET':
        # Render the custom Google login template
        return render(request, 'account/google_login.html')
    else:
        # Redirect to the Google OAuth login page
        return oauth2_login(request)
