from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from .models import User



class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'categoriUser')
        
        
class  CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if  not user.is_active :
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')
        
class CustomUserChangeFrom(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'categoriUser')
    


