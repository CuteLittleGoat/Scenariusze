$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

python (Join-Path $ScriptDir 'generate_manifest.py')

Write-Host 'Uruchamiam serwer lokalny na http://localhost:8000/Main/index.html'
python (Join-Path $ScriptDir 'local_server.py')
