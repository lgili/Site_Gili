

import posts.views
import ccccjs.views
#from ccccjs.views import (ccccjs)
from accounts.views import (login_view, register_view, logout_view, sendERROR_view,thankyou_view,password_reset_view)
from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static
from django.contrib import admin
#from django.contrib.sites.models import Site
#from django.contrib.auth.views import  password_reset_confirm, password_reset_done, password_reset_complete
admin.autodiscover()


from django.contrib.sitemaps.views import sitemap
from sitemaps import TodoSitemap
sitemaps = {
    'post': TodoSitemap
}
#from django.contrib.sitemaps import views
urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    
    #url(r'^robots.txt$', include('robots.urls')),
    #url(r'^robots\.txt', include('robots.urls')),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^about/$', posts.views.about, name='about'),
    url(r'^buck/', posts.views.buck, name='buck'),
    url(r'^boost/', posts.views.boost, name='boost'),
    url(r'^buck_boost/', posts.views.buck_boost, name='buck_boost'),
    url(r'^flyback/', posts.views.flyback, name='flyback'),
    url(r'^forward/', posts.views.forward, name='forward'),
    url(r'^push_pull/', posts.views.push_pull, name='push_pull'),
    url(r'^half_bridge/', posts.views.half_bridge, name='half_bridge'),
    url(r'^full_bridge/', posts.views.full_bridge, name='full_bridge'),
    #url(r'^ccccjs/#tab2', posts.views.ccccjs, name='ccccjs1'),
    url(r'^chat/$', posts.views.chat, name='chat'),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^senderror/', sendERROR_view, name='senderror'),
    url(r'^thankyou/', thankyou_view, name='thankyou'),
	#url(r'^about/', about, name='about'),
    url(r'^', include("posts.urls", namespace='posts')),
    url(r'^', include("ccccjs.urls", namespace='ccccjs')),
    

    #url(r'^', include("ccccjs.urls", namespace='ccccjs')),
    #url(r'^ccccjs/', ccccjs.views.ccccjs, name='ccccjs'),
    #url('^', include('django.contrib.auth.urls')),
    #url(r'^password_reset/$', auth_views.password_reset),
    
    url(r'^password_reset/$', password_reset_view, name='password_reset'),
    #url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
	#url(r'^scada/$', posts.views.scada, name='scada'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},    name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

