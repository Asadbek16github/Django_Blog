from django.urls import path
from .views import Sign_Up_View

urlpatterns = [
    path('signup/', Sign_Up_View.as_view(), name='sign_up_page'),
]