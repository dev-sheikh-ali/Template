# /utils/views.py

import threading
from django.core.mail import send_mail
from django.contrib import messages

def send_email_async(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"Error sending email: {e}")

def contact_web_owner(request, form, recipient_email):
    """
    Utility function to process the contact form and send emails.

    Args:
        request (HttpRequest): The current HTTP request.
        form (Form): The validated contact form.
        recipient_email (str): Recipient's email address.

    Returns:
        bool: True if the emails are sent successfully, False otherwise.
    """
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone_number = form.cleaned_data["phone_number"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        full_message = (
            
            f"Name: {first_name} {last_name}\n"
            f"Email: {email}\n"
            f"Phone Number: {phone_number}\n\n"
            
            f"\n{message}\n"
        )
        confirmation_message = (
            f"Dear {first_name},\n\n"
            f"Thank you for reaching out to us. We have received your message and "
            f"will get back to you as soon as possible.\n\n"
            f"Best regards,\n"
            f"Support Team"
        )

        try:
            # Send emails using threading
            threading.Thread(
                target=send_email_async,
                args=(f"Contact Us: {subject}", full_message, email, [recipient_email]),
            ).start()
            threading.Thread(
                target=send_email_async,
                args=("Thank you for contacting us!", confirmation_message, recipient_email, [email]),
            ).start()

            messages.success(request, "Your message has been sent successfully! A confirmation email has been sent to your address.")
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, "Failed to send your message. Please try again later.")
            return False
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
        return False
