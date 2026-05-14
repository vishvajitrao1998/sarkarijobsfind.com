
from django.urls import path

from .views import *

urlpatterns = [
    path("", home, name="home"),
    # path("up-scholorship-status", single_job, name="home"),
    path("<str:slug>", job_detail_view, name="job_detail_view"),

]