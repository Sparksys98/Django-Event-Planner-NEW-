from django.db import models
from django.contrib.auth.models import User
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
# from location_field.models.spatial import LocationField
# from location_field.models.plain import PlainLocationField
class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    #city = models.CharField(max_length=255)
    # location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    #location = PlainLocationField(based_fields=['city'], zoom=7,)
    location = models.TextField()
    datetime = models.DateTimeField()
    seats= models.PositiveIntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Booking(models.Model):
    event=models.ForeignKey(Event, on_delete=models.CASCADE,blank=True,null=True)
    tickets=models.PositiveIntegerField()
    booker = models.ForeignKey(User, on_delete = models.CASCADE,related_name='booker',blank=True,null=True)
