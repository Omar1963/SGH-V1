---
description: Mantener y migrar modelos SQLAlchemy 2.0 y estructuras PostgreSQL
---

---
name: database-postgresql-alembic
description: Skill avanzado para diseñar, mantener y migrar modelos SQLAlchemy 2.0 y estructuras PostgreSQL en SGH‑V1, respetando el Prompt Maestro y la arquitectura oficial.
---

# Database‑PostgreSQL‑Alembic  
Skill profesional para modelado, integridad y migraciones en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar sobre la **capa de datos** de SGH‑V1, garantizando:

- Modelos SQLAlchemy 2.0 consistentes  
- Migraciones Alembic seguras y controladas  
- Integridad referencial en PostgreSQL  
- Respeto total al modelo de datos existente  
- Aislamiento multi‑tenant por empresa  
- Compatibilidad con el flujo documental  
- No inventar campos, entidades ni relaciones  

El objetivo es **evolucionar la base de datos sin romper el sistema**.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Crear o modificar modelos en `backend/app/db/models/`
- Crear o modificar migraciones Alembic
- Ajustar relaciones entre entidades
- Revisar integridad referencial
- Optimizar consultas o índices
- Corregir errores en modelos existentes
- Preparar estructuras para dashboards o analítica
- Revisar impacto de cambios en el flujo documental

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No inventar entidades, campos ni relaciones**
- **No eliminar columnas sin instrucción explícita**
- **No alterar el flujo documental**
- **No romper el aislamiento multi‑tenant**
- **No cambiar nombres de tablas o modelos**
- **No introducir migraciones destructivas**
- **No usar SQLAlchemy 1.x**
- **No modificar roles, estados ni flujos**

---

## 4. Estructura obligatoria de modelos y migraciones
El agente debe trabajar dentro de esta estructura:

backend/
└── app/
├── db/
│    └── models/
│          ├── empresa.py
│          ├── persona.py
│          ├── documento.py
│          ├── habilitacion.py
│          └── ...
└── alembic/
├── versions/
└── env.py


---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Analizar el modelo existente**
- Revisar modelos relacionados
- Verificar claves foráneas
- Verificar restricciones
- Verificar si el cambio afecta el flujo documental

### **Paso 2 — Evaluar impacto**
- ¿Afecta a otras tablas?
- ¿Afecta a servicios o repositorios?
- ¿Afecta a roles o permisos?
- ¿Afecta a dashboards o analítica?

### **Paso 3 — Modificar el modelo SQLAlchemy**
- Usar SQLAlchemy 2.0 (ORM moderno)
- Mantener nombres exactos
- No agregar campos no autorizados
- Mantener relaciones coherentes

### **Paso 4 — Generar migración Alembic**
- Crear migración con `--autogenerate`
- Revisar manualmente el script
- Confirmar que solo contiene los cambios esperados
- Evitar operaciones destructivas

### **Paso 5 — Validar integridad**
- Revisar claves foráneas
- Revisar índices
- Revisar restricciones NOT NULL
- Revisar cascadas (evitar borrados peligrosos)

### **Paso 6 — Validar multi‑tenant**
- Confirmar que las tablas afectadas respetan el aislamiento por empresa
- Confirmar que no se exponen datos entre empresas

### **Paso 7 — Validar compatibilidad con el flujo documental**
- Confirmar que los estados no se ven afectados
- Confirmar que las relaciones no rompen el flujo

### **Paso 8 — Generar el código final**
- Código limpio, coherente y documentado
- Migración clara y reversible
- Sin duplicaciones ni inconsistencias

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Crear tablas duplicadas  
❌ Eliminar columnas críticas sin instrucción explícita  
❌ Cambiar nombres de tablas o modelos  
❌ Introducir campos no autorizados  
❌ Crear migraciones vacías o incorrectas  
❌ Usar SQLAlchemy 1.x  
❌ Crear relaciones circulares  
❌ Romper el aislamiento multi‑tenant  
❌ Alterar claves primarias existentes  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿El cambio respeta el modelo actual?  
- [ ] ¿No inventé campos ni entidades?  
- [ ] ¿La migración solo contiene los cambios necesarios?  
- [ ] ¿No hay operaciones destructivas?  
- [ ] ¿Respeté el aislamiento multi‑tenant?  
- [ ] ¿Respeté el flujo documental?  
- [ ] ¿Usé SQLAlchemy 2.0?  
- [ ] ¿El modelo es coherente con el resto del sistema?  

---

## 8. Ejemplos de delegación correctos
- “Usá Database‑PostgreSQL‑Alembic para agregar un índice en Documentos sin alterar el modelo.”  
- “Corregí la relación entre Personas y Empresas usando Database‑PostgreSQL‑Alembic.”  
- “Generá una migración para agregar un campo de auditoría, respetando el Prompt Maestro.”  
- “Revisá las migraciones existentes con Database‑PostgreSQL‑Alembic y corregí inconsistencias.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Crear migraciones  
- Corregir modelos  
- Optimizar relaciones  
- Mejorar integridad  
- Ajustar índices  
- Documentar cambios  

Este skill **NO puede**:

- Crear entidades nuevas  
- Alterar el flujo documental  
- Cambiar roles o estados  
- Introducir frameworks no autorizados  
- Realizar migraciones destructivas sin instrucción explícita  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **arquitecto de base de datos senior**, manteniendo la integridad del modelo SGH‑V1, sin bloquear la velocidad del desarrollo y garantizando consistencia en todo el proyecto.

