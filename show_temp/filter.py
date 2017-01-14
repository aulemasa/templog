# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
from django.utils.encoding import python_2_unicode_compatible

import django_filters
from .models import TempMeasurmentsValues


class DataFilter(django_filters.FilterSet):
    class Meta:
        model = TempMeasurmentsValues
        fields = ['tepm_measurment_data', ]
