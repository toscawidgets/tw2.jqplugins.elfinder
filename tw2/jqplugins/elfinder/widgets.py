
# tw2-proper imports
import tw2.core as twc
from tw2.jquery import base as jqbase, defaults as jqdefaults

# imports from this package
from tw2.jqplugins.ui import base as jquibase
from tw2.jqplugins.elfinder import base as elfinderbase
from tw2.jqplugins.elfinder import defaults

modname = 'tw2.jqplugins.elfinder'

#elRTE
elfinder_images = jqbase.DirLink(modname=modname, filename=defaults._plugin_css_dirname_ % dict(name=defaults._elfinder_name_, version=defaults._elfinder_version_, subdir="images"))
elfinder_css = jqbase.jQueryPluginCSSLink(resources=[elfinder_images], name=defaults._elfinder_name_,
    basename='%s' % (defaults._elfinder_basename_),
    version=defaults._elfinder_version_,
    modname = modname
    )
elfinder_js = jqbase.jQueryPluginJSLink(name=defaults._elfinder_name_,
    basename='%s.%s' % (defaults._elfinder_basename_, defaults._elfinder_debug_),
    modname = modname,
    version=defaults._elfinder_version_)

elfinder = jqbase.jQueryJSLink(resources=[jquibase.jquery_ui_js, elfinder_css, elfinder_js])

class elFinderWidget(jquibase.JQueryUIWidget):
    resources = [jquibase.jquery_ui_js, elfinder_css, elfinder_js]
    url = twc.params.Param('Connector URL', default=twc.params.Required)
    template = 'tw2.jqplugins.elfinder.templates.widget'

    def prepare(self):
        if 'url' not in self.options:
            assert hasattr(self, 'url'), 'No url provided.   Please supply the url parameter'
            self.options['url'] = self.url
        super(elFinderWidget, self).prepare()
