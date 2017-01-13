#coding: utf-8
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
class Place(models.Model):
    room = models.CharField(max_length=256)

    def __unicode__(self):
        return unicode("%s" % (self.room))


class TempMeasurmentsValues(models.Model):
    room_foreign_key = models.ForeignKey(Place)
    temp_value = models.DecimalField(max_digits=5, decimal_places=2,
        verbose_name="Temperatura")
    tepm_measurment_data = models.DateField(verbose_name="Data pomiaru")
    temp_measurment_time = models.TimeField(verbose_name="Czas poiaru")

    def __unicode__(self):
        return unicode("%s: %s %s" % (self.temp_value, self.tepm_measurment_data, self.temp_measurment_time))