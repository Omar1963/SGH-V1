---
description: Diseñar, mantener y optimizar Dockerfiles, docker-compose y scripts de infraestructura
---

---
name: devops-docker-compose-infra
description: Skill avanzado para diseñar, mantener y optimizar Dockerfiles, docker-compose y scripts de infraestructura en SGH‑V1, respetando el Prompt Maestro y la arquitectura oficial.
---

# DevOps‑Docker‑Compose‑Infra  
Skill profesional para infraestructura y despliegue en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en la **infraestructura y contenedores** de SGH‑V1, garantizando:

- Dockerfiles optimizados y reproducibles  
- docker-compose estable y modular  
- Redes, volúmenes y dependencias bien configuradas  
- Scripts de inicialización seguros  
- Ejecución consistente en local y en contenedores  
- Compatibilidad con FastAPI, PostgreSQL y frontend HTML/JS  
- Integración fluida con Antigravity dentro o fuera del contenedor  

El objetivo es **asegurar que SGH‑V1 se ejecute de forma confiable**, sin bloquear el desarrollo y manteniendo la arquitectura oficial.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Crear o modificar Dockerfiles del backend o frontend  
- Crear o modificar `docker-compose.yml`  
- Configurar redes, volúmenes o dependencias  
- Agregar health checks  
- Preparar scripts de inicialización (migraciones, seeds)  
- Optimizar tiempos de build  
- Resolver errores de ejecución en contenedores  
- Preparar el entorno para QA o despliegue  
- Integrar Antigravity dentro del entorno Docker  

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No cambiar puertos ni nombres de servicios sin instrucción explícita**  
- **No modificar arquitectura**  
- **No inventar servicios nuevos**  
- **No eliminar dependencias críticas**  
- **No romper compatibilidad con PostgreSQL**  
- **No introducir tecnologías no autorizadas**  
- **No ejecutar migraciones destructivas automáticamente**  
- **No exponer credenciales en Dockerfiles**  

---

## 4. Estructura obligatoria de infraestructura en SGH‑V1
El agente debe trabajar dentro de esta estructura:

docker/
├── backend.Dockerfile
├── frontend.Dockerfile
├── scripts/
│     ├── init_db.sh
│     ├── run_migrations.sh
│     └── healthcheck.sh
docker-compose.yml

---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Revisar la configuración actual**
- Analizar Dockerfiles existentes  
- Revisar `docker-compose.yml`  
- Revisar redes, volúmenes y dependencias  
- Verificar compatibilidad con FastAPI y PostgreSQL  

### **Paso 2 — Optimizar Dockerfiles**
- Usar imágenes base oficiales  
- Minimizar capas  
- Aprovechar caché  
- Evitar instalar paquetes innecesarios  
- Mantener el entorno reproducible  

### **Paso 3 — Ajustar docker-compose**
- Definir servicios: backend, frontend, db  
- Configurar redes internas  
- Configurar volúmenes persistentes  
- Agregar health checks  
- Definir dependencias (`depends_on`)  

### **Paso 4 — Scripts de inicialización**
- Crear scripts para migraciones Alembic  
- Crear scripts para seeds (si el usuario lo indica)  
- Evitar scripts destructivos  
- Mantener logs claros  

### **Paso 5 — Validar ejecución**
- Confirmar que `docker-compose up` levante todo sin errores  
- Validar que el backend se conecte a PostgreSQL  
- Validar que el frontend acceda al backend  
- Validar que Antigravity pueda operar dentro del contenedor  

### **Paso 6 — Seguridad**
- No exponer credenciales  
- No usar imágenes inseguras  
- No abrir puertos innecesarios  
- No ejecutar contenedores como root (si es posible)  

### **Paso 7 — Generar el código final**
- Dockerfiles limpios y optimizados  
- docker-compose claro y modular  
- Scripts seguros y reutilizables  
- Comentarios mínimos pero útiles  

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Hardcodear credenciales  
❌ Exponer puertos innecesarios  
❌ Usar imágenes no oficiales  
❌ Ejecutar migraciones destructivas automáticamente  
❌ Crear contenedores monolíticos  
❌ Romper compatibilidad con el entorno local  
❌ Usar rutas o nombres no autorizados  
❌ Introducir servicios no solicitados (Redis, Nginx, etc.)  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿El Dockerfile es reproducible y optimizado?  
- [ ] ¿El docker-compose respeta la arquitectura?  
- [ ] ¿Los servicios tienen health checks?  
- [ ] ¿Las redes y volúmenes están bien configuradas?  
- [ ] ¿No expongo credenciales?  
- [ ] ¿No inventé servicios nuevos?  
- [ ] ¿El backend se conecta correctamente a PostgreSQL?  
- [ ] ¿Antigravity puede operar dentro del contenedor?  

---

## 8. Ejemplos de delegación correctos
- “Usá DevOps‑Docker‑Compose‑Infra para optimizar el Dockerfile del backend.”  
- “Agregá health checks al servicio de FastAPI usando DevOps‑Docker‑Compose‑Infra.”  
- “Corregí el docker-compose para que PostgreSQL persista datos correctamente.”  
- “Prepará un script de migraciones seguro usando DevOps‑Docker‑Compose‑Infra.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Crear y optimizar Dockerfiles  
- Crear y ajustar docker-compose  
- Configurar redes y volúmenes  
- Crear scripts de inicialización  
- Resolver errores de infraestructura  
- Documentar decisiones  

Este skill **NO puede**:

- Cambiar arquitectura  
- Introducir tecnologías no autorizadas  
- Inventar servicios nuevos  
- Exponer credenciales  
- Ejecutar migraciones destructivas sin instrucción explícita  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **DevOps senior**, asegurando que SGH‑V1 se ejecute de forma estable, segura y reproducible, sin bloquear el desarrollo y respetando todas las reglas del proyecto.