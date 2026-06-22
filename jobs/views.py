from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Contact, Job, QuizTitle, State, Tag

# Create your views here.

def home(request):

    states = State.objects.all()

    all_jobs = Job.objects.filter(
        is_active=True
    ).order_by('-updated_at')

    featured_jobs = Job.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by('-id')[:8]

    result_jobs = Job.objects.filter(
        category__name='Results',
        is_active=True
    ).order_by('-updated_at')

    admit_cards = Job.objects.filter(
        category__name='Admit Card',
        is_active=True
    ).order_by('-updated_at')

    latest_jobs = Job.objects.filter(
        category__name='Latest Jobs',
        is_active=True
    ).order_by('-updated_at')


    syllabus = Job.objects.filter(
        category__name='Syllabus',
        is_active=True
    ).order_by('-updated_at')


    answer_keys = Job.objects.filter(
        category__name='Answer Keys',
        is_active=True
    ).order_by('-updated_at')

    document_verifications = Job.objects.filter(
        category__name='Documents',
        is_active=True
    ).order_by('-updated_at')


    admission = Job.objects.filter(
        category__name='Admission',
        is_active=True
    ).order_by('-updated_at')

    tenth_jobs = Job.objects.filter(
        category__name='12th Jobs',
        is_active=True
    ).order_by('-updated_at')

    context = {
        'result_jobs': result_jobs,
        'admit_cards': admit_cards,
        'latest_jobs': latest_jobs,
        'syllabus': syllabus,
        'answer_keys': answer_keys,
        'document_verifications': document_verifications,
        'admissions': admission,
        "featured_jobs": featured_jobs,
        "jobs": all_jobs,
        "states": states,
        "tenth_jobs": tenth_jobs
    }

    return render(request, "home2.html", context)

def single_job(request):
    return render(request, "job_detail_page.html")



def job_detail_view(request, slug):
    job = get_object_or_404(
    Job.objects.prefetch_related(
        'category',
        'job_widgets'
    ),
    slug=slug,
    is_active=True
)

    latest_jobs = Job.objects.filter(is_active=True).filter(category__name='Latest Jobs').order_by('-updated_at')[:10]
    latest_updates = Job.objects.filter(is_active=True).filter(category__name='Latest Updates').order_by('-updated_at')[:10]



    data = {
        "job": job,
        "title": job.title,
        "notification_msg": job.notification_msg,
        "slug": job.slug,
        "category": job.category.name if job.category else None,
        "short_description": job.description if job.description else 'NA',
        "total_vacancies": job.total_vacancies if job.total_vacancies else 'NA',
        "description": job.description if job.description else 'NA',
        "dates": {
            "posted_date": job.posted_date if job.posted_date else 'NA',
            "last_date": job.last_date if job.last_date else 'NA',
            "exam_date": job.exam_date if job.exam_date else 'NA',
            "updated_at": job.updated_at if job.updated_at else 'NA',
            "created_at": job.created_at if job.created_at else 'NA',
        },
        "job_widgets": job.job_widgets.all(),
        "important_links": job.official_links.all().order_by('-created_at'),
        "faqs": job.job_faqs.filter(is_active=True),
        "featured_image": job.featured_image if job.featured_image else 'NA',

        "meta_title": job.meta_title if job.meta_title else 'NA',
        "meta_description": job.meta_description if job.meta_description else 'NA',
        "keywords": job.keywords if job.keywords else 'NA',
        "latest_updates": latest_updates,
        "latest_jobs": latest_jobs,

        # "application_fees": job.fees.all()[0] if len(job.fees.all()) else 'NA',
        # "age_limit": job.age_limit.description if job.age_limit.description else 'NA',
        # "vacancies": job.vacancies.all() if len(job.vacancies.all()) else 'NA',
        # "syllabus": job.syllabus.all()[0] if len(job.syllabus.all()) else 'NA',
        # "guides": job.guides.all()[0] if len(job.guides.all()) else 'NA',
    }
    return render(request, "job_detail_page.html", {'job_info': data})

def category_jobs(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug
    )

    jobs = Job.objects.filter(
        category=category,
        is_active=True
    ).order_by('-updated_at')

    context = {
        'category': category,
        'jobs': jobs,
        'state': False
    }

    return render(request, 'category-jobs.html', context)


def state_jobs(request, slug):
    state = get_object_or_404(
        State,
        slug=slug
    )

    jobs = Job.objects.filter(
        states=state,
        is_active=True
    ).order_by('-updated_at')

    title = f"Latest updates in {state.name}"
 
    context = {
        'category': state,
        'jobs': jobs,
        'state': True,
        'title': title
    }

    return render(request, 'category-jobs.html', context)



def privacy_policy(request):
    return render(request, 'privacy.html')

def about_us(request):
    return render(request, 'about.html')

def terms_and_conditions(request):
    return render(request, 'tandc.html')

def contact(request):
    flag = False
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        contact_rectord = Contact(
            name=name,
            email=email,
            comment=comment
        )
        contact_rectord.save()
        flag = True
        return render(request, "contact.html", {"flag": flag})
    return render(request, 'contact.html')



def quiz_detail(request, quiz_slug):
    quiz = QuizTitle.objects.prefetch_related(
        'questions__options'
    ).get(slug=quiz_slug)

    jobs = Job.objects.filter(
    tags__in=quiz.tags.all()
        ).distinct()
    quizs = QuizTitle.objects.filter(tags__in=quiz.tags.all()).distinct()
    return render(
        request,
        'quiz.html',
        {
            'quiz': quiz,
            'jobs': jobs,
            'quizs': quizs
        }
    )


def tag_detail(request, tag_slug):

    tag = get_object_or_404(
        Tag,
        slug=tag_slug
    )

    tags = Tag.objects.all()

    jobs = (
        Job.objects
        .filter(tags=tag)
        .distinct()
        .order_by('-id')
    )

    quizzes = (
        QuizTitle.objects
        .filter(tags=tag)
        .distinct()
        .order_by('-id')
    )

    context = {
        "tag": tag,
        "jobs": jobs,
        "quizzes": quizzes,
        "tags": tags
    }

    return render(
        request,
        "tags.html",
        context
    )


