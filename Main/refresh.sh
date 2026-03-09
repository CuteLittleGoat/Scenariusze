#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "${SCRIPT_DIR}/generate_manifest.py"

echo "Uruchamiam serwer lokalny na http://localhost:8000/Main/index.html"
python3 "${SCRIPT_DIR}/local_server.py"
