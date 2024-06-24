from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name="new-post") , #MUST BE AboVE THE SLUG
    path('<slug:slug>', views.post_page, name="page"),
]