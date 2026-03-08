#!/usr/bin/env python3
"""Small Python web app that serves a static page."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parent
    static_dir = project_root / "static"

    # Serve files from the static directory.
    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(*args, directory=str(static_dir), **kwargs)

    host = "0.0.0.0"
    port = 8000
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Serving static page on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
