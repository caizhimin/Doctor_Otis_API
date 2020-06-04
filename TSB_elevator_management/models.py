from django.db import models

# Create your models here.

branch = ((1, 'oe'), (2, 'ocl'))


class TSBCity(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class Elevator(models.Model):
    unit_number = models.CharField(max_length=10, blank=True, verbose_name='梯号')
    tsb_regcode = models.CharField(max_length=20, blank=True, verbose_name='TSB电梯识别码')
    unit_regcode = models.CharField(max_length=50, blank=True, verbose_name='设备注册代码')
    branch = models.IntegerField(choices=branch, blank=True, null=True, verbose_name='分公司')
    city = models.ForeignKey(TSBCity, null=True, on_delete=models.CASCADE, verbose_name='城市')

    def __str__(self):
        return self.unit_number

    class Meta:
        verbose_name = '电梯'
        verbose_name_plural = verbose_name


class ReportType(models.Model):
    name = models.CharField(max_length=30, verbose_name='上报类型')
    city = models.ForeignKey(TSBCity, null=True, on_delete=models.CASCADE, verbose_name='城市')


