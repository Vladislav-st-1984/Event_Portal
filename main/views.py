from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView, BSModalUpdateView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect




## регистрация пользователя
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, ListView

from main.forms import CreateUserForm, LoginUserForm, UpdateProfile, UpdateEventsForm
from main.models import Users, Event
from main.utils import DataMixin


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
            login(self.request, user)  ## авто-логин пользователя при регистрации
        return redirect('home')


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
        return reverse_lazy('home')


## функция выхода пользователя
def logout_user(request):
    logout(request)
    return redirect('home')



def index(request):
    return render(request, 'main/index.html')


def eventfunc(request):
    return render(request, 'main/Events.html')


def enentinfofunc(request):
    return render(request, 'main/Eventsinfo.html')


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




## Создание оборудования
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


## Список оборудования
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


## Обновление оборудования
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
