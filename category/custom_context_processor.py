from .models import Category
from django.db.models import Count

def category_renderer(request):
    all = Category.objects.annotate(num_post=Count('post')).order_by('-num_post')
    _top_categories = []
    max_range = all.count() if all.count()<5 else 5
    for c in range(0,max_range,1):
        _top_categories.append(all[c])

    return {
       'all_categories': Category.objects.all(),
       'top_categories': _top_categories,
    }

