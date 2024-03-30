
## Контекстное меню (которое сверху). title - заголовок. url_name - ссылка странички. path - та же url_name,
# только с '/' для проверки, на той ли мы страничке находимся
menu = [{'title': 'Главная', 'url_name': 'home', 'path': '/'},
        {'title': 'Список мероприятий', 'url_name': 'Events', 'path': '/Events'},
        {'title': 'Добавить мероприятие', 'url_name': 'list_event', 'path': '/list_event'}
        ]

class DataMixin:
    def get_user_content(self, **kwargs):
        context = kwargs
        context['error'] = ''
        context['menu'] = menu
        return context