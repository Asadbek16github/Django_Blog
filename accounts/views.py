from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Sign_Up_View(CreateView):
    form_class = UserCreationForm
    success_url = 'all_post_page'
    template_name = 'registration/signup.html'
