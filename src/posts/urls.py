from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDetail, BlogPostDelete
from posts import views


app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create") , # On ajoute ce chemin d'URL
    path('<str:slug>/', BlogPostDetail.as_view(), name="post"),  # On rajoute ce chemin
   # path('original-url/', views.original_view),
    #path('another-url/', views.another_view, name='named-url'),
    path('edit/<str:slug>/', BlogPostEdit.as_view(), name="edit"),
    path('delete/<str:slug>/', BlogPostDelete.as_view(), name="delete"),  # On ajoute la vue delete
]
