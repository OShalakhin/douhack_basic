from django.conf.urls import patterns
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'douhack_basic.views.home', name='home'),
    # url(r'^douhack_basic/', include('douhack_basic.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^m/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^s/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
