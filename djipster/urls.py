from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()
import os


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joeArtSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^galleries/$', 'artSite.views.GalleriesPage', name='galleries'),
    url(r'^galleries/(\w+)/$', 'artSite.views.ArtInGallery', name='Art in Gallery'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'artSite.views.GalleriesPage', name='root'),
    url(r'^all/$', 'artSite.views.AllArt', name='all'),
    url(r'^about/$', 'artSite.views.AboutView', name='about'),
    url(r'^(\w+)/$', 'artSite.views.ArtsInProject', name='Art in Collection'),
    
)

urlpatterns += patterns('', 
    url(r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root': os.path.join(settings.SITE_ROOT, 'static')})
)

urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root': os.path.join(settings.SITE_ROOT, 'media')})
)

