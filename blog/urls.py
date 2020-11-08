from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeletelView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('blog/<int:id>/', ArticleDetailView.as_view(), name='article_detail_view'),
    path('createArticle/', ArticleCreateView.as_view(), name = 'article_create_view'),
    path('blog/<int:id>/update/', ArticleUpdateView.as_view(), name='article_update_view'),
    path('blog/<int:id>/delete/', ArticleDeletelView.as_view(), name='article_delete_view'),

]