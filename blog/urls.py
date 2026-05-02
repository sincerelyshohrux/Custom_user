from django.urls import path
from blog import views

urlpatterns=[
    path('',views.get_blog,name='list'),
    path('create/blog/',views.create_blog,name='create-blog'),
    path('detail/<int:id>/', views.blog_detail, name='detail'),
]