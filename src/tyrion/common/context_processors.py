from django.contrib.sites.models import get_current_site

def site(request):
    current_site = get_current_site(request)
    
    return {
        'CURRENT_SITE_DOMAIN': current_site.domain,
        'CURRENT_SITE_NAME': current_site.name,
    }