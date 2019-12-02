from django.views.generic import TemplateView
from .scrappers.ml import getitemsml


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items_ml'] = getitemsml()

        return context
