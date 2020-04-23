from django.db import models


# Create your models here.

class ApiRecord(models.Model):
    client_ip = models.CharField(max_length=30, verbose_name='客户端IP')
    user_agent = models.CharField(max_length=200, verbose_name='User-Agent')
    authorization = models.CharField(max_length=100, verbose_name='Authorization')
    unit_number = models.CharField(max_length=20, verbose_name='梯号')

    @staticmethod
    def create(client_ip, user_agent, authorization, unit_number):
        record = ApiRecord()
        record.client_ip = client_ip
        record.user_agent = user_agent
        record.authorization = authorization
        record.unit_number = record.unit_number
        record.save()
