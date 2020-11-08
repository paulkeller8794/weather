from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404
from .models import Article
from .form import ArticleForm
from django.urls import reverse

# Create your views here.

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()  # list of objects   #<blog>/<modelname>_list.html


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeletelView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("article-list")

