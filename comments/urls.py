# from django.urls import path
# from . import views

# urlpatterns = [
#     path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
# ]

from django.urls import path
from .views import CommentListCreate

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreate.as_view(), name='comment_list_create'),
]
