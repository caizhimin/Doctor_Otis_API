import pandas as pd
import json
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, JsonResponse
from utils.cosmos_db import cosmos
from TSB_elevator_management.models import TSBCity, ReportType
from django.utils.html import escape


# Create your views here.

def query_city_name(_id):
    name = TSBCity.objects.get(pk=_id).name
    return name


def query_tsb_report_name(_id):
    name = ReportType.objects.get(pk=_id).name
    return name


def tsb_report_page(request):
    tsb_cities = TSBCity.objects.all()
    return render_to_response('tsb_report.html', context={"tsb_cities": tsb_cities})


def tsb_report_json(request):
    offset = request.GET.get('offset')
    limit = request.GET.get('limit')
    city_id = (request.GET.get('city_id'))
    type_id = request.GET.get('type_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    raw_sql = """SELECT c.id, c.City, c.UnitNumber, c.Type, c.RequestData, c.RequestTime, c.ResponseData, c.ResponseTime, c.Error from c"""
    if start_date and end_date:
        raw_sql += """ WHERE c.RequestTime >= '%s' and c.RequestTime <= '%s'""" % (
            start_date + 'T00:00:00', end_date + 'T23:59:59')
        if city_id:
            raw_sql += """ c.City=%s""" % city_id
            if type_id:
                raw_sql += """ AND c.Type=%s""" % type_id
    elif city_id:
        raw_sql += """ WHERE c.City=%s""" % city_id
        if type_id:
            raw_sql += """ AND c.Type=%s""" % type_id
    count_sql = raw_sql.replace('c.id, c.City, c.UnitNumber, c.Type, c.RequestData, c.RequestTime, c.ResponseData, c.ResponseTime, c.Error',
                                             'value count(1)')
    print('count_sql', count_sql)
    total = cosmos.query_by_raw(container_id='TSB_Report', raw_sql=count_sql)[0]
    raw_sql += """ ORDER BY c._ts DESC"""
    if offset and limit:
        raw_sql += """ OFFSET %s LIMIT %s""" % (offset, limit)
    if city_id:
        res = cosmos.query_by_raw('TSB_Report', raw_sql)
    else:
        res = cosmos.query_by_raw('TSB_Report', raw_sql)[int(offset):]
    df = pd.DataFrame(res)
    df = df.reset_index()
    df['City'] = df['City'].apply(query_city_name)
    df['Type'] = df['Type'].apply(query_tsb_report_name)
    df['RequestData'] = df['RequestData'].apply(str)
    df['RequestTime'].replace('T', '<br>', inplace=True, regex=True)
    df['RequestTime'] = df['RequestTime'].str.slice(0, -7)
    df['ResponseTime'].replace('T', '<br>', inplace=True, regex=True)
    df['ResponseTime'] = df['ResponseTime'].str.slice(0, -7)
    df['Error'] = df['Error'].apply(escape)
    print(df['RequestTime'])
    print(df)
    rows = df.to_dict(orient='records')  # output just the records (no fieldnames) as a collection of tuples
    result = json.dumps({'total': total, "totalNotFiltered": total, 'rows': rows})
    return HttpResponse(result)


def get_tsb_report_types(request):
    if request.method == 'GET':
        city_id = request.GET.get('city_id')
        if city_id:
            data = json.dumps(list(ReportType.objects.filter(city_id=city_id).values('id', 'name')))
            return JsonResponse(data, safe=False)
