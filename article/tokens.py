from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()

print(account_activation_token)

def mail(self,**kwargs):
    subject = 'Thank you for registering to our site'
    message="it  means a world to us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [kwargs['email']]
    send_mail( subject, message, email_from, recipient_list )
    return True