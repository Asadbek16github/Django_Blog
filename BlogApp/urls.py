from django.urls import path
from .views import ( 
                        All_Post_Show_View, 
                        See_Only_One_Post_View,
                        Create_new_post,
                        Update_Post_View,
                        Delete_Post_View
                    )


urlpatterns = [
    path('', All_Post_Show_View.as_view(), name='all_post_page'),
    path('post/<int:pk>/', See_Only_One_Post_View.as_view(), name='only_post'),
    path('post/new/', Create_new_post.as_view(), name="create_post_page"),
    path('post/edit/<int:pk>/', Update_Post_View.as_view(), name='update_post'),
    path('post/delete/<int:pk>/', Delete_Post_View.as_view(), name='delete_post_page')
]