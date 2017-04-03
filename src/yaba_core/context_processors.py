from django.conf import settings


def global_settings(request):
    return {
        'LAST_FM_API_KEY': settings.LAST_FM_API_KEY,
        'LAST_FM_USERNAME': settings.LAST_FM_USERNAME,
        'LAST_FM_SCROBBLES_LIMIT': settings.LAST_FM_SCROBBLES_LIMIT
    }
