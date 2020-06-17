from django.contrib import admin
from .models import IPRECORD
# Register your models here.
@admin.register(IPRECORD)
class IPRECORDAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'max_count',
        'is_same'
    )