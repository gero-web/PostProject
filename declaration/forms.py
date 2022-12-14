from django.db import models
from django.forms import ModelForm
from .models import Comment, Abs


class CommentForm(ModelForm):
     class Meta:
        model = Comment
        fields = ['text', 'abs']


    
class AbsForm(ModelForm):
     class Meta:
        model = Abs
        fields =  ['text', 'title', 'file']