from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Comment



@receiver(post_save, sender=Comment)
def new_comment(sender,instance:Comment, created,**kwargs):
    if created:
        user = instance.abs.user
        send_mail(
            'New comment',
            f'Пользователь {instance.user.get_username()} оставил комментарий к вашему посту',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        print(user.email)