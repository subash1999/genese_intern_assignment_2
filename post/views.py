from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from django.forms import widgets
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.base import View
from post.models import Post
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='get')
class PostListView(ListView):
    paginate_by = 5
    model = Post
    queryset = Post.objects.all().annotate()


@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='get')
class PostDetailView(DetailView):
    context_object_name = 'post'
    queryset = Post.objects.all()


@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='post')
@method_decorator(login_required,name='get')
class PostCreateView(CreateView):
    context_object_name = 'post'
    model = Post
    fields = [
        'category',
        'title',
        'body',        
    ]

    def get_success_url(self):
        return reverse('post:detail',kwargs={'slug':self.object.slug})


@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='post')
@method_decorator(login_required,name='get')
class PostUpdateView( UserPassesTestMixin, UpdateView):
    context_object_name = 'post'
    model = Post
    fields = [
        'category',
        'title',
        'body',        
    ] 

    def get_success_url(self):
        return reverse('post:detail',kwargs={'slug':self.object.slug})

    def test_func(self):
        return test_post_update_delete_permission(self.kwargs['slug'],self.request)


@method_decorator(login_required,name='dispatch')
class PostDeleteView(UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')

    def test_func(self):
        return test_post_update_delete_permission(self.kwargs['slug'],self.request)

class PostSearchView(ListView):
    template_name = 'post/post_search.html'
    model = Post
    paginate_by = 5
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        title = self.request.GET.get('q')
        object_list = self.model.objects.all()
        if title:
            print("\n"*5+title+"\n"*5)
            object_list = object_list.filter(title__icontains=title)
        self.count = object_list.count()
        return object_list

def test_post_update_delete_permission(slug, request):
    post = get_object_or_404(Post, slug = slug)
    permission = False
    if hasattr(post, 'user'):
        if(post.user is not None):
            permission = (post.user.id == request.user.id)
    return request.user.is_superuser or permission



