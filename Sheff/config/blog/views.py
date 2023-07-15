from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


#def home(request):
#    return render(request, 'base.html')

class HomeView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/home.html'


class PostListView(DetailView):
    model = Post

    """фильтрация постов по списку категорий"""
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')
    """.select_related('category') для запросов в бд"""


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    """переопределили из-за urls(<slug:slug>/<slug:post_slug>) """

    context_object_name = 'post'
    """как будет именоваться переменнная в шаблоне post_detail"""