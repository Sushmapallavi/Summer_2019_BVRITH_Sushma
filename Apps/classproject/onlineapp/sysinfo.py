from debug_toolbar.panels import DebugPanel
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


class MyUsefulDebugPanel(DebugPanel):
    name = 'MyUseful'
    has_content = True

    def nav_title(self):
        return _('Useful Infos')

    def title(self):
        return _('My Useful Debug Panel')

    def url(self):
        return ''

    def content(self):
        context = self.context.copy()
        context.update({
            'infos': [
                {'plop': 'plip'},
                {'plop': 'plup'},
            ],
        })
        return render_to_string('sysinfo.html', context)