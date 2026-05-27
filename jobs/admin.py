from django.contrib import admin
from .models import (Contact, Job, JobFaqs, JobWidget, Category, Organization, JobLink, SocialLink, SEOSetting)


admin.site.site_header = "SarkariJobsFind.com"      # Text in the large <h1> header
admin.site.site_title = "SarkariJobsFind.com Admin"  # Text in the browser tab <title>
admin.site.index_title = "Welcome SarkariJobsFind.com Admin Panel"  # Text on the admin index page


@admin.register(SEOSetting)
class SEOSettingAdmin(admin.ModelAdmin):
    list_display = (
        'meta_title',
        'meta_description'
    )


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ('name',)

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
        'title'
    )
    search_fields = ('name',)

    def get_job_title(self, obj):
        return obj.job.title
    

@admin.register(JobFaqs)
class JobfaqAdmin(admin.ModelAdmin):
    list_display = (
        'get_job_title',
        'title',
        'is_active'
    )
    search_fields = ('get_job_title', 'title')
    list_filter = ('is_active',)

    def get_job_title(self, obj):
        return obj.job.title

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
            'title',
            'is_active'
        )
    search_fields = ('title',)
    list_filter = ('is_active', 'is_featured')


@admin.register(JobWidget)
class JobWidgetAdmin(admin.ModelAdmin):
    list_display = (
            'get_job_title',
            'title',
            'is_active'
        )
    search_fields = ('name',)

    def get_job_title(self, obj):
        return obj.job.title
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'email')
    ordering = ['-created_at']
    
