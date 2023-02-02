from django.urls import path
from .views import ( 
                        All_Post_Show_View, 
                        See_Only_One_Post_View
                    )


urlpatterns = [
    path('', All_Post_Show_View.as_view(), name='all_post_page'),
    path('post/<int:pk>/', See_Only_One_Post_View.as_view(), name='only_post')
]