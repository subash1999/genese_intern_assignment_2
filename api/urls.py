from django.urls import path

from api.views import UserListAPIView

app_name = "api"
urlpatterns = [
    path("user/list", UserListAPIView.as_view({"get": "list"}), name="user_list"),
    path(
        "user/detail/<int:pk>",
        UserListAPIView.as_view({"get": "retrieve"}),
        name="user_detail",
    ),
]
