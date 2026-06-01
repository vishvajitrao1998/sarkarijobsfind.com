
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemap import CategorySitemap, JobSitemap, MCQSitemap, StateSitemap, StaticViewSitemap, TagSitemap

sitemaps = {
    'jobs': JobSitemap,
}
categories_sitemaps = {
    'categories': CategorySitemap,

}
states_sitemaps = {
    'states': StateSitemap
}
static_sitemaps = {
    'static': StaticViewSitemap
}
mcqs_sitemaps = {
    'mcq': MCQSitemap
}
tags_sitemaps = {
    'tags': TagSitemap
}

urlpatterns = [
    path("", home, name="home"),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'categories/sitemap.xml',
        sitemap,
        {'sitemaps': categories_sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'states/sitemap.xml',
        sitemap,
        {'sitemaps': states_sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'page/sitemap.xml',
        sitemap,
        {'sitemaps': static_sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'mcqs/sitemap.xml',
        sitemap,
        {'sitemaps': mcqs_sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'tags/sitemap.xml',
        sitemap,
        {'sitemaps': tags_sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path("<str:slug>", job_detail_view, name="job_detail_view"),
    path("category/<str:slug>", category_jobs, name="category_jobs"),
    path("state/<str:slug>", state_jobs, name="state_jobs"),
    path("mcq/<str:quiz_slug>", quiz_detail, name="quiz_detail"),
    path("tag/<str:tag_slug>", tag_detail, name="tag_detail"),
    path("p/privacy-policy", privacy_policy, name="privacy_policy"),
    path("p/about-us", about_us, name="about_us"),
    path("p/terms-and-conditions", terms_and_conditions, name="terms_and_conditions"),
    path("p/contact", contact, name="contact"),

]





urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)