from django.contrib import admin
from .models import (
    Category,
    Organization,
    Job,
    JobImportantDate,
    JobApplicationFee,
    JobAgeLimit,
    JobVacancy,
    JobSyllabus,
    SocialLink,
    Guide,
    State,
    JobLink
)
from django.contrib import admin
from django.utils.safestring import mark_safe

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        'platform',
        'title',
        'is_active'
    )

    list_editable = ('is_active',)
    list_filter = ('platform', 'is_active')
    search_fields = ('platform', 'title')


    fieldsets = (
        ("Basic Info", {
            'fields': ('platform', 'title', 'url')
        }),
        ("Display Settings", {
            'fields': ('icon_class', 'is_active')
        }),
    )

    # def preview_icon(self, obj):
    #     if obj.icon_class:
    #         return f'<i class="{obj.icon_class}"></i>'
    #     return "-"
    # preview_icon.allow_tags = True
    # preview_icon.short_description = "Icon"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


@admin.register(JobLink)
class JobLinkAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'title',
        'is_active'
    )
    search_fields = ('name',)

    def get_job_title(self, obj):
        return obj.job.title


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(JobImportantDate)
class JobImportantDateAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'title',
        'is_active'
    )
    search_fields = ('title','job_title',)

    def get_job_title(self, obj):
        return obj.job.title
    

@admin.register(JobAgeLimit)
class JobAgeLimitAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'min_age',
        'max_age',
        'is_active'
    )
    search_fields = ('job_title',)

    def get_job_title(self, obj):
        return obj.job.title
    

@admin.register(JobVacancy)
class JobVacancyAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'post_name',
        'total_posts',
        'is_active'
    )
    search_fields = ('get_job_title','post_name')

    def get_job_title(self, obj):
        return obj.post_name
    

@admin.register(JobSyllabus)
class JobSyllabusAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'subject',
        'is_active'
    )
    search_fields = ('get_job_title','subject')

    def get_job_title(self, obj):
        return obj.subject
    

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'title'
    )
    search_fields = ('get_job_title','title')

    def get_job_title(self, obj):
        return obj.title


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organization',
        'category',
        'last_date',
        'is_active',
        'is_featured',
        'created_at',
    )

    list_filter = ('category', 'organization','total_vacancies', 'is_active', 'is_featured')
    search_fields = ('title', 'organization__name')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('states',)

    # inlines = [
    #     JobImportantDateInline,
    #     JobApplicationFeeInline,
    #     JobVacancyInline,
    #     JobSyllabusInline,
    #     OfficialLinkInline,
    # ]

    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'slug', 'category', 'organization', 'total_vacancies')
        }),
        ("Content", {
            'fields': ('short_description', 'description')
        }),
        ("Dates", {
            'fields': ('last_date', 'exam_date')
        }),
        ("Status", {
            'fields': ('is_active', 'is_featured')
        }),
        ("SEO", {
            'fields': ('meta_title', 'meta_description', 'keywords')
        }),
        ("Filters", {
            'fields': ('states',)
        }),
    )



