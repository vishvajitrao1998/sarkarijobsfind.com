# sitemap.py
from django.contrib.sitemaps import Sitemap
from .models import Category, Job, State
from django.urls import reverse

class JobSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.9

    def items(self):
        return Job.objects.filter(is_active=True).order_by('-updated_at')

    def lastmod(self, obj):
        return obj.updated_at
    


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()
    

class StateSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return State.objects.all()
    

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return [
            'home',
            'privacy_policy',
            'terms_and_conditions',
            'about_us',
            'contact',
        ]

    def location(self, item):
        return reverse(item)