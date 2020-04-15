from django.utils import deprecation


class CheckSourceMiddleware(deprecation.MiddlewareMixin):
    def process_request(self, request):
        meta = request.META
        HTTP_USER_AGENT = meta.get('HTTP_USER_AGENT')
        HTTP_X_FORWARDED_FOR = meta.get('HTTP_X_FORWARDED_FOR')
        print('HTTP_X_FORWARDED_FOR %s' % HTTP_X_FORWARDED_FOR, 'HTTP_USER_AGENT: %s' % HTTP_USER_AGENT,  'POST-data: %s'% request.POST)



