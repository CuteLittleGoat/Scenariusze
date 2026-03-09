#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

python3 "${SCRIPT_DIR}/generate_manifest.py"

echo "Uruchamiam serwer lokalny na http://localhost:8000/Main/index.html"
cd "${REPO_ROOT}"
python3 -m http.server 8000
