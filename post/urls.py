from django.urls import path
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, PostSearchView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(),name='list'),
    path('create', PostCreateView.as_view(), name="create"),
    path('<slug:slug>/update', PostUpdateView.as_view(), name="update"),
    path('<slug:slug>/detail', PostDetailView.as_view(), name="detail"),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name="delete"),
    path('search', PostSearchView.as_view(), name="search"),
]