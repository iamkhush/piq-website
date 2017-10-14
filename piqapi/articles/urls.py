"""articles URL Configuration."""

from django.conf.urls import url

from views import ArticleListView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article-list'),
]
