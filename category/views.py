from django.db.models.aggregates import Count
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from category.models import Category
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='get')
class CategoryListView(ListView):
    paginate_by = 5
    model = Category
    queryset = Category.objects.all().annotate(posts_count=Count('post'))


@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='get')
class CategoryDetailView(DetailView):
    context_object_name = 'category'
    queryset = queryset = Category.objects.all().annotate(posts_count=Count('post'))


@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='post')
@method_decorator(login_required,name='get')
class CategoryCreateView(UserPassesTestMixin,CreateView):
    context_object_name = 'category'
    model = Category
    fields = [
        'name',
        'description'
    ]
    def get_success_url(self):
        return reverse('category:detail',kwargs={'slug':self.object.slug})

    def test_func(self):
        return self.request.user.is_superuser 


@method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='post')
@method_decorator(login_required,name='get')
class CategoryUpdateView(UserPassesTestMixin,UpdateView):
    context_object_name = 'category'
    model = Category
    fields = [
        'name',
        'description'
    ]
    def get_success_url(self):
        return reverse('category:detail',kwargs={'slug':self.object.slug})

    def test_func(self):
        return self.request.user.is_superuser 


@method_decorator(login_required,name='dispatch')
class CategoryDeleteView(UserPassesTestMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')

    def test_func(self):
        return self.request.user.is_superuser 

