import webtest
import webob
import os
from nose.tools import eq_
import strainer.operators as ops

import tw2.jqplugins.elfinder.connector as elconnector

class TestElFinderConnector(object):
    options = {
        'root': os.path.join(os.path.dirname(__file__), 'files')
    }
    def setup(self):
        self.app = webtest.TestApp(elconnector.make_app(None, self.options, '/files'))

    def test_na(self):
        res = self.app.get('/foo', status=404)
        eq_(res.status_int, 404)
        eq_(res.body, 'No handler found for that request')

    def test_show(self):
        res = self.app.get('/files?cmd=open')
        eq_(res.status_int, 200)
        assert res.body
        assert ops.eq_json(res.body,
                           {
                               u'cwd':
                               {
                                   u'hash': u'8b1d9657a3b75bc4ff70aeec8f8cb312',
                                   u'name': u'Home',
                                   u'read': True,
                                   u'write': True,
                                   u'mime': u'directory',
                                   u'rel': u'Home',
                                   u'date': '&ignore',
                                   u'rm': False,
                                   u'size': 0
                                },
                               u'cdc':
                               [
                                   {
                                       u'hash': u'7ec8a4d49b2f7f628c18e1e10268b25b',
                                       u'name': u'foo.txt',
                                       u'read': True,
                                       u'write': True,
                                       u'url': u'/foo.txt',
                                       u'mime': u'text/plain',
                                       u'date': '&ignore',
                                       u'rm': True,
                                       u'size': 0
                                    },
                                   {
                                       u'hash': u'b23524f6a41d3a690573dcd83fadf1b7',
                                       u'name': u'image.jpg',
                                       u'read': True,
                                       u'write': True,
                                       u'url': u'/image.jpg',
                                       u'mime': u'image/jpeg',
                                       u'date': '&ignore',
                                       u'rm': True,
                                       u'size': 0
                                   }
                               ]
                           }
                           )

    def test_get_file(self):
        res = self.app.get('/files?cmd=open&current=8b1d9657a3b75bc4ff70aeec8f8cb312&target=b23524f6a41d3a690573dcd83fadf1b7')
        eq_(res.status_int, 200)
        eq_(res.content_type, u'image/jpeg')
        eq_(res.content_length, 307)
        eq_(res.body, open(os.path.join(os.path.dirname(__file__), 'files/image.jpg')).read())
