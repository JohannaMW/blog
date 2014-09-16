from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bloggy.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/new/$', 'blog.views.add_comment', name = "add_comment"),
    url(r'^blogpost/new/$', 'blog.views.add_blogpost', name='add_blogpost'),
    url(r'^author/new/$', 'blog.views.add_author', name='add_author'),
    url(r'^tag/new/$', 'blog.views.add_tag', name='add_tag'),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    url(r'^/', 'blog.views.home', name='home'),
)
