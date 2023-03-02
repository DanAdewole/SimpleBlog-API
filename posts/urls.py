from django.urls import path

from .views import (
    homepage, 
    PostListCreateView, 
    PostRetrieveUpdateDeleteView,
    get_current_user_posts,
    ListPostsForAuthor
)

urlpatterns = [
    path("homepage", homepage, name="posts_home"),
    # path("", list_posts, name="lists_posts"),
    path("", PostListCreateView.as_view(), name="list_posts"),
    path("<int:pk>", PostRetrieveUpdateDeleteView.as_view(), name="post_detail"),
    path("current_user/", get_current_user_posts, name="current_user"),
    path(
        "posts_for/", 
        ListPostsForAuthor.as_view(),
        name="posts_for_current_user"
    )
    # path("<int:post_id>", post_detail, name="post_detail"),
    # path("update/<int:post_id>", update_post, name="update_post"),
    # path("delete/<int:post_id>", delete_post, name="delete_post"),
]
