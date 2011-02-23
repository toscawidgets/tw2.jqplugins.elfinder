from tw2.core.testbase import WidgetTest, TestInPage, assert_in_xhtml

from nose.tools import raises

import tw2.jqplugins.elfinder.widgets as w
import re

class TestelfinderCSS(WidgetTest):
    widget = w.elfinder_css
    attrs = {}
    params = {}
    expected = """
<link rel="stylesheet" type="text/css" href="/resources/tw2.jqplugins.elfinder/static/jquery/plugins/elfinder/1.1/css/elfinder.css" media="all"/>
"""
class TestelfinderJS(WidgetTest):
    widget = w.elfinder_js
    attrs = {}
    params = {}
    expected = """
<script type="text/javascript" src="/resources/tw2.jqplugins.elfinder/static/jquery/plugins/elfinder/1.1/js/elfinder.full.js"></script>
"""

#class TestURLRequired(WidgetTest):
#    wrap = True
#    widget = w.elFinderWidget(id='widget')
#    attrs = {}
#    params = {}
#    expected = """
#<textarea id="widget"></textarea>
#<script type="text/javascript">
#$(function() {
#    $("#widget").elfinder({});
#});
#</script>
#"""
#
#    @raises(AssertionError)
#    def test_raises(self):
#        self._check_rendering_vs_expected('mako', self.attrs, self.params, self.expected)
#    def test_display(self):
#        pass

    
class TestBase(WidgetTest):
    wrap = True
    widget = w.elFinderWidget
    attrs = {'id': 'widget', 'url': '/flabbrith'}
    params = {}
    expected = """
<textarea id="widget"></textarea>
<script type="text/javascript">
$(function() {
    $("#widget").elfinder({url: '/flabbrith'});
});
</script>
"""

class TestBaseParams(WidgetTest):
    wrap = True
    widget = w.elFinderWidget
    attrs = {'id': 'widget'}
    params = {'url': '/flabbrith'}
    expected = """
<textarea id="widget"></textarea>
<script type="text/javascript">
$(function() {
    $("#widget").elfinder({url: '/flabbrith'});
});
</script>
"""

class TestAdvanced(TestBase):
    wrap = True
    params = {
        'options': {
            'url': '/flabbit'
        }
    }
    expected = """
<textarea id="widget"></textarea>
<script type="text/javascript">
$(function() {
    $("#widget").elfinder({"url": "/flabbit"});
});
</script>
"""

class TestBasePage(TestInPage):
    inject_widget = w.elFinderWidget(id='widget', url="/flabbrith")

    contents = [
        '/resources/tw2.jquery/static/jquery/[^/]*/jquery(\.(full|min))?\.js',
        '/resources/tw2.jqplugins.ui/static/jquery/ui/[^/]*/css/[^/]*/jquery-ui.css',
        '/resources/tw2.jqplugins.ui/static/jquery/ui/[^/]*/js/jquery-ui(\.(min|full))?\.js',
        '''\$\("#widget"\)\.elfinder\({['"]?url['"]?: ['"]/flabbrith['"]}\);'''
    ]

    def custom_display(self):
        return self.inject_widget.display()

    def _test_contents(self, body):
        for x in self.contents:
            m = re.search(x, body)
            assert m is not None, '%s was not found in %s' % (x, body)

    def test_el_finder_widget(self):
        res = self.app.get('/')
        self._test_contents(res.body)
        assert_in_xhtml('<link rel="stylesheet" type="text/css" href="/resources/tw2.jqplugins.elfinder/static/jquery/plugins/elfinder/1.1/css/elfinder.css" media="all" />', res.body)
        assert_in_xhtml('<script type="text/javascript" src="/resources/tw2.jqplugins.elfinder/static/jquery/plugins/elfinder/1.1/js/elfinder.full.js">', res.body)
