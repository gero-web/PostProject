import django_filters
from .models import Comment

class CommentAbsFilter(django_filters.FilterSet):
    
    class Meta:
        model = Comment
        fields = ['abs__title',]