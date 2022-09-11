from django.views.generic import ListView
from maps.models import Maps


class MapsList(ListView):
    model = Maps

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Карты'
        context['Button'] = 'Скачать'
        context['Prefix'] = 'Авторство: '
        return context
