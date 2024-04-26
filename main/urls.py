from django.urls import path

from main.views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),

    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('reg', RegisterUser.as_view(), name='register'),


    path('Events', EventList.as_view(), name='Events'),
    path('Eventsinfo/<pk>', EventDetail.as_view(), name='Eventsinfo'),
    path('profile/<pk>', Profile.as_view(), name='profile'),


    path('update_event/<pk>', UpdateEvent.as_view(), name='update_event'),
    path('list_event', ListEvent.as_view(), name='list_event'),
    path('event', event, name='event'),
    path('create_event', CreateEvent.as_view(), name='create_event'),


    path('update_stage/<pk>', UpdateStage.as_view(), name='update_stage'),
    path('list_stage', ListStage.as_view(), name='list_stage'),
    path('stage', stage, name='stage'),
    path('create_stage', CreateStage.as_view(), name='create_stage'),


]