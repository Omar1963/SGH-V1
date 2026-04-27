Write-Host "=== SGH-V1 START SCRIPT ==="

$compose = "C:\Users\Admin\GitHub\SGH-V1\habilitaciones-app\docker\docker-compose.yml"

if (-Not (Test-Path $compose)) {
    Write-Host "ERROR: No se encontró docker-compose.yml en ruta: $compose"
    exit 1
}

Write-Host "`n[1] Verificando Docker Desktop..."
$dockerStatus = docker info 2>$null

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Docker Desktop NO está corriendo."
    exit 1
}

Write-Host "Docker OK."

Write-Host "`n[2] Levantando contenedores..."
docker compose -f $compose up -d --build

Write-Host "`n[3] Contenedores activos:"
docker ps

Write-Host "`nSGH-V1 iniciado correctamente."
