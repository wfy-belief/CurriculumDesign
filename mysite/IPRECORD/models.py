from django.db import models

# Create your models here.
class IPRECORD(models.Model):
    id = models.CharField(primary_key=True,max_length=16)
    max_count = models.IntegerField(default=3)
    is_same = models.BooleanField(default=False)
    object = models.Manager()
    def __str__(self):
        return "<%s>" % self.id