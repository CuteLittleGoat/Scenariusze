#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import generate_manifest


class ManifestHandler(SimpleHTTPRequestHandler):
    endpoint_paths = {"/refresh-manifest", "/Main/refresh-manifest"}

    def _json_response(self, status: HTTPStatus, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _handle_manifest_refresh(self) -> None:
        if self.path not in self.endpoint_paths:
            self._json_response(HTTPStatus.NOT_FOUND, {"ok": False, "error": "Nieznana ścieżka."})
            return

        try:
            generate_manifest.main()
            self._json_response(HTTPStatus.OK, {"ok": True})
        except Exception as error:  # pragma: no cover
            self._json_response(HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "error": str(error)})

    def do_POST(self) -> None:  # noqa: N802
        self._handle_manifest_refresh()

    def do_GET(self) -> None:  # noqa: N802
        if self.path in self.endpoint_paths:
            self._handle_manifest_refresh()
            return
        super().do_GET()


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    os.chdir(repo_root)

    host = "0.0.0.0"
    port = 8000
    server = ThreadingHTTPServer((host, port), ManifestHandler)

    print("Manifest i serwer UI: http://localhost:8000/Main/index.html")
    print("Endpoint POST: http://localhost:8000/refresh-manifest")
    server.serve_forever()


if __name__ == "__main__":
    main()
