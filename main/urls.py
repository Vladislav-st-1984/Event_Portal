from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home'),

    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('reg', RegisterUser.as_view(), name='register'),


    path('events', eventfunc, name='events' ),
    path('Eventsinfo', enentinfofunc, name='eventsinfo' ),
    path('profile', profilefunc, name='profile' ),


]