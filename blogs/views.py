from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.


def HomeView(request):
    return render(request, 'blogs/home.html')


class DetailView(generic.DetailView):
    model = Post
    template_name ='blogs/detail.html'