from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'videoscrapping.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    # Redirect to show video width uuid
    url(r'^video/(?P<uuid>[^/]+)/$', 'video.views.video', name='video'),
    # Redirect to index
    url(r'^$', 'video.views.index', name='index'),
    url(r'^flickr/$', 'video.views.flickr', name='flickr'),

    # ----------------------------- API -------------------------------
    # like video
    url(r'^api/(?P<uuid>[^/]+)/like/$', 'video.views.like', name='like'),
    url(r'^api/(?P<uuid>[^/]+)/unlike/$', 'video.views.unlike', name='unlike'),

    # ----------------------------- API -------------------------------
    # Authentication
    url(r'^users/singup/$', 'video.views.new_user', name='new_user'),
    url(r'^users/login/$', 'video.views.login_user', name='login_user'),
    url(r'^users/logout/$', 'video.views.logout_user', name='logout_user')
)
