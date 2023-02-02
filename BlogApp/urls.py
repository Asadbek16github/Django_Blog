from django.urls import path
from .views import All_Post_Show_View


urlpatterns = [
    path('', All_Post_Show_View.as_view(), name='all_post_page')
]