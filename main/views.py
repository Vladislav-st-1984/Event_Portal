import random

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView, BSModalUpdateView
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

## регистрация пользователя
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, ListView, DetailView

from main.forms import CreateUserForm, LoginUserForm, UpdateProfile, UpdateEventsForm
from main.models import Users, Event
from main.utils import DataMixin

## Импорт Логгера
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class RegisterUser(DataMixin, BSModalCreateView):
    form_class = CreateUserForm
    template_name = 'main/create_user.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Регистрация!")
        return dict(list(context.items()) + list(c_def.items()))

    ## функция, вызывающаяся при валидности формы
    def form_valid(self, form):
        if not is_ajax(self.request):
            form.save()
            stud_email = form.cleaned_data.get('stud_email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=stud_email, password=raw_password)

            print(f'stud_email - {stud_email}')
            print(f'raw_password - {raw_password}')
            print(f'user - {user}')

            logger.debug(f"Юзер {stud_email} зарегестрировался")

            login(self.request, user)  ## авто-логин пользователя при регистрации
        return redirect('home')

    # def form_invalid(self, form):
    #     print("fsfdsfsdfsdf")
    #     logger.error(f"Юзер {form.cleaned_data.get('stud_email')} не смог зарегестрироваться")
    #     return redirect('home')

## логин пользователя
class LoginUser(DataMixin, BSModalLoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    success_message = 'Найс, ты залогинился'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Авторизируйся!")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        logger.info(f"Юзер {self.request.user.username} залогинился")
        return reverse_lazy('home')


## функция выхода пользователя
def logout_user(request):
    logger.info(f"info")
    logger.debug(f"debig")

    db_logger = logging.getLogger('db')
    db_logger.error(f"Error")

    logout(request)
    return redirect('home')


import datetime
class Index(DataMixin, TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info("")
        event_list = Event.objects.all()
        date_list = [event.date for event in event_list]

        now = datetime.date.today()
        date_format = "%Y-%B-%d %H:%M:%S"
        past_dates, future_dates = [], []

        for date in event_list:
            # date_obj = datetime.datetime.strptime(date.date, date_format)
            date_obj = date.date
            if now > date_obj:
                past_dates.append(date_obj)
            else:
                future_dates.append(date_obj)

        # past_date = max(past_dates)
        future_date_arr = []
        # print(f"future_dates - {future_dates}")
        if future_dates != []:
            future_date_arr = min(future_dates)

        # if len(future_date_arr) > 1:
        #     future_date_arr = random.choice(future_date_arr)

        print(f'future_date_arr - {future_date_arr}')
        # nearly_event = Event.objects.filter(Q(date=future_date_arr))
        nearly_event = Event.objects.filter(Q(date=future_date_arr)).first()

        # print(f'before if - {nearly_event}')
        #
        # if len(nearly_event) > 1:
        #     nearly_event = random.choice(nearly_event)
        #     print(f'after if - {nearly_event}')

        c_def = self.get_user_content(title="Главная!", Nearly_event=nearly_event)
        return dict(list(context.items()) + list(c_def.items()))


class EventList(DataMixin, TemplateView):
    template_name = "main/Events.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            event_list = Event.objects.all()
            date_list = [event.date for event in event_list]

            now = datetime.date.today()
            date_format = "%Y-%B-%d %H:%M:%S"
            past_dates, future_dates, nearly_dates = [], [], []

            for date in event_list:
                # date_obj = datetime.datetime.strptime(date.date, date_format)
                date_obj = date.date
                if now <= date_obj <= (now + datetime.timedelta(days=3)):
                    nearly_dates.append(date_obj)
                elif now >= date_obj:
                    past_dates.append(date_obj)
                else:
                    future_dates.append(date_obj)

            nearly_event = Event.objects.filter(Q(date__in=nearly_dates))
            past_event = Event.objects.filter(Q(date__in=past_dates))
            future_event = Event.objects.filter(Q(date__in=future_dates))

            print(f"nearly_event = {nearly_event}")
            print(f"past_event - {past_event}")
            print(f"future_event - {future_event}")

            c_def = self.get_user_content(title="Список мероприятий", Nearly_event=nearly_event, Past_event=past_event, Future_event=future_event)
            return dict(list(context.items()) + list(c_def.items()))
        except ():
            logger.error("Произошла ошибка")
            c_def = self.get_user_content(title="Список мероприятий")
            return dict(list(context.items()) + list(c_def.items()))


class EventDetail(DataMixin, DetailView):
    template_name = "main/Eventsinfo.html"
    context_object_name = "event"
    model = Event

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Подробная инфа!")
        return dict(list(context.items()) + list(c_def.items()))

    # def get_queryset(self):
    #     # event = get_object_or_404(Event, pk=self.kwargs["pk"])
    #     return Event.objects.filter(pk=self.kwargs["pk"])



class Profile(DataMixin, UpdateView):
    model = Users
    template_name = 'main/profile.html'
    form_class = UpdateProfile
    # fields = ['first_name', 'last_name', 'middle_name', "email", "stud_email", "phone"]
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        c_def = self.get_user_content(title="Твой профиль", user=self.request.user)
        # print(f"user - {self.request.user}")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('profile', args=[self.kwargs['pk']])  ## передаем "слагом" пк юзера

    def form_valid(self, form):
        print("form_valid")
        # form.instance.user = self.user_id
        form.save()
        # return super(Profile, self).form_valid(form)
        return super().form_valid(form)


## Создание мероприятия
class CreateEvent(BSModalCreateView):
    form_class = UpdateEventsForm
    template_name = 'main/admin/create_events.html'
    success_url = reverse_lazy('list_event')


def event(request):
    data = dict()
    if request.method == 'GET':
        events = Event.objects.all()
        # asyncSettings.dataKey = 'table'
        data['tables'] = render_to_string(
            'main/admin/_event_table.html',
            {'Event': events},
            request=request
        )
        return JsonResponse(data)


## Список мероприятия
class ListEvent(DataMixin, ListView):
    model = Event
    template_name = "main/admin/list_events.html"
    context_object_name = "Event"
    queryset = Event.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Список мероприятий")
        return dict(list(context.items()) + list(c_def.items()))

    def get(self, request, *args, **kwargs):
        for key in request.GET.keys():
            if key.startswith('btn_'):
                btn_pk = key[4:]
                record = Event.objects.get(id=btn_pk)
                record.delete()
        return super(ListEvent, self).get(request, *args, **kwargs)


## Обновление мероприятия
class UpdateEvent(DataMixin, BSModalUpdateView):
    model = Event
    form_class = UpdateEventsForm
    template_name = 'main/admin/update_events.html'
    success_url = reverse_lazy('list_event')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Обновление данных мероприятия")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        if self.request.POST.get('asyncUpdate') == 'True':
            form.save()
        return super().form_valid(form)

