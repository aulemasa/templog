from django.shortcuts import render

# Create your views here.
import os
import datetime
from .models import TempMeasurmentsValues
from django.db.models import Avg, Max, Min


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
sensor_temp = '/sys/bus/w1/devices/28-0000084be100//w1_slave'


def showActualTemp(request):
    temp_read = open(sensor_temp, 'r')
    lines = temp_read.readlines()
    temp_read.close()

    temp_find = lines[1].find('t=')
    if temp_find != -1:
        temp_strip = lines[1].strip()[temp_find + 2:]
        temp_result_cel = round(float(temp_strip) / 1000, 2)

    return render(request, 'show_temp/showing_temp.html',
    {'temp_result_cel': temp_result_cel})


class Round():#add Func
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 0)'


def showTodayTemp(request):
    today_temp_measur = TempMeasurmentsValues.objects.filter(
        tepm_measurment_data=datetime.date.today()).order_by(
            'temp_measurment_time')
    today_aggregation_values = today_temp_measur.aggregate(
        Avg('temp_value'), Max('temp_value'),
        Min('temp_value'))

    return render(request, 'show_temp/today_temp.html',
    {'today_temp_measur': today_temp_measur,
    'today_aggregation_values': today_aggregation_values})


def showMeasurmentsHistory(request):
    all_temp_measur = TempMeasurmentsValues.objects.all().exclude(
        tepm_measurment_data__gte=datetime.date.today() - datetime.timedelta()).order_by(
            'tepm_measurment_data','temp_measurment_time')

    return render(request, 'show_temp/history_temp.html',
    {'all_temp_measur': all_temp_measur})