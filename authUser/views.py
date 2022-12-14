from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import response,HttpResponseRedirect
from django.views.generic.edit import CreateView
from .forms import CustomUserCreateForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
import random

def code():
    random.seed()
    return str(random.randint(1001,9999))

def confirm(request):
    if request.method == 'POST':
        print(request.POST)
        code = request.POST.get('code')
        if code:
            User = get_user_model()
            user = User.objects.filter(code=code).first()
            if user:
                user.is_active = True
                user.save()
                return HttpResponseRedirect('/login')
    return render(request,'confirm.html' )
   
     

class SingUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = '/confirm'
    template_name = 'registration/singup.html'
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.is_active = False
        self.object.code = code()
        send_mail('код подтверждения', 
                self.object.code,
                settings.EMAIL_HOST_USER,
                [self.object.email], 
                fail_silently=False)  
        form.save()
        return super(SingUpView, self).form_valid(form)
   
    

    

