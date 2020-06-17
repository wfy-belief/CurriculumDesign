from django.contrib import admin

# Register your models here.
from .models import Stu_Info

@admin.register(Stu_Info)
class Stu_InfoAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'classes',
        'major',
        'information',
        'deeds',
        'is_nominated',
        'is_deleted',
        'votes',
        'submit_time',
        'last_update_time',
        'ip'
    )

    
# Register your models here.,
