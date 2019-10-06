import async_server
import os
import sys
import StringIO

class AsyncWSGIServer(async_server.AsyncServer):

    def set_app(self, app):
        self.application = app

    def get_app(self):
        return self.application


class AsyncWSGIRequestHandler(async_server.AsyncHTTPRequestHandler):

    def get_environ(self):
        env = {
         'wsgi.version': (1, 0),
         'wsgi.url_scheme': 'http',
         'wsgi.input': StringIO.StringIO(self.request_body),
         'wsgi.errors': sys.stderr,
         'wsgi.multithread': False,
         'wsgi.multiprocess': False,
         'wsgi.run_once': False,
         'REQUEST_METHOD': self.method,
         'PATH_INFO': self.path,
         'SERVER_NAME': self.server_name,
         'SERVER_PORT': str(self.server_port)
              }

        return env

    def start_response(self, status, headers):
        code, message = status.split(" ")[:2]
        self.init_response(code, message)

        for key, value in headers:
            self.add_header(key, value)

        self.end_headers()

    def handle_request(self):
        env = self.get_environ()
        app = server.get_app()
        result = app(env, self.start_response)
        self.finish_response(result)

    def finish_response(self, result):
        self.send(bytes(self.response.encode('utf-8')) + result[0])
        self.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    server = AsyncWSGIServer(handler_class=AsyncWSGIRequestHandler)
    server.set_app(application)
    server.serve_forever()
