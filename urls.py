# -*- coding: utf-8 -*-
from django.conf.urls import defaults
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from django.contrib import admin

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + defaults.patterns('',
    (r'^$', defaults.include('home.urls')),
    (r'^resume/', defaults.include('resume.urls')),
    (r'^photos/', defaults.include('photos.urls')),
    (r'^portfolio/', defaults.include('portfolio.urls')),
    (r'^blog/', defaults.include('blog.urls')),
) + urlpatterns