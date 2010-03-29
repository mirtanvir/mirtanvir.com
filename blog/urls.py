from django.conf.urls import defaults

urlpatterns = defaults.patterns('blog.views',
    (r'^$', 'list_blog_entries'),
    (r'^show/(\d+)/$', 'show_single_blog'),
    
)

urlpatterns += defaults.patterns('blog.rpc',
    (r'^rpc/get_sidebar_blog_title$', 'list_sidebar_blog_title'),
)
