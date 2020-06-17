from django.db import models
from django.utils import timezone
# Create your models here.

class Stu_Info(models.Model):
    id = models.CharField(primary_key=True,max_length=12)
    name = models.CharField(max_length=20)
    # 防止冲突，字符串类型
    classes = models.CharField(max_length=20)
    # 专业 
    major = models.CharField(max_length=25)
    # 个人信息
    information = models.TextField()
    # deeds 突出事迹
    deeds = models.TextField()
    
    # is_nominated
    is_nominated = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    submit_time = models.DateTimeField(default=timezone.now)
    last_update_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=16, default='127.0.0.1')

    object = models.Manager()
    def __str__(self):
        return "<%s>" % self.id