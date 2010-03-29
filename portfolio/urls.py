# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('portfolio.views',
    (r'^$', 'list_portfolio'),
)
