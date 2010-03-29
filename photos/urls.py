from django.conf.urls import defaults

urlpatterns = defaults.patterns('photos.views',
    (r'^$', 'list_albums'),
    (r'^album/(\d+)/photo/(\d+)/$', 'show_single_photo'),
    (r'^album/(\d+)/photo/(\d+)/next/(\d+)/$', 'show_single_photo'),
    (r'^album/(\d+)/photo/(\d+)/prev/(\d+)/$', 'show_single_photo'),
    (r'^album/(\d+)/photo/(\d+)/next/(\d+)/prev/(\d+)/$', 'show_single_photo'),
    (r'^album/(\d+)/$', 'list_album_pictures'),
)

urlpatterns += defaults.patterns('photos.rpc',
    (r'^rpc/get_thumb_list$', 'album_thumb_images'),
)
