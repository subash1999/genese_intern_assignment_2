from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import (
    PostCreateGenericView,
    PostDestroyGenericView,
    PostDetailAPIView,
    PostListAPIView,
    PostListCreateGenericView,
    PostListGenericView,
    PostModelViewSet,
    PostRetrieveDestroyGenericView,
    PostRetrieveGenericView,
    PostRetrieveUpdateDestroyGenericView,
    PostRetrieveUpdateGenericView,
    PostUpdateGenericView,
)

app_name = "api"

# model view set
router = DefaultRouter()
router.register("model_view/post", PostModelViewSet, basename="post")

urlpatterns = [
    # api view
    path("api_view/post", PostListAPIView.as_view(), name="post-api"),
    path(
        "api_view/post/<int:pk>",
        PostDetailAPIView.as_view(),
        name="post-detail-api",
    ),
    # generic view
    path(
        "generic_view/post/create",
        PostCreateGenericView.as_view(),
        name="post-create-api",
    ),
    path("generic_view/post/list", PostListGenericView.as_view(), name="post-list-api"),
    path(
        "generic_view/post/retrieve/<int:pk>",
        PostRetrieveGenericView.as_view(),
        name="post-retrieve-api",
    ),
    path(
        "generic_view/post/destroy/<int:pk>",
        PostDestroyGenericView.as_view(),
        name="post-destroy-api",
    ),
    path(
        "generic_view/post/update/<int:pk>",
        PostUpdateGenericView.as_view(),
        name="post-update-api",
    ),
    path(
        "generic_view/post/list-create",
        PostListCreateGenericView.as_view(),
        name="post-list-create-api",
    ),
    path(
        "generic_view/post/retrieve-update/<int:pk>",
        PostRetrieveUpdateGenericView.as_view(),
        name="post-retrieve-update-api",
    ),
    path(
        "generic_view/post/retrieve-destroy/<int:pk>",
        PostRetrieveDestroyGenericView.as_view(),
        name="post-retrieve-destroy-api",
    ),
    path(
        "generic_view/post/retrieve-update-destroy/<int:pk>",
        PostRetrieveUpdateDestroyGenericView.as_view(),
        name="post-retrieve-update-destroy-api",
    ),
] + router.urls
