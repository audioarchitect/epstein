from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
  
    # homepage routes
    url( r'^$', 			'apps.home.views.index',  name='home' ),

    #users routes
    url( r'^users/$', 	 	'apps.users.views.index', 	name='home' ),
    url( r'^users/new$', 	'apps.users.views.new', 	name='home' ),
    url( r'^users/create$', 'apps.users.views.create',     name='home' ),
    url( r'^users/login$', 	'apps.users.views.do_login', 	name='home' ),
    url( r'^users/logout$', 'apps.users.views.do_logout',    name='home' ),
    url( r'^dashboard/$',   'apps.users.views.dashboard',   name='bands' ),

    #bands routes
    url( r'^bands/$',       'apps.bands.views.show_bands',  name='show_bands' ),
    url( r'^band/$',        'apps.bands.views.dashboard',  name='show_bands' ),
   
    # event routes
    url( r'^events/$',      'apps.events.views.events',  name='home' ),

    # setlist routes
    url( r'^setlist/$',     'apps.setlists.views.setlist',  name='setlist' ),

    # basically hacks for now... need to clean up
    url( r'^about/$', 		'apps.users.views.about',  name='home' ),

    # admin routes
    #url( r'^admin/doc/', include('django.contrib.admindocs.urls') ),
    #url( r'^admin/', 	include(admin.site.urls) ),
)
