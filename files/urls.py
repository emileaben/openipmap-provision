from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^openipmap(/)*', include('openipmap.urls', namespace="openipmap")),
   url(r'^admin/', include(admin.site.urls)),
   #url(r'^accounts/login/$', auth_views.login, {'template_name': 'myapp/login.html'}),
   url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
   url(r'^$', TemplateView.as_view(template_name="index.html") ),
   url(r'^', TemplateView.as_view(template_name="404.html") ),
)
