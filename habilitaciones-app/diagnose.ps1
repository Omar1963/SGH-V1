Write-Host "=== SGH-V1 DIAGNOSTIC SCRIPT ==="

function Test-Port {
    param($port)
    try {
        $tcp = New-Object System.Net.Sockets.TcpClient
        $tcp.Connect("localhost", $port)
        $tcp.Close()
        return $true
    }
    catch {
        return $false
    }
}

Write-Host "`n[1] Verificando Docker Desktop..."
docker info >$null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Docker Desktop NO está corriendo."
    exit 1
}
Write-Host "Docker OK."

Write-Host "`n[2] Contenedores activos:"
docker ps

Write-Host "`n[3] Verificando puertos:"
$ports = @(8000, 8080, 5432)
foreach ($p in $ports) {
    if (Test-Port $p) {
        Write-Host "Puerto $p OK"
    }
    else {
        Write-Host "Puerto $p NO responde"
    }
}

Write-Host "`n[4] Verificando Backend..."
try {
    $code = (Invoke-WebRequest -Uri "http://localhost:8000" -UseBasicParsing -TimeoutSec 3).StatusCode
    Write-Host "Backend HTTP: $code"
}
catch {
    Write-Host "Backend NO responde"
}

Write-Host "`n[5] Verificando Frontend..."
try {
    $code = (Invoke-WebRequest -Uri "http://localhost:8080" -UseBasicParsing -TimeoutSec 3).StatusCode
    Write-Host "Frontend HTTP: $code"
}
catch {
    Write-Host "Frontend NO responde"
}

Write-Host "`n[6] Verificando DB..."
docker exec sgh-db pg_isready

Write-Host "`n[7] Verificando red interna..."
docker network inspect habilitaciones-app_default >$null 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Red interna OK"
}
else {
    Write-Host "Red interna NO encontrada"
}

Write-Host "`n=== DIAGNOSTICO COMPLETO ==="
