from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Abs, Comment
from .forms import CommentForm,AbsForm
from .filter import CommentAbsFilter

class Posts(ListView):
    model = Abs
    paginate_by = 50
    template_name = 'home.html'
    context_object_name = 'posts'
  
  
class CreateComment(CreateView):
    model = Comment
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            return HttpResponseRedirect(f'/detail/{instance.abs.pk}')
        return HttpResponseRedirect(f'/detail/{form.cleaned_data["abs"].pk}')
    
   
class PostCreate(CreateView):
    model = Abs
    context_object_name = 'post'
    template_name = 'create_post.html'
    form_class = AbsForm
    
    def post(self, request, *args, **kwargs):
        form = AbsForm(request.POST, request.FILES)
        form.is_valid()
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            return HttpResponseRedirect(f'/detail/{instance.pk}')
        return HttpResponseRedirect('/create_post')  
    
 
class PostDetail(DetailView):
    model = Abs
    context_object_name = 'post'
    template_name = 'detail_post.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        comments = Comment.objects.filter(abs = context['object'])
        context['commets'] = comments
        return context
    
    
def profil_list(request):
    f = CommentAbsFilter(request.GET, queryset=Comment.objects.filter(abs__user = request.user))
    return render(request, 'profile.html', {'filter': f})  

def success_button(request, pk):
     comment = Comment.objects.get(pk= pk)
     comment.success_comment() 
     return HttpResponseRedirect('/profile')
 
def delete_button(request, pk):
     comment = Comment.objects.get(pk= pk)
     comment.delete() 
     return HttpResponseRedirect('/profile')