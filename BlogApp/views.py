from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class All_Post_Show_View(ListView):
    model = Post
    template_name = 'all_post_view.html'


class See_Only_One_Post_View(DetailView):
    model = Post
    template_name = 'see_only_one_post.html'

