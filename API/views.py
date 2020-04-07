from django.shortcuts import render
from utils.cosmos_db import cosmos
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
            return Response({'Result': 0, 'Message': '请求成功', 'Data': data[0]['DO_value']})
        else:
            return Response({'Result': 0, 'Message': 'eventlog不存在', 'Data': {}})


@api_view(['GET'])
def test(request):
    return Response(111)
