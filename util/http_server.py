import threading
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpHealthServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/actuator/health' or self.path == '/actuator/info':
            self.send_response(HTTPStatus.OK)
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    @staticmethod
    def run_thread(port=8080):
        httpd = HTTPServer(('', port), HttpHealthServer)
        t = threading.Thread(target=httpd.serve_forever)
        t.setDaemon(True)
        t.start()
