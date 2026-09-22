# Flow Kit — Windows PowerShell Setup Script
$ErrorActionPreference = "Stop"

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Flow Kit — Windows Setup" -ForegroundColor Cyan
Write-Host "========================================="
Write-Host ""

# 1. Check Python
Write-Host "Checking Python..."
try {
    $pyVersion = python --version 2>&1
    Write-Host "  OK: $pyVersion" -ForegroundColor Green
} catch {
    Write-Host "  MISSING: Python 3 not found on PATH. Vui lòng cài Python 3.10+ từ python.org" -ForegroundColor Red
    exit 1
}

# 2. Check ffmpeg
Write-Host "Checking ffmpeg..."
if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
    $ffVer = ffmpeg -version | Select-Object -First 1
    Write-Host "  OK: $ffVer" -ForegroundColor Green
} else {
    Write-Host "  WARNING: ffmpeg not found. Tải ffmpeg và thêm vào PATH để ghép video/audio." -ForegroundColor Yellow
}

# 3. Virtual Environment
Write-Host "Setting up Python virtual environment (venv)..."
if (-not (Test-Path "venv")) {
    python -m venv venv
    Write-Host "  Created: venv/" -ForegroundColor Green
} else {
    Write-Host "  Exists: venv/" -ForegroundColor Green
}

# 4. Install Dependencies
Write-Host "Installing Python dependencies..."
& ".\venv\Scripts\python.exe" -m pip install -q --upgrade pip
& ".\venv\Scripts\python.exe" -m pip install -q -r requirements.txt
Write-Host "  Dependencies installed successfully." -ForegroundColor Green

# 5. Verify Import
Write-Host "Verifying agent can import..."
& ".\venv\Scripts\python.exe" -c "from agent.main import app; print('  OK: agent.main imports successfully')"

# 6. Sync skills
Write-Host "Syncing FlowKit skills..."
& ".\venv\Scripts\python.exe" setup.py --tool all
& ".\venv\Scripts\python.exe" scripts/sync_antigravity.py

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "  Setup complete!" -ForegroundColor Cyan
Write-Host "========================================="
Write-Host ""
Write-Host "Các bước tiếp theo:"
Write-Host "  1. Kích hoạt môi trường ảo: .\venv\Scripts\Activate.ps1"
Write-Host "  2. Khởi động server FlowKit: python -m agent.main"
Write-Host "  3. Kiểm tra kết nối: curl http://127.0.0.1:8100/health"
