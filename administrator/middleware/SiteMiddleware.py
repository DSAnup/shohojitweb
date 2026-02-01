# administrator/middleware/SiteMiddleware.py
from administrator.models import SiteUser

class SiteMiddleware:
    def __init__(self, get_response):
        # print("🧠 SiteMiddleware INIT")
        self.get_response = get_response

    def __call__(self, request):
        # print("🚀 SiteMiddleware CALL")

        request.site = None
        if request.user.is_authenticated:
            site_link = SiteUser.objects.filter(
                user=request.user,
                is_active=True
            ).first()
            if site_link:
                request.site = site_link.site

        return self.get_response(request)
