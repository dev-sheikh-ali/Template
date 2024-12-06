from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user):
    subject = 'Verify your email address'
    message = f'Hi {user.username},\n\nPlease verify your email address by clicking the link below:\n\nhttp://example.com/verify/{user.id}\n\nThank you!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    send_mail(subject, message, from_email, recipient_list)