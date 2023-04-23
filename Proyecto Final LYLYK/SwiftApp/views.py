from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from SwiftApp.models import Post
from django.urls import reverse_lazy


def index(request):
    return render(request,"SwiftApp/index.html")


class PostList(ListView):
    model = Post 

class PostDetail(DetailView):
    model = Post 

class PostCreate(CreateView):
    model = Post 
    success_url = reverse_lazy("post-list")
    fields = '__all__'


class PostUpdate(UpdateView):
    model = Post 
    success_url = reverse_lazy("post-list")
    fields = '__all__'


class PostDelete(DeleteView):
    model = Post 
    success_url = reverse_lazy("post-list")