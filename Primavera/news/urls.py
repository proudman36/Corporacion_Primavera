from django.urls import path
from . import views 

urlpatterns = [
    path('news/', views.index,name='index'),
    path('post_news/',views.post_news,name="post_news")
]
