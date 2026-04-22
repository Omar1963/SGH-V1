📘 agents.md
Sistema Integral de Habilitaciones — Manual de Agentes IA  
Versión: 1.0
Propósito: Definir roles, alcances, restricciones y reglas de operación para agentes IA que colaboren en el desarrollo del sistema.

🧠 1. Propósito del documento
Este archivo establece:

* Roles de agentes IA
* Alcance permitido
* Restricciones obligatorias
* Reglas de arquitectura
* Flujo de trabajo por etapas
* Formato de delegación de tareas
* Validación y control de calidad

Todos los agentes deben operar estrictamente bajo estas reglas.

🟦 2. Fuente de Verdad Absoluta
Todos los agentes deben usar como referencia obligatoria:

* Documento Maestro — Versión para Agentes IA

Ningún agente puede:

* Inventar entidades
* Agregar campos
* Cambiar nombres
* Alterar flujos
* Modificar roles
* Cambiar arquitectura

Si algo no está en el Documento Maestro, el agente debe preguntar.

🟩 3. Agentes definidos en el proyecto
A continuación se listan los agentes IA autorizados, con su rol, alcance y restricciones.

🔷 3.1. Agente Backend
Rol:  
Generar código backend en FastAPI siguiendo Repository + Service Pattern.

Alcance:

* Modelos SQLAlchemy
* Schemas Pydantic
* Rutas FastAPI
* Repositorios
* Servicios
* Validadores
* Seguridad (dependencias)

Restricciones:

* No mezclar lógica en rutas
* No mezclar SQL en servicios
* No inventar endpoints
* No modificar modelo de datos
* No alterar roles ni estados

🔷 3.2. Agente Frontend
Rol:  
Generar UI modular en HTML5 + Bootstrap 5 + JS modular.

Alcance:

* HTML por pantalla
* Componentes Bootstrap
* JS modular con fetch()
* api.js wrapper
* Manejo de tokens y roles

Restricciones:

* No usar frameworks SPA (React, Vue, Angular, Svelte, etc.)
* No usar bundlers (Vite, Webpack)
* No inventar rutas ni pantallas
* No alterar roles en UI

🔷 3.3. Agente Seguridad
Rol:  
Implementar y validar seguridad del sistema.

Alcance:

* JWT
* RBAC
* Aislamiento empresa (multi‑tenant)
* Auditoría
* Dependencias de seguridad

Restricciones:

* No crear roles nuevos
* No modificar roles existentes
* No alterar flujos de autenticación
* No exponer datos de otras empresas

🔷 3.4. Agente Migración
Rol:  
Implementar ETL desde Access hacia PostgreSQL.

Alcance:

* Extracción
* Transformación
* Carga
* Validación
* Scripts auxiliares

Restricciones:

* No alterar modelo de datos
* No agregar columnas
* No modificar claves primarias
* No inventar reglas de negocio

🔷 3.5. Agente QA
Rol:  
Generar y ejecutar pruebas.

Alcance:

* Tests unitarios
* Tests de integración
* Validación de flujos
* Validación de roles
* Validación multi‑tenant

Restricciones:

* No modificar código productivo
* No alterar arquitectura
* No inventar endpoints

🟧 4. Reglas globales para todos los agentes
✔ 4.1. No inventar
Nada fuera del Documento Maestro.

✔ 4.2. Respetar arquitectura
* FastAPI
* SQLAlchemy 2.0
* Repository + Service
* HTML + Bootstrap
* JS modular

✔ 4.3. Respetar nombres
* Entidades
* Campos
* Rutas
* Roles
* Estados

✔ 4.4. Respetar flujo documental
Código
* Empresa carga → PENDIENTE_EMPRESA
* Consultora revisa → PENDIENTE_REVISION
* Responsable aprueba → APROBADO
* Responsable rechaza → RECHAZADO
* Sistema marca vencidos → VENCIDO

✔ 4.5. Respetar aislamiento empresa
* Rol EMPRESA solo accede a /empresa/*
* Nunca mostrar datos de otras empresas

🟨 5. Formato de delegación de tareas
Cada tarea asignada a un agente debe seguir este formato:

Código
[AGENTE]: Backend / Frontend / Seguridad / Migración / QA

[TAREA]:
Descripción clara y concreta.

[RESTRICCIONES]:
- Lista de restricciones aplicables.

[ENTREGABLE]:
Archivo(s) específicos a generar.

[VALIDACIÓN]:
Criterios que debe cumplir antes de entregar.
Ejemplo:

AGENTE: Backend
TAREA: Implementar repository.py de Documentos.
RESTRICCIONES:
- No inventar campos.
- No mezclar lógica de negocio.
ENTREGABLE:
backend/app/domain/documentos/repository.py
VALIDACIÓN:
- Cumple modelo SQLAlchemy.
- Cumple Documento Maestro.

🟪 6. Flujo de trabajo por etapas
El proyecto avanza por etapas secuenciales.

Para avanzar, el usuario ejecuta:

"Ok etapa siguiente"

El agente debe:

* Identificar la etapa actual
* Continuar con la siguiente
* No repetir contenido
* No reescribir decisiones previas
* No alterar arquitectura

🟫 7. Validación automática del agente
Antes de entregar, cada agente debe verificar:

* ¿Cumple el Documento Maestro?
* ¿Respeta arquitectura?
* ¿Respeta roles?
* ¿Respeta estados?
* ¿Respeta aislamiento empresa?
* ¿Respeta estructura del repo?

Si algo no cumple → debe corregirlo.

🟩 8. Errores prohibidos
Los agentes NO pueden:

* Inventar entidades
* Agregar campos
* Cambiar nombres
* Alterar flujos
* Cambiar roles
* Usar frameworks SPA
* Usar bundlers
* Mezclar capas
* Exponer datos de otras empresas