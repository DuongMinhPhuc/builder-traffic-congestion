import datetime as datetime
from django.db import models


class Information(models.Model):
    camera_id = models.CharField(max_length=50, blank=False)
    count_N = models.IntegerField(default=0)
    persons_count = models.IntegerField(default=0)
    motorcycle_count = models.IntegerField(default=0)
    bicycle_count = models.IntegerField(default=0)
    car_count = models.IntegerField(default=0)
    bus_count = models.IntegerField(default=0)
    truct_count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True,blank=True)

    class Meta:
        db_table = 'information'
