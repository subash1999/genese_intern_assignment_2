from django.shortcuts import render
from post.models import Post 

def home(request):
    posts = Post.objects.order_by('-created_at')
    no_of_posts = posts.count() if posts.count()<10 else 10
    return render(request,'home.html', { 'posts' : posts[:no_of_posts] } )