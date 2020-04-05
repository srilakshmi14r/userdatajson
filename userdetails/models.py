from django.db import models
from datetime import datetime,date
import pytz
#from timezone_utils.fields import TimeZoneField
#from timezone_utils.choices import PRETTY_ALL_TIMEZONES_CHOICES

# Create your models here.
class users(models.Model):

    TIMEZONES=tuple(zip(pytz.all_timezones,pytz.all_timezones))
    userid = models.CharField(max_length = 100, primary_key=True)
    name=models.CharField(max_length=200)
    #timezone = models.TimeZoneField(choices=PRETTY_ALL_TIMEZONES_CHOICES)
    timezone=models.CharField(max_length=100,choices=TIMEZONES,default='UTC')

    def __str__(self):
        return self.name

class ActivePeriod(models.Model):
    start_time=models.DateField(auto_now=False,auto_now_add=False)
    end_time=models.DateField(auto_now=False,auto_now_add=False)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
