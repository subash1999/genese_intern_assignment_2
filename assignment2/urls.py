"""assignment2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from user.views import LogoutMsgView, LogoutView, RegistrationForm

from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("", home),
    path("category/", include("category.urls")),
    path("post/", include("post.urls")),
    path("user/", include("user.urls")),
    path("api/", include("api.urls")),
    path("register", RegistrationForm.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("logout_msg", LogoutMsgView.as_view(), name="logout_msg"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
