from django.urls import path

from api.views import UserList

app_name = "api"
urlpatterns = [path("user/list", UserList.as_view(), name="user_list")]
