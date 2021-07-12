from user.models import UserProfile
from django.urls import path
from user.views import LogoutMsgView, LogoutView, RegistrationForm, UpdateUserProfileView, UserMyPostView, UserProfileView


app_name = 'user'

urlpatterns = [
    path('profile', UserProfileView.as_view(), name="profile"),
    path('update_profile', UpdateUserProfileView.as_view(), name="update_profile"),

    path('my_posts', UserMyPostView.as_view(), name="posts"),

    path('register',RegistrationForm.as_view(),name='register'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('logout_msg', LogoutMsgView.as_view(),name='logout_msg'),   

]