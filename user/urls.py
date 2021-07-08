from user.models import UserProfile
from django.urls import path
from user.views import LogoutMsgView, LogoutView, RegistrationForm, UserProfileView


app_name = 'user'

urlpatterns = [
    path('profile', UserProfileView.as_view(), name="profile"),

    path('register',RegistrationForm.as_view(),name='register'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('logout_msg', LogoutMsgView.as_view(),name='logout_msg'),   

]