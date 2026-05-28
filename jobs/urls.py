
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("<str:slug>", job_detail_view, name="job_detail_view"),
    path("category/<str:slug>", category_jobs, name="category_jobs"),


    path("p/privacy-policy", privacy_policy, name="privacy_policy"),
    path("p/about-us", about_us, name="about_us"),
    path("p/terms-and-conditions", terms_and_conditions, name="terms_and_conditions"),
    path("p/contact", contact, name="contact"),

]





urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)