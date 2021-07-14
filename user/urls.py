from user.models import UserProfile
from django.urls import path
from user.views import ExportUserAndPostView, LogoutMsgView, LogoutView, RegistrationForm, UpdateUserProfileView, UserMyPostView, UserProfileView, SessionExpireView


app_name = 'user'

urlpatterns = [
    path('profile', UserProfileView.as_view(), name="profile"),
    path('update_profile', UpdateUserProfileView.as_view(), name="update_profile"),

    path('export', ExportUserAndPostView.as_view(), name="export"),

    path('my_posts', UserMyPostView.as_view(), name="posts"),

    path('register',RegistrationForm.as_view(),name='register'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('logout_msg', LogoutMsgView.as_view(),name='logout_msg'), 
    path('session_expired', SessionExpireView.as_view(),name='session_expired'),   


]