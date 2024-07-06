from djoser.email import ActivationEmail

class CustomActivationEmail(ActivationEmail):
    template_name = "email/account_activate_email.html"