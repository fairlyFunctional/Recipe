from django.conf.urls import patterns, url
from recipeapp import views
from recipeapp.views import RecipeUpdate, RecipeDelete

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /recipe/5/
    url(r'^(?P<recipe_id>\d+)/$', views.detail, name='detail'),
    # ex: /recipe/5/edit/
    #url(r'^(?P<recipe_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<pk>\d+)/edit/$', RecipeUpdate.as_view(), name='recipe_update'),
    #ex: /category/1/list
    url(r'^(?P<category_id>\d+)/list/$', views.list, name='list'),
    #url(r'recipe/(?P<pk>\d+)$', RecipeUpdate.as_view(), name='recipe_edit'),
    url(r'^(?P<pk>\d+)/delete/$', RecipeDelete.as_view(), name='recipe_delete'),
)