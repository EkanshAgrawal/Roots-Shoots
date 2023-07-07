from django.urls import path
from . import views

urlpatterns = [
    path('blog_home', views.blog_home, name='blogs'),
    path('blog_upload', views.blog_upload, name='uploading_blogs'),
    path('<slug:the_slug>', views.blog_details, name='blog_details'),
]
