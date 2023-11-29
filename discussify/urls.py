from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from discussify import views
from discussify.views import PostListView, PostDetailView, SearchListView

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("search/", SearchListView.as_view(), name="search"),
    path("posts/new", views.new_post, name="new_post"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/comments/new", views.comment, name="new_comment")
]

urlpatterns += staticfiles_urlpatterns()