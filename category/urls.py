from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
)

app_name = "category"
urlpatterns = [
    path("", CategoryListView.as_view(), name="list"),
    path("create", CategoryCreateView.as_view(), name="create"),
    path("<slug:slug>/update", CategoryUpdateView.as_view(), name="update"),
    path("<slug:slug>/detail", CategoryDetailView.as_view(), name="detail"),
    path("<slug:slug>/delete", CategoryDeleteView.as_view(), name="delete"),
]
