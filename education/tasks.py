from celery import shared_task
from django.core.mail import send_mass_mail
from energy_distribution.models import EnergyUser

@shared_task
def send_education_campaign():
    users = EnergyUser.objects.all()
    messages = []
    for user in users:
        message = (
            'Clean Energy Education',
            'Learn about the benefits of renewable energy!',
            'noreply@cleanenergy.com',
            [user.email],
        )
        messages.append(message)
    send_mass_mail(messages, fail_silently=False)