from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    date_of_birth = forms.DateField(required=False, widget=forms.SelectDateWidget(years=range(1900, 2025)))
    bio = forms.CharField(required=False, widget=forms.Textarea)
    consent_given = forms.BooleanField(initial=True, required=True)  # Default True

    def save(self, request):
        """
        Save custom signup form fields to the user model.
        """
        user = super().save(request)
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.bio = self.cleaned_data['bio']
        user.consent_given = self.cleaned_data['consent_given']
        user.save()
        return user
