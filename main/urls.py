from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home' ),
    path('Events', eventfunc, name='events' ),
    path('Eventsinfo', enentinfofunc, name='eventsinfo' ),
    path('profile', profilefunc, name='profile' ),


]