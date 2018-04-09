from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site

from posts.models import Post
#from posts.models import Item

class TodoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
    	return Post.objects.all()
    #def items(self):
     #   return Post.objects.filter(is_draft=False)
	
	def lastmod(self, obj):
		return obj.publish       