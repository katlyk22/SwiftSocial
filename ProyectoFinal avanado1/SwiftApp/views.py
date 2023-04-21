from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from SwiftApp.models import Post



def index(request):
    return render(request,"SwiftApp/index.html")


class PostList(ListView):
    model = Post 

class PostDetail(DetailView):
    model = Post 
