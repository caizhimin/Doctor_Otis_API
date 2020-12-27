from django.contrib import admin
from API.models import ApiRecord


# Register your models here.

@admin.register(ApiRecord)
class ApiRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_ip', 'user_agent', 'unit_number', 'datetime', 'status', 'A_1_1', 'A_1_4', 'A_1_5',
                    'A_1_6', 'A_1_7', 'A_1_13', 'A_1_19', 'A_1_19_extra_floor', 'A_1_20', 'A_1_21',
                    'A_1_21_extra_floor', 'A_1_22', 'A_1_22_extra_floor', 'A_1_23', 'A_1_23_extra_floor',
                    'A_1_24', 'A_1_24_extra_floor', 'A_1_25', 'A_1_28', 'A_1_28_extra_floor', 'A_2_2',
                    'A_2_3', 'A_2_5', 'A_2_8', 'A_2_8_extra_floor', 'A_3_4', 'A_3_5', 'A_4_2', 'A_4_4')

    search_fields = ('unit_number',)

    def get_description(self, obj):
        return obj.user_agent[:10]

    class Media:
        css = {
            'all': ('/static/admin/css/my_own_admin.css',)
        }

    # list_filter = ('city',)

    # def city_name(self, obj):
    #     return obj.city.name

    # city_name.short_description = '城市'
