"""Local preview server. Like `python3 -m http.server`, but missing paths get
404.html with a 404 status, the way GitHub Pages serves them."""

import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOT_FOUND = ROOT / "404.html"


class Handler(SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code != 404 or not NOT_FOUND.is_file():
            return super().send_error(code, message, explain)
        body = NOT_FOUND.read_bytes()
        self.send_response(404, message)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = ThreadingHTTPServer(("", port), partial(Handler, directory=str(ROOT)))
    print(f"Serving {ROOT} at http://localhost:{port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
