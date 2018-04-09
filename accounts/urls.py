

import posts.views
from accounts.views import (login_view, register_view, logout_view, sendERROR_view,thankyou_view)
from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views 
from django.contrib.auth.views import password_reset, password_reset_confirm, password_reset_done, password_reset_complete
admin.autodiscover()



urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^about/$', posts.views.about, name='about'),
    url(r'^chat/$', posts.views.chat, name='chat'),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^senderror/', sendERROR_view, name='senderror'),
    url(r'^thankyou/', thankyou_view, name='thankyou'),
	#url(r'^about/', about, name='about'),
    url(r'^', include("posts.urls", namespace='posts')),
    
    #url('^', include('django.contrib.auth.urls')),
    #url(r'^password_reset/$', auth_views.password_reset),
    
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
	#url(r'^scada/$', posts.views.scada, name='scada'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

