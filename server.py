import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


HOST = "0.0.0.0"
PORT = 3000

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

DATA_FILE = os.path.join("storage", "data.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


class RequestHandler(BaseHTTPRequestHandler):
    def _render_template(self, template_name, context=None, status_code=200):
        if context is None:
            context = {}
        template = env.get_template(template_name)
        html_content = template.render(context)

        self.send_response(status_code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self._render_template("index.html")

        elif self.path == "/message.html":
            self._render_template("message.html")

        elif self.path == "/read":
            messages = load_data()
            self._render_template("read.html", {"messages": messages})

        elif self.path.startswith("/static/"):
            file_path = self.path.lstrip("/")
            if os.path.exists(file_path):
                self.send_response(200)
                if file_path.endswith(".css"):
                    self.send_header("Content-type", "text/css")
                elif file_path.endswith(".png"):
                    self.send_header("Content-type", "image/png")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self._render_template("error.html", status_code=404)

        else:
            self._render_template("error.html", status_code=404)

    def do_POST(self):
        if self.path == "/message":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            form_data = parse_qs(post_data)

            username = form_data.get("username", [""])[0].strip()
            message = form_data.get("message", [""])[0].strip()

            if username and message:
                messages = load_data()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                messages[timestamp] = {"username": username, "message": message}
                save_data(messages)

                self.send_response(303)
                self.send_header("Location", "/read")
                self.end_headers()
            else:
                self._render_template("error.html", status_code=400)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Server running on http://localhost:{PORT}")
    server.serve_forever()
