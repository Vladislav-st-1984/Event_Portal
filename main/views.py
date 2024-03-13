from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect




## регистрация пользователя
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from main.forms import CreateUserForm, LoginUserForm
from main.models import Users
from main.utils import DataMixin


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
        # if not self.request.is_ajax():
        user = form.save()  ## сохранение формы
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


def profilefunc(request):
    return render(request, 'main/profile.html')
