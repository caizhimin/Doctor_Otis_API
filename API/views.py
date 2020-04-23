from datetime import datetime
from django.shortcuts import render
from utils.cosmos_db import cosmos
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from oauth2_provider.oauth2_validators import AccessToken
from API.models import ApiRecord



# Create your views here.

@api_view(['POST'])
def DO_data(request, unit_number):
    if request.method in ('GET', 'POST'):
        try:
            data = cosmos.query('DO_auto_maintenance_result',
                                fields=('DO_value',), query_params={'UnitNumber': unit_number})
        except:
            return Response({'Result': -1, 'Message': '服务器错误，请求失败', 'Data': {}})
        if data:
            meta = request.META
            HTTP_X_FORWARDED_FOR = meta.get('HTTP_X_FORWARDED_FOR')
            HTTP_USER_AGENT = request.headers.get('User-Agent')
            Authorization = request.headers.get('Authorization')
            ApiRecord.create(client_ip=HTTP_X_FORWARDED_FOR, user_agent=HTTP_USER_AGENT, authorization=Authorization,
                             unit_number=unit_number)
            return Response({'Result': 0, 'Message': '请求成功', 'Data': data[0]['DO_value']})
        else:
            return Response({'Result': 0, 'Message': 'eventlog不存在', 'Data': {}})


@api_view(['GET'])
def test(request):
    return Response(111)


def delete_expires_token(request):
    """
    删除过期token
    :param request:
    :return:
    """
    if request.META['REMOTE_ADDR'] == '127.0.0.1':
        AccessToken.objects.filter(expires__lt=datetime.now()).delete()
        return HttpResponse('delete expires token success')
    else:
        raise Http404
