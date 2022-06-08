import requests
from datetime import datetime
from utils.cosmos_db import cosmos
from utils.DO_mysql import get_unit_oil, reset_unit_oil
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from oauth2_provider.oauth2_validators import AccessToken
from API.models import ApiRecord


# Create your views here.

@api_view(['POST', 'GET'])
def DO_data(request, unit_number):
    # print(1111)
    # meta = request.META
    # HTTP_X_FORWARDED_FOR = meta.get('HTTP_X_FORWARDED_FOR')
    # try:
    #     HTTP_USER_AGENT = request.headers.get('User-Agent')
    # except:
    #     HTTP_USER_AGENT = ''
    # try:
    #     Authorization = request.headers.get('Authorization')
    # except:
    #     Authorization = ''
    if request.method in ('GET', 'POST'):
        # try:
        data = cosmos.query('DO_Auto_Maintenance_Result',
                                fields=('DO_value',), query_params={'UnitNumber': unit_number})
        print(2222)
        # except:
        #     ApiRecord.create(client_ip=HTTP_X_FORWARDED_FOR, user_agent=HTTP_USER_AGENT, authorization=Authorization,
        #                      unit_number=unit_number, status=-1)
        #     return Response({'Result': -1, 'Message': '服务器错误，请求失败', 'Data': {}})
        if data:
            # oil = get_unit_oil(unit_number)
            if data[0].get('DO_value'):
                # for i in data[0]['DO_value']['autoItems']:
                #     if i['item'] == 'A-1_13':
                #         if oil < 71:
                #             i['tsbStatus'] = 1
                #             reset_unit_oil(unit_number)
                #         else:
                #             i['tsbStatus'] = 0
                # ApiRecord.create(client_ip=HTTP_X_FORWARDED_FOR, user_agent=HTTP_USER_AGENT,
                #                  authorization=Authorization,
                #                  unit_number=unit_number, status=1, data=data[0]['DO_value'])
                return Response({'Result': 0, 'Message': '请求成功', 'Data': data[0]['DO_value']})
            else:
                url = 'https://developerstudio-china.otiselevator.com/iot-core/v2/api/CHN/v2/unitlist'
                Ocp_Apim_Subscription_Key = 'd7299181f9b94dfb8cfcefbb676a4c1d'
                headers = {'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key}
                req_text = {
                    "CountryCode": "CHN",
                    "PlatformType": "robustel",
                    "PageSize": 20,
                    "FreeTextSearch": unit_number,
                    "FetchCount": False,
                    "commissioningState": "commissioned,fullycommissioned,partiallycommissioned"
                }
                res = requests.post(headers=headers, url=url, json=req_text).json()
                if res.get('units'):
                    new_data = {
                        "autoItems": [
                            {
                                "item": "A-1_7",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-2_3",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_21",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-2_8",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_22",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_28",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-2_5",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-3_4",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_24",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_23",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_20",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_19",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_5",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-4_2",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_4",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_6",
                                "tsbStatus": 1,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_13",
                                "tsbStatus": 80,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_1",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-1_25",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-2_2",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-3_5",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            },
                            {
                                "item": "A-4_4",
                                "tsbStatus": 0,
                                "tsbString": "",
                                "floorInfo": None
                            }]}
                    # ApiRecord.create(client_ip=HTTP_X_FORWARDED_FOR, user_agent=HTTP_USER_AGENT,
                    #                  authorization=Authorization,
                    #                  unit_number=unit_number, status=1, data=new_data)
                    data[0]['DO_value'] = new_data
                    return Response({'Result': 0, 'Message': '请求成功', 'Data': new_data})
                else:
                    return Response({'Result': 0, 'Message': 'eventlog不存在', 'Data': {}})
        else:
            url = 'https://developerstudio-china.otiselevator.com/iot-core/v2/api/CHN/v2/unitlist'
            Ocp_Apim_Subscription_Key = 'd7299181f9b94dfb8cfcefbb676a4c1d'
            headers = {'Ocp-Apim-Subscription-Key': Ocp_Apim_Subscription_Key}
            req_text = {
                "CountryCode": "CHN",
                "PlatformType": "robustel",
                "PageSize": 20,
                "FreeTextSearch": unit_number,
                "FetchCount": False,
                "commissioningState": "commissioned,fullycommissioned,partiallycommissioned"
            }
            res = requests.post(headers=headers, url=url, json=req_text).json()
            if res.get('units'):
                new_data = {
                    "autoItems": [
                        {
                            "item": "A-1_7",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-2_3",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_21",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-2_8",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_22",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_28",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-2_5",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-3_4",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_24",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_23",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_20",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_19",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_5",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-4_2",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_4",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_6",
                            "tsbStatus": 1,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_13",
                            "tsbStatus": 80,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_1",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-1_25",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-2_2",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-3_5",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        },
                        {
                            "item": "A-4_4",
                            "tsbStatus": 0,
                            "tsbString": "",
                            "floorInfo": None
                        }]}

                # ApiRecord.create(client_ip=HTTP_X_FORWARDED_FOR, user_agent=HTTP_USER_AGENT,
                #                  authorization=Authorization,
                #                  unit_number=unit_number, status=1, data=new_data)
                if unit_number:
                    cosmos.insert('DO_Auto_Maintenance_Result',
                                  data={'UnitNumber': unit_number, 'DO_value': new_data})
                return Response({'Result': 0, 'Message': '请求成功', 'Data': new_data})
            else:
                # ApiRecord.create(client_ip=HTTP_X_FORWARDED_FOR, user_agent=HTTP_USER_AGENT,
                #                  authorization=Authorization,
                #                  unit_number=unit_number, status=0)
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
