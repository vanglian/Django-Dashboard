from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'SocialIQ.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^textanalytics/',include('textanalytics')),
    url(r'^textanalytics/', include('textanalytics.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
