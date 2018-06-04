from django.conf.urls import url , include

from . import views



urlpatterns = [
    url(r'^buck_new/$', views.buck_new, name='buck_new'), 
    
    
    

]