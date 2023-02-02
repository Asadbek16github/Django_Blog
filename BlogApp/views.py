from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class All_Post_Show_View(ListView):
    model = Post
    template_name = 'all_post_view.html'


class See_Only_One_Post_View(DetailView):
    model = Post
    template_name = 'see_only_one_post.html'



class Create_new_post(CreateView):
    model = Post
    template_name = 'create_new_post.html'
    fields = ['title', 'author', 'text', 'short_info']


class Update_Post_View(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'text', 'short_info']

class Delete_Post_View(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('all_post_page')
    


