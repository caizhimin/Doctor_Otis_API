from django.utils import deprecation


class CheckSourceMiddleware(deprecation.MiddlewareMixin):
    def process_request(self, request):
        meta = request.META
        try:
            HTTP_USER_AGENT = request.headers.get('User-Agent')
        except:
            HTTP_USER_AGENT = ''
        HTTP_X_FORWARDED_FOR = meta.get('HTTP_X_FORWARDED_FOR')
        try:
            Authorization = request.headers.get('Authorization')
        except:
            Authorization = ''
        print('HTTP_X_FORWARDED_FOR %s' % HTTP_X_FORWARDED_FOR, 'HTTP_USER_AGENT: %s' % HTTP_USER_AGENT,
              'Authorization %s' % Authorization, 'POST-data: %s' % request.POST)



