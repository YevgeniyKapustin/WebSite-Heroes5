from django.views.generic import ListView
from mods.models import Mods


class ModsList(ListView):
    model = Mods

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Моды'
        context['Button'] = 'Скачать'
        context['Prefix'] = 'Авторство: '
        return context
