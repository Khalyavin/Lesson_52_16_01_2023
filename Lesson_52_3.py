import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    data_file_address = 'lisl.json'

    def _get_json_from_file(self):
        with open(self.data_file_address, encoding='UTF-8') as list_file:
            return json.load(list_file)

    def _write_data_to_json(self, data):
        with open(self.data_file_address, 'w', encoding="UTF-8") as list_file:
            json.dump(data, list_file)

    def do_GET(self):
#        result_string = json.dumps(self._get_json_from_file())
        result_string = 'Hello, World wide web!'

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(result_string, 'UTF-8'))

    def do_POST(self):
#        data_from_file = self._get_json_from_file()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        data_from_request = json.loads(post_data)
        print(data_from_request)
#        data_from_file.append(data_from_request)
#        self._write_data_to_json(data_from_file)

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('{"result": "ok"}', 'UTF-8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print('Server stopped.')











