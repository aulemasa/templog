from django.conf.urls import include, url
from django.contrib import admin
import show_temp.views


urlpatterns = [
    # Examples:
    # url(r'^$', 'home_temp_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', show_temp.views.showActualTemp, name='main'),
    url(r'^today.temp/', show_temp.views.showTodayTemp, name='today'),
    url(r'^history.temp/', show_temp.views.showMeasurmentsHistory, name='history'),

]
