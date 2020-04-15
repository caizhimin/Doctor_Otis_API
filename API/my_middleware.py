from django.utils import deprecation


class CheckSourceMiddleware(deprecation.MiddlewareMixin):
    def process_request(self, request):
        meta = request.META
        HTTP_USER_AGENT = meta.get('HTTP_USER_AGENT')
        REMOTE_ADDR = meta.get('REMOTE_ADDR')
        print('REMOTE_ADDR %s' % REMOTE_ADDR, 'HTTP_USER_AGENT: %s' % HTTP_USER_AGENT,  'POST-data: %s'% request.POST)



