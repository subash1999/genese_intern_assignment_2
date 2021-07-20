from django.urls import path

from api.views import PostDetailAPIView, PostListAPIView

app_name = "api"
urlpatterns = [
    path("api_view/post", PostListAPIView.as_view(), name="post_api"),
    path(
        "api_view/post/<int:pk>",
        PostDetailAPIView.as_view(),
        name="post_api_detail",
    ),
]
