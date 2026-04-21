# SGH-V1

# 🛡️ Sistema Integral de Habilitaciones  
Gestión completa de personas, empresas, documentos, estados, habilitaciones y alertas, con acceso externo para empresas, flujo de aprobación documental y reportes operativos/regulatorios.

---

## 📌 Características principales

- Gestión de **personas** y **empresas**
- Carga documental interna y externa
- Flujo de aprobación:
  - Empresa carga → Consultora revisa → Responsable aprueba/rechaza
- Estados automáticos y vencimientos
- Generación de **habilitaciones** por jurisdicción
- Sistema de **alertas**
- Dashboard con KPIs y reportes
- Acceso externo seguro para empresas
- Auditoría completa
- Arquitectura modular y escalable

---

## 🧱 Arquitectura

### Backend
- **FastAPI**
- **SQLAlchemy 2.0**
- **Alembic**
- **JWT + RBAC**
- Patrón **Repository + Service**
- PostgreSQL

### Frontend
- **HTML + Bootstrap 5**
- **JavaScript modular**
- fetch() + tokens en localStorage

### Infraestructura
- Docker
- Contenedores backend / frontend / base de datos

---

## 📂 Estructura del repositorio

```
habilitaciones-app/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   ├── schemas/
│   │   │   └── dependencies/
│   │   ├── domain/
│   │   │   ├── personas/
│   │   │   ├── empresas/
│   │   │   ├── documentos/
│   │   │   ├── estados/
│   │   │   ├── habilitaciones/
│   │   │   └── alertas/
│   │   ├── db/
│   │   │   ├── models/
│   │   │   ├── migrations/
│   │   │   └── session.py
│   │   └── core/
│   └── tests/
│
├── frontend/
│   ├── *.html
│   ├── js/
│   └── css/
│
├── docs/
│   ├── DocumentoMaestro.md
│   ├── ModeloDatos.md
│   ├── OpenAPI.yaml
│   ├── UI.md
│   ├── Seguridad.md
│   └── Migracion.md
│
└── docker-compose.yml
```

---

## 🔐 Seguridad y Roles

El sistema implementa **JWT**, **RBAC** y **multi‑tenant**.

### Roles disponibles
- `ADMIN_CONSULTORA`
- `RESPONSABLE_HABILITACIONES`
- `OPERADOR_CONSULTORA`
- `EMPRESA`
- `AUDITOR`

### Acceso empresa externa
Las empresas pueden:
- Ver solo sus personas
- Ver solo sus documentos
- Cargar documentos
- Ver habilitaciones propias
- Ver alertas propias

---

## 🔄 Flujo documental

```
Empresa carga documento → PENDIENTE_EMPRESA
Consultora revisa → PENDIENTE_REVISION
Responsable aprueba → APROBADO
Responsable rechaza → RECHAZADO
Sistema marca vencidos → VENCIDO
```

---

## 📊 Dashboard y Reportes

Incluye:
- Documentos vencidos / por vencer
- Estados por jurisdicción
- Habilitaciones activas
- Alertas activas
- Reportes PDF y JSON

---

## 🚀 Instalación y ejecución

### Requisitos
- Docker + Docker Compose
- Python 3.11 (si se ejecuta sin Docker)
- Node opcional (solo si se migra a SPA)

### Ejecución con Docker

```bash
docker-compose up --build
```

Backend disponible en:  
`http://localhost:8000`

Frontend disponible en:  
`http://localhost:8080`

---

## 🧪 Testing

- Pruebas unitarias (pytest)
- Pruebas de integración (FastAPI TestClient)
- Pruebas UI (Cypress/Playwright)
- Validación de flujos críticos:
  - Aprobación documental
  - Estados automáticos
  - Acceso empresa externa

---

## 📥 Migración desde Access

Proceso ETL:

1. Extracción  
2. Transformación  
3. Carga  
4. Validación  
5. Paralelismo  
6. Corte final  

Validaciones obligatorias:
- Conteo por tabla
- Conteo por empresa
- Vigencias
- Estados
- Documentos faltantes

---

## 🗺️ Roadmap (Sprints)

1. Infraestructura  
2. Modelo de datos  
3. Seguridad  
4. Personas + Empresas  
5. Documentos + Aprobación  
6. Estados + Habilitaciones  
7. Dashboard + Reportes  
8. QA + Migración  

---

## 🤝 Contribución

1. Crear rama feature/  
2. Seguir estructura modular  
3. Respetar Documento Maestro  
4. Crear tests  
5. Pull Request con descripción clara

---

## 📄 Licencia

Proyecto interno — uso restringido.

---

## 👤 Autor

**Omar A. Domínguez**  
Arquitectura, seguridad, datos, procesos y habilitaciones.  
