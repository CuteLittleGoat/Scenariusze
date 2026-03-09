$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir '..')

python (Join-Path $ScriptDir 'generate_manifest.py')

Write-Host 'Uruchamiam serwer lokalny na http://localhost:8000/Main/index.html'
Set-Location $RepoRoot
python -m http.server 8000
