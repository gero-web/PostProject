from django.contrib.auth.models import  AbstractUser
from django.db import models


class CategoriUser(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    categoriUser = models.ForeignKey(CategoriUser, null= True,  on_delete=models.CASCADE)
    code = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.username