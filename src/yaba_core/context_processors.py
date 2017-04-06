from django.conf import settings


def global_settings(request):
    return {
        'LAST_FM_API_KEY': getattr(settings, 'LAST_FM_API_KEY', None),
        'LAST_FM_USERNAME': getattr(settings, 'LAST_FM_USERNAME', None),
        'LAST_FM_SCROBBLES_LIMIT': getattr(settings, 'LAST_FM_SCROBBLES_LIMIT', 10),
        'TWITTER_USERNAME': getattr(settings, 'TWITTER_USERNAME', None),
        'GITHUB_USERNAME': getattr(settings, 'GITHUB_USERNAME', None),
        'DISQUS_WEBSITE_SHORTNAME': getattr(settings, 'DISQUS_WEBSITE_SHORTNAME', None),
    }
