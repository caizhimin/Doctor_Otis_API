from django.db import models
from datetime import datetime


# Create your models here.

class ApiRecord(models.Model):
    client_ip = models.CharField(max_length=30, null=True, blank=True, verbose_name='客户端IP')
    user_agent = models.CharField(max_length=200, null=True, blank=True, verbose_name='User-Agent')
    authorization = models.CharField(max_length=100, null=True, blank=True, verbose_name='Authorization')
    unit_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='梯号')
    datetime = models.DateTimeField(null=True, blank=True, verbose_name='时间')
    status = models.IntegerField(null=True, blank=True, verbose_name='请求状态')
    A_1_1 = models.IntegerField(null=True, blank=True, verbose_name='A-1_1')
    A_1_4 = models.IntegerField(null=True, blank=True, verbose_name='A-1_4')
    A_1_4_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_4额外检查楼层')
    A_1_5 = models.IntegerField(null=True, blank=True, verbose_name='A-1_5')
    A_1_5_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_5额外检查楼层')
    A_1_6 = models.IntegerField(null=True, blank=True, verbose_name='A-1_6')
    A_1_7 = models.IntegerField(null=True, blank=True, verbose_name='A-1_7')
    A_1_7_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_7额外检查楼层')
    A_1_13 = models.IntegerField(null=True, blank=True, verbose_name='A-1_13')
    A_1_19 = models.IntegerField(null=True, blank=True, verbose_name='A-1_19')
    A_1_19_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_19额外检查楼层')
    A_1_20 = models.IntegerField(null=True, blank=True, verbose_name='A-1_20')
    A_1_20_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_20额外检查楼层')
    A_1_21 = models.IntegerField(null=True, blank=True, verbose_name='A-1_21')
    A_1_21_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_21额外检查楼层')
    A_1_22 = models.IntegerField(null=True, blank=True, verbose_name='A-1_22')
    A_1_22_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_22额外检查楼层')
    A_1_23 = models.IntegerField(null=True, blank=True, verbose_name='A-1_23')
    A_1_23_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_23额外检查楼层')
    A_1_24 = models.IntegerField(null=True, blank=True, verbose_name='A-1_24')
    A_1_24_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_24额外检查楼层')
    A_1_25 = models.IntegerField(null=True, blank=True, verbose_name='A-1_25')
    A_1_25_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_25额外检查楼层')
    A_1_28 = models.IntegerField(null=True, blank=True, verbose_name='A-1_28')
    A_1_28_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-1_28额外检查楼层')
    A_2_2 = models.IntegerField(null=True, blank=True, verbose_name='A-2_2')
    A_2_3 = models.IntegerField(null=True, blank=True, verbose_name='A-2_3')
    A_2_3_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-2_3额外检查楼层')
    A_2_5 = models.IntegerField(null=True, blank=True, verbose_name='A-2_5')
    A_2_5_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-2_5额外检查楼层')
    A_2_8 = models.IntegerField(null=True, blank=True, verbose_name='A-2_8')
    A_2_8_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-2_8额外检查楼层')
    A_3_4 = models.IntegerField(null=True, blank=True, verbose_name='A-3_4')
    A_3_4_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-3_4额外检查楼层')
    A_3_5 = models.IntegerField(null=True, blank=True, verbose_name='A-3_5')
    A_4_2 = models.IntegerField(null=True, blank=True, verbose_name='A-4_2')
    A_4_2_extra_floor = models.CharField(max_length=200, null=True, blank=True, verbose_name='A-4_2额外检查楼层')
    A_4_4 = models.IntegerField(null=True, blank=True, verbose_name='A-4_4')

    @staticmethod
    def create(client_ip, user_agent, authorization, unit_number, status, data=None):
        record = ApiRecord()
        record.client_ip = client_ip
        record.user_agent = user_agent
        record.authorization = authorization
        record.unit_number = unit_number
        record.datetime = datetime.now()
        record.status = status
        if data.get('autoItems') and isinstance(data.get('autoItems'), list):
            for i in data.get('autoItems'):
                item = i['item'].replace('-', '_', 1)
                tsbStatus = i['tsbStatus']
                floorInfo = i['floorInfo']
                exec('record.' + item + '=' + str(tsbStatus))
                if item in ['A_1_4', 'A_1_5', 'A_1_7', 'A_1_19', 'A_1_20', 'A_1_21', 'A_1_22', 'A_1_23',
                            'A_1_24', 'A_1_25', 'A_1_28', 'A_2_3', 'A_2_5', 'A_2_8', 'A_3_4', 'A_4_2']:
                    exec('record.' + item + '_extra_floor' + '=' + (str(floorInfo) if floorInfo else 'None'))
        record.save()
