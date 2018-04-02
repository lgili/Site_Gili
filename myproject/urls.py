

import posts.views
from accounts.views import (login_view, register_view, logout_view)
from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()



urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("comments.urls", namespace='comments')),
    url(r'^about/$', posts.views.about, name='about'),
    url(r'^chat/$', posts.views.chat, name='chat'),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
	#url(r'^about/', about, name='about'),
    url(r'^', include("posts.urls", namespace='posts')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
	#url(r'^scada/$', posts.views.scada, name='scada'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

