from .models import SocialLink


def social_links(request):
    links = SocialLink.objects.filter(is_active=True)
    return {
        "social_links": links
    }