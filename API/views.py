from django.shortcuts import render
from utils.cosmos_db import cosmos
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET', 'POST'])
def DO_data(request, unit_number):
    if request.method in ('GET', 'POST'):
        data = cosmos.query('DO_auto_maintenance_result',
                            fields=('DO_value',), query_params={'UnitNumber': unit_number})
        if data:
            return Response(data[0])
        else:
            content = {'error': 'unit number not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def test(request):
    return Response(111)
