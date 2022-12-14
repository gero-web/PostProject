from django.urls import path,include
from .views import SingUpView,confirm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', SingUpView.as_view(), name = 'signup'),
    path('sigin/', LoginView.as_view(template_name = 'registration/login.html' ,authentication_form=CustomAuthenticationForm),
         name = 'login'),
    path('confirm/', confirm ,name = 'confirm'),
]
