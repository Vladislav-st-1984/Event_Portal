
## Контекстное меню (которое сверху). title - заголовок. url_name - ссылка странички. path - та же url_name,
# только с '/' для проверки, на той ли мы страничке находимся
menu = [{'title': 'Главная', 'url_name': 'home', 'path': '/'},
        {'title': 'Список мероприятий', 'url_name': 'Events', 'path': '/Events'},
        {'title': 'Добавить мероприятие', 'url_name': 'list_event', 'path': '/list_event'},
        {'title': 'Добавить этап', 'url_name': 'list_stage', 'path': '/list_stage'},
        {'title': 'Список зарегестрированных пользователей', 'url_name': 'show_list_users_events', 'path': '/show_list_users_events'},
        {'title': 'Список твоих мероприятий', 'url_name': 'show_list_events_for_user', 'path': '/show_list_events_for_user'}
        ]

class DataMixin:
    def get_user_content(self, **kwargs):
        context = kwargs
        context['error'] = ''
        context['menu'] = menu
        return context