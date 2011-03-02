import webob as wo
import elFinder
try:
    import json
except ImportError:
    import simplejson as json

class file_streamer(object):
    def __init__(self, fileobj, buffsize=4096):
        self.buffsize = buffsize
        self.fileobj = fileobj
    def __iter__(self):
        return self
    def next(self):
        chunk = self.fileobj.read(self.buffsize)
        if not chunk:
            self.fileobj.close()
            raise StopIteration
        return chunk

def make_app(app, options, basepath):
    elf = elFinder.connector(options)

    def elfinder_connector(environ, start_response):
        req = wo.Request(environ)
        if req.path_info.startswith(basepath):
            res = wo.Response()
            #call the elFinder class
            status, header, response = elf.run(req.params)
            res.status_int = status
            res.headers.update(header)
            if status == 200 and not response is None:
                if 'file' in response and isinstance(response['file'], file):
                    res.app_iter = file_streamer(response['file'])
                else:
                    res.body = json.dumps(response, indent=True)
            return res(environ, start_response)
        else:
            if app:
                st, hl, app_iter = req.call_application(app)
                try:
                    start_response(st, hl)
                    return app_iter
                finally:
                    if hasattr(app_iter, 'close'):
                        app_iter.close()
            else:
                start_response("404 NOT FOUND", [('Content-Type', 'text/html')])
                return ["No handler found for that request",]
    return elfinder_connector
