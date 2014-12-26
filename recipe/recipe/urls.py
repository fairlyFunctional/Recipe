from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipe/',include('recipeapp.urls', namespace="recipe")),
    url(r'^category/',include('recipeapp.urls', namespace="category")),
    #url(r'^$',views.index, name='index'),
)
