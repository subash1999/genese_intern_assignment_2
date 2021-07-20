from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.aggregates import Count
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from category.models import Category


# Create your views here.
class CategoryListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Category
    queryset = Category.objects.all().annotate(posts_count=Count("post"))


class CategoryDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "category"
    queryset = queryset = Category.objects.all().annotate(posts_count=Count("post"))


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    context_object_name = "category"
    model = Category
    fields = ["name", "description"]

    def get_success_url(self):
        return reverse("category:detail", kwargs={"slug": self.object.slug})

    def test_func(self):
        return self.request.user.is_superuser


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    context_object_name = "category"
    model = Category
    fields = ["name", "description"]

    def get_success_url(self):
        return reverse("category:detail", kwargs={"slug": self.object.slug})

    def test_func(self):
        return self.request.user.is_superuser


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("category:list")

    def test_func(self):
        return self.request.user.is_superuser
