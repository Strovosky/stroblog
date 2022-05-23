from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path(route="", view=PostListView.as_view(), name="blog-home"),
    path(route="about-us/", view=views.about_us, name="blog-about-us"),
    path(route="my-account/", view=views.my_account, name="my-account"),
    path(route="post/<int:pk>/", view=PostDetailView.as_view(), name="detail-post"),
    path(route="post/create/", view=PostCreateView.as_view(), name='create-post'),
    path(route="post/<int:pk>/update/", view=PostUpdateView.as_view(), name='update-post'),
    path(route="post/<int:pk>/delete", view=PostDeleteView.as_view(), name='delete-post')
]
