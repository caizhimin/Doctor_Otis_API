
from django.utils import deprecation


class CheckSourceMiddleware(deprecation.MiddlewareMixin):
    def process_request(self, request):
        print(request.POST)