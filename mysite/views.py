import logging

from django.apps import apps
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)

# --- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dictVerbose = {}
        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context
