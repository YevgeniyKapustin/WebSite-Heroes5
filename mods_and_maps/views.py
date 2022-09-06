from django.views.generic import ListView
from mods_and_maps.models import Mods, Maps


class ModsList(ListView):
    model = Mods
    template_name = 'mods_and_maps/mods_and_maps.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Моды'
        context['Button'] = 'Скачать'
        context['Prefix'] = 'Авторство: '
        return context


class MapsList(ListView):
    model = Maps
    template_name = 'mods_and_maps/mods_and_maps.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Карты'
        context['Button'] = 'Скачать'
        context['Prefix'] = 'Авторство: '
        return context
