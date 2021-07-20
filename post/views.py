from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from post.models import Post


# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Post
    queryset = Post.objects.all().annotate()


class PostDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "post"
    queryset = Post.objects.all()


class PostCreateView(LoginRequiredMixin, CreateView):
    context_object_name = "post"
    model = Post
    fields = [
        "category",
        "title",
        "body",
    ]

    def get_success_url(self):
        return reverse("post:detail", kwargs={"slug": self.object.slug})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    context_object_name = "post"
    model = Post
    fields = [
        "category",
        "title",
        "body",
    ]

    def get_success_url(self):
        return reverse("post:detail", kwargs={"slug": self.object.slug})

    def test_func(self):
        return test_post_update_delete_permission(self.kwargs["slug"], self.request)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post:list")

    def test_func(self):
        return test_post_update_delete_permission(self.kwargs["slug"], self.request)


class PostSearchView(ListView):
    template_name = "post/post_search.html"
    model = Post
    paginate_by = 5
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["count"] = self.count or 0
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        title = self.request.GET.get("q")
        object_list = self.model.objects.all()
        if title:
            print("\n" * 5 + title + "\n" * 5)
            object_list = object_list.filter(title__icontains=title)
        self.count = object_list.count()
        return object_list


def test_post_update_delete_permission(slug, request):
    post = get_object_or_404(Post, slug=slug)
    permission = False
    if hasattr(post, "user"):
        if post.user is not None:
            permission = post.user.id == request.user.id
    return request.user.is_superuser or permission


def home(request):
    posts = Post.objects.order_by("-created_at")
    no_of_posts = posts.count() if posts.count() < 10 else 10
    return render(request, "home.html", {"posts": posts[:no_of_posts]})
