from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class All_Post_Show_View(ListView):
    model = Post
    template_name = 'all_post_view.html'
