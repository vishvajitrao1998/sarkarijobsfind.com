from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, blank=True)  # optional (for UI)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"
    
class Organization(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    states = models.ManyToManyField(State, blank=True)

    short_description = models.TextField()
    description = models.TextField()

    total_vacancies = models.IntegerField(null=True, blank=True)

    # Dates
    posted_date = models.DateField(auto_now_add=True)
    last_date = models.DateField(null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)

    # Links
    apply_link = models.URLField()
    official_notification = models.URLField()

    # Status
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    # SEO
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)

    in_featured_list = models.BooleanField(default=False)
    in_top_list = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class JobWidget(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_wigets')
    title = models.CharField(max_length=100)  # e.g. "Application Start"
    description = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job.title} -> {self.title}"
    
    class Meta:
        verbose_name = 'Job Widget'
        verbose_name_plural = 'Job Widgets'



class JobLink(models.Model):
    job = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE,
        related_name='official_links'
    )
    title = models.CharField(max_length=255)  # Custom text (optional override)
    url = models.URLField()
    is_primary = models.BooleanField(default=False)  # highlight button
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Job Link"
        verbose_name_plural = "Job Links"

    def __str__(self):
        return f"{self.job.title}"


class SocialLink(models.Model):
    PLATFORM_CHOICES = (
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('twitter', 'Twitter'),
        ('other', 'Other'),
    )

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    title = models.CharField(max_length=200)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, blank=True)  # for UI icons
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

    def __str__(self):
        return f"{self.platform} - {self.title}"
    


class SEOSetting(models.Model):
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)

    class Meta:
        verbose_name = "SEO Setting"
        verbose_name_plural = "SEO Settings"

    def __str__(self):
        return "SEO Settings"







