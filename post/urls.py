from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index_page"),

    path("posts/", views.all_posts, name="all_posts"),

    path("posts/new", views.create_post, name="create_post"),

    path("posts/<int:post_id>", views.single_post, name="single_post"),

    # UPDATE
    path(
        "posts/<int:post_id>/edit/",
        views.edit_post,
        name="edit_post"
    ),

    # DELETE
    path(
        "posts/<int:post_id>/delete/",
        views.delete_post,
        name="delete_post"
    ),
]