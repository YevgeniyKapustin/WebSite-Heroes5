from django.views.generic import ListView, DetailView
from guides.models import Guides


class GuidesMain(ListView):
    model = Guides

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Руководства'
        return context


class GuideDetailMain(DetailView):
    model = Guides
