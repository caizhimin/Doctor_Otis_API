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

    @staticmethod
    def create(client_ip, user_agent, authorization, unit_number, status):
        record = ApiRecord()
        record.client_ip = client_ip
        record.user_agent = user_agent
        record.authorization = authorization
        record.unit_number = unit_number
        record.datetime = datetime.now()
        record.status = status
        record.save()
