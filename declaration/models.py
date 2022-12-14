from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
user_model = get_user_model()


class Abs(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=30)
    file = models.FileField()    

class Comment(models.Model):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    text = models.TextField()
    abs  = models.ForeignKey(Abs, on_delete=models.CASCADE)

    def success_comment(self):
        send_mail( 'Ваш комментарий принили!', 
                'Спасибо за ваш комментарий !!',
                settings.EMAIL_HOST_USER,
                [self.user.email],
                fail_silently=False,
                 
            )