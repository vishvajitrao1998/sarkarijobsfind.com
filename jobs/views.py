from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Job

# Create your views here.

def home(request):
    return render(request, "home2.html")


def single_job(request):
    return render(request, "job_detail_page.html")



def job_detail_view(request, slug):
    job = get_object_or_404(
        Job.objects.select_related('category')
        .prefetch_related(
            'job_wigets'
        ),
        slug=slug,
        is_active=True
    )

    data = {
        "title": job.title,
        "slug": job.slug,
        "category": job.category.name if job.category else None,
        "short_description": job.short_description if job.short_description else 'NA',
        "total_vacancies": job.total_vacancies if job.total_vacancies else 'NA',
        "description": job.description if job.description else 'NA',
        "dates": {
            "posted_date": job.posted_date if job.posted_date else 'NA',
            "last_date": job.last_date if job.last_date else 'NA',
            "exam_date": job.exam_date if job.exam_date else 'NA',
        },
        "job_wigets": job.job_wigets.all() if len(job.job_wigets.all()) else 'NA',
        "important_links": job.official_links.all() if len(job.official_links.all()) else 'NA',
        # "application_fees": job.fees.all()[0] if len(job.fees.all()) else 'NA',
        # "age_limit": job.age_limit.description if job.age_limit.description else 'NA',
        # "vacancies": job.vacancies.all() if len(job.vacancies.all()) else 'NA',
        # "syllabus": job.syllabus.all()[0] if len(job.syllabus.all()) else 'NA',
        # "guides": job.guides.all()[0] if len(job.guides.all()) else 'NA',
    }

    print(data)

    return render(request, "job_detail_page.html", {'job_info': data})
