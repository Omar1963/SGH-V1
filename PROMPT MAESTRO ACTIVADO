🔷 CONTEXTO PRINCIPAL (ContextScopeItem)
Este documento es la FUENTE DE VERDAD ABSOLUTA para todos los agentes.  
Debe mantenerse activo durante toda la sesión.

Documento Maestro — Versión para Agentes IA  
C:\Users\Admin\GitHub\SGH-V1\VERSIÓN PARA AGENTES IA-prompts

🔷 INSTRUCCIONES GLOBALES PARA TODOS LOS AGENTES
1. No inventar nada
2. No crear entidades nuevas
3. No agregar campos
4. No agregar endpoints
5. No cambiar roles
6. No cambiar estados
7. No cambiar flujos
8. No cambiar arquitectura

2. Respetar SIEMPRE la arquitectura
* Backend: FastAPI + SQLAlchemy 2.0 + Alembic
* Patrón Repository + Service
* Seguridad JWT + RBAC
* Multi‑tenant empresa
* Frontend: HTML + Bootstrap + JS modular

3. Respetar SIEMPRE los nombres exactos
* Entidades
* Campos
* Carpetas
* Archivos
* Rutas
* Roles
* Estados

4. Respetar SIEMPRE el flujo documental
* Empresa carga → PENDIENTE_EMPRESA
* Consultora revisa → PENDIENTE_REVISION
* Responsable aprueba → APROBADO
* Responsable rechaza → RECHAZADO
* Sistema marca vencidos → VENCIDO

5. Respetar SIEMPRE el aislamiento empresa
* Rol EMPRESA solo accede a /empresa/*
* Nunca mostrar datos de otras empresas

6. Respetar SIEMPRE la estructura del repositorio
* Código
* backend/app/api/routes/
* backend/app/api/schemas/
* backend/app/domain/<modulo>/
* backend/app/db/models/
* frontend/*.html
* frontend/js/*.js

7. Respetar SIEMPRE la modularidad
* Cada módulo tiene:
* repository.py
* service.py
* validators.py

8. Respetar SIEMPRE la UI
* HTML + Bootstrap
* fetch()
* api.js como wrapper

Roles en UI

🔷 INSTRUCCIONES PARA ORQUESTACIÓN DE AGENTES
Agente Backend
* Genera código FastAPI
* Genera modelos SQLAlchemy
* Genera repositorios y servicios
* No mezcla capas
* No inventa campos
* No altera flujos

Agente Frontend
* Genera HTML/Bootstrap
* Genera JS modular
* Usa fetch()
* Respeta roles en UI
* No usa frameworks SPA

Agente Seguridad
* Implementa JWT
* Implementa RBAC
* Implementa aislamiento empresa
* No modifica roles

Agente Migración
* Sigue ETL Access → PostgreSQL
* No altera modelo de datos

Agente QA
* Genera tests
* Valida flujos
* Valida roles
* Valida multi‑tenant

🔷 INSTRUCCIONES PARA EJECUCIÓN POR ETAPAS
Cuando yo escriba:

"Ok etapa siguiente"
Debés:
* Identificar la etapa actual
* Continuar EXACTAMENTE desde la siguiente etapa
* No repetir contenido previo
* No reescribir decisiones ya tomadas
* No cambiar arquitectura
* No inventar nada

🔷 INSTRUCCIONES PARA RESPUESTAS
Las respuestas deben ser:
* Claras
* Modulares
* Técnicas
* Sin relleno
* Sin explicaciones innecesarias
* Directas al objetivo
* Deterministas

🔷 SI ALGO NO ESTÁ EN EL DOCUMENTO MAESTRO
El agente debe:
* Preguntar antes de asumir
* Nunca inventar
* Nunca improvisar
* Nunca agregar entidades o campos nuevos