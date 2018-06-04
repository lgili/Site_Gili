from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from posts.models import Post
#from posts.models import Item

class TodoSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5


    def items(self):
        # Return list of url names for views to include in sitemap
        return ['about','buck','boost','buck_boost','flyback','forward','push_pull','half_bridge','full_bridge','register',
        'login','senderror','thankyou']

    def location(self, item):
        return reverse(item)

    #def items(self):
    #	return Post.objects.all()
    #def items(self):
     #   return Post.objects.filter(is_draft=False)
     
	
	

		     