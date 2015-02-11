from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

import mysite.views.personal
import mysite.views.hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mysite.views.personal.personal),
    url(r'^hello$', mysite.views.hello.hello),
)

urlpatterns += staticfiles_urlpatterns()
