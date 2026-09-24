from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class AdminLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path.startswith('/spasb_admin/') and not request.path.startswith('/spasb_admin/login'):
            if not request.user.is_authenticated:
                return HttpResponseRedirect('/accounts/login/?next=' + request.path)
        return self.get_response(request)