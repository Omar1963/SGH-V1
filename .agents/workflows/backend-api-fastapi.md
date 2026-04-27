---
description: Mantener y corregir rutas, servicios y repositorios FastAPI
---

---
name: backend-api-fastapi
description: Skill avanzado para generar, mantener y corregir rutas, servicios y repositorios FastAPI siguiendo la arquitectura SGH‑V1 y el Prompt Maestro.
---

# Backend‑API‑FastAPI  
Skill profesional para desarrollo backend en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en el backend de SGH‑V1 respetando:

- Arquitectura oficial: FastAPI + SQLAlchemy 2.0 + Alembic  
- Patrón Repository + Service  
- Seguridad JWT + RBAC  
- Multi‑tenant por empresa  
- Flujo documental rígido  
- Estructura del repositorio  
- Reglas del Prompt Maestro  

El objetivo es **generar código correcto, seguro y consistente**, sin bloquear la creatividad ni la velocidad del desarrollo.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Crear o modificar **endpoints** en `backend/app/api/routes/`
- Crear o modificar **schemas Pydantic** en `backend/app/api/schemas/`
- Crear o modificar **repositorios** en `backend/app/domain/<modulo>/repository.py`
- Crear o modificar **servicios** en `backend/app/domain/<modulo>/service.py`
- Implementar validaciones o lógica de negocio
- Integrar dependencias de seguridad (JWT, RBAC, empresa actual)
- Revisar o corregir errores en módulos backend existentes
- Alinear código con el flujo documental

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No inventar entidades, campos, roles, estados ni flujos**
- **No cambiar arquitectura**
- **No mezclar capas**
- **No alterar el flujo documental**
- **No romper el aislamiento multi‑tenant**
- **No exponer datos de otras empresas**
- **No usar frameworks no autorizados**
- **Respetar nombres exactos de archivos, carpetas y módulos**

---

## 4. Estructura obligatoria del backend SGH‑V1
El agente debe trabajar dentro de esta estructura:

backend/
└── app/
├── api/
│    ├── routes/
│    └── schemas/
├── domain/
│    └── <modulo>/
│          ├── repository.py
│          ├── service.py
│          └── validators.py
└── db/
└── models/


---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Identificar el módulo**
- Ubicar el módulo en `backend/app/domain/<modulo>/`
- Revisar modelos, repositorio y servicio existentes
- Verificar si ya existen schemas y rutas

### **Paso 2 — Analizar el requerimiento**
- Determinar si es CRUD, lógica de negocio, validación o seguridad
- Verificar impacto en el flujo documental
- Confirmar si requiere filtrado por empresa

### **Paso 3 — Diseñar o actualizar schemas**
- Crear Request/Response según estilo del proyecto
- No agregar campos no autorizados
- Mantener nombres coherentes

### **Paso 4 — Actualizar repositorio**
- Implementar métodos usando SQLAlchemy 2.0 (ORM moderno)
- Usar `select()`, `session.execute()`, `scalars()`
- Incluir filtros por empresa cuando corresponda

### **Paso 5 — Actualizar servicio**
- Encapsular lógica de negocio
- Validar estados del flujo documental
- No acceder directamente a la BD desde el router

### **Paso 6 — Crear o modificar router**
- Definir endpoints en `routes/<modulo>.py`
- Inyectar servicio vía dependencias
- Aplicar dependencias de seguridad (JWT + RBAC)
- Filtrar por empresa actual

### **Paso 7 — Validar consistencia**
- Revisar que no se rompa el flujo documental
- Revisar que no se expongan datos de otras empresas
- Revisar que roles y permisos sean correctos

### **Paso 8 — Generar el código final**
- Código limpio, modular, sin duplicaciones
- Comentarios mínimos pero claros
- Respetar estilo del proyecto

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Lógica de negocio en el router  
❌ Acceso directo a la BD desde el router  
❌ Inventar campos o estados  
❌ Saltarse el patrón Repository + Service  
❌ Endpoints sin seguridad  
❌ Consultas sin filtro por empresa  
❌ Cambiar nombres de carpetas o archivos  
❌ Usar SQLAlchemy 1.x o estilos antiguos  
❌ Crear endpoints que alteren el flujo documental  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿Respeté la estructura del repositorio?  
- [ ] ¿Usé Repository + Service correctamente?  
- [ ] ¿Apliqué JWT + RBAC?  
- [ ] ¿Filtré por empresa?  
- [ ] ¿Respeté el flujo documental?  
- [ ] ¿No inventé campos ni estados?  
- [ ] ¿El código es claro y modular?  

---

## 8. Ejemplos de delegación correctos
- “Usá Backend‑API‑FastAPI para crear el endpoint de carga de documentos respetando el flujo PENDIENTE_EMPRESA → PENDIENTE_REVISION.”  
- “Corregí el servicio de Habilitaciones con Backend‑API‑FastAPI para asegurar que filtre por empresa.”  
- “Agregá un schema de respuesta para Personas usando Backend‑API‑FastAPI.”  
- “Revisá el router de Documentos con Backend‑API‑FastAPI y aplicá RBAC correctamente.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Crear código nuevo  
- Corregir errores  
- Optimizar consultas  
- Reorganizar lógica dentro del patrón  
- Mejorar validaciones  
- Documentar decisiones técnicas  

Este skill **NO puede**:

- Cambiar arquitectura  
- Crear entidades nuevas  
- Alterar el flujo documental  
- Modificar roles o estados  
- Introducir frameworks no autorizados  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **desarrollador backend senior**, manteniendo la arquitectura SGH‑V1, sin bloquear la velocidad del desarrollo y garantizando consistencia en todo el proyecto.

