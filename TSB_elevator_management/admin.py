from django.contrib import admin
from TSB_elevator_management.models import TSBCity, Elevator


# Register your models here.

@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_number', 'tsb_regcode', 'unit_regcode', 'branch', 'city_name')

    search_fields = ('unit_number', 'tsb_regcode', 'unit_regcode',)

    list_filter = ('city',)

    def city_name(self, obj):
        return obj.city.name

    city_name.short_description = '城市'


@admin.register(TSBCity)
class TSBCityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # readonly_fields = ('name',)
