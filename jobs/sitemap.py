# sitemap.py
from django.contrib.sitemaps import Sitemap
from .models import Category, Job, QuizTitle, State, Tag
from django.urls import reverse

class JobSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Job.objects.filter(is_active=True).order_by('-updated_at')

    def lastmod(self, obj):
        return obj.updated_at
    


class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3

    def items(self):
        return Category.objects.all()
    

class StateSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.3

    def items(self):
        return State.objects.all()
    

class StaticViewSitemap(Sitemap):
    priority = 0.3
    changefreq = 'monthly'

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


class MCQSitemap(Sitemap):
    priority = 0.3
    changefreq = 'monthly'

    def items(self):
        return QuizTitle.objects.filter(is_active=True).order_by('-updated_at')

    def lastmod(self, obj):
        return obj.updated_at
    

class TagSitemap(Sitemap):
    priority = 0.3
    changefreq = 'monthly'

    def items(self):
        return Tag.objects.order_by('-updated_at')

    def lastmod(self, obj):
        return obj.updated_at