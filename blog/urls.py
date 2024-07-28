# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]


# from django.urls import path
# from . import views
# from .views import PostListCreate, PostDetail

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
#     path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
#     path('api/posts/', PostListCreate.as_view(), name='post_list_create'),
#     path('api/posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('posts/', views.PostListCreate.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail_api'),
]
