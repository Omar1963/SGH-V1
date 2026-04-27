---
description:  Diseñar métricas, KPIs, consultas y dashboards
---

name: data-insights-dashboards
description: Skill avanzado para diseñar métricas, KPIs, consultas y dashboards en SGH‑V1, respetando el Prompt Maestro, la arquitectura oficial y el modelo de datos existente.
---

# Data‑Insights‑Dashboards  
Skill profesional para analítica y visualización en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en la **analítica de datos y dashboards** de SGH‑V1, garantizando:

- KPIs relevantes para empresas, consultoras y responsables  
- Consultas SQL optimizadas y seguras  
- Endpoints de analítica en FastAPI  
- Dashboards basados en HTML + Bootstrap + JS  
- Métricas alineadas al flujo documental  
- Respeto por el aislamiento multi‑tenant  
- No inventar campos ni entidades  
- No alterar la arquitectura  

El objetivo es **convertir los datos del sistema en información útil**, sin romper la estructura del proyecto.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Diseñar dashboards o reportes  
- Crear KPIs o métricas  
- Crear endpoints de analítica  
- Optimizar consultas SQL  
- Preparar datos para visualizaciones  
- Analizar tendencias o patrones  
- Responder preguntas del negocio  
- Mejorar la toma de decisiones  
- Validar integridad de datos para reportes  

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No inventar campos ni entidades**  
- **No modificar roles ni estados**  
- **No alterar el flujo documental**  
- **No romper el aislamiento multi‑tenant**  
- **No introducir librerías externas no autorizadas**  
- **No cambiar arquitectura**  
- **No usar frameworks SPA**  
- **Dashboards = HTML + Bootstrap + JS modular**  

---

## 4. Tipos de métricas permitidas en SGH‑V1
El agente puede diseñar métricas basadas en:

### **Documentos**
- Documentos cargados por empresa  
- Documentos en cada estado del flujo  
- Documentos vencidos  
- Documentos rechazados  
- Tiempos promedio de revisión  

### **Personas**
- Personas habilitadas  
- Personas con documentos vencidos  
- Personas con habilitaciones próximas a vencer  

### **Habilitaciones**
- Habilitaciones activas  
- Habilitaciones vencidas  
- Habilitaciones por tipo  
- Tiempos de aprobación  

### **Consultoras / Responsables**
- Tiempos de respuesta  
- Cantidad de aprobaciones  
- Cantidad de rechazos  
- Carga de trabajo por responsable  

### **Multi‑tenant**
- Métricas por empresa  
- Comparativas internas (nunca cruzadas entre empresas)  

---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Identificar la pregunta del negocio**
Ejemplos:

- “¿Cuántas habilitaciones vencen este mes?”  
- “¿Qué empresa tiene más documentos rechazados?”  
- “¿Qué responsable aprueba más rápido?”  

### **Paso 2 — Revisar el modelo de datos**
- Identificar tablas involucradas  
- Identificar relaciones  
- Identificar estados del flujo documental  

### **Paso 3 — Diseñar la consulta**
- Usar SQLAlchemy 2.0  
- Optimizar filtros  
- Respetar multi‑tenant  
- Evitar joins innecesarios  
- Evitar subconsultas pesadas  

### **Paso 4 — Crear endpoint de analítica**
- En `backend/app/api/routes/analytics.py`  
- Respuesta clara y estructurada  
- Validar rol y permisos  
- Filtrar por empresa  

### **Paso 5 — Preparar datos para dashboard**
- Normalizar datos  
- Ordenar por relevancia  
- Preparar series temporales si aplica  

### **Paso 6 — Diseñar dashboard HTML**
- Usar Bootstrap (cards, badges, tables, progress bars)  
- Evitar gráficos complejos (no usar librerías externas sin permiso)  
- Mantener claridad visual  

### **Paso 7 — Integrar con JS**
- Llamar al endpoint desde `frontend/js/analytics.js`  
- Renderizar métricas en cards o tablas  
- Actualizar dinámicamente  

### **Paso 8 — Validar resultados**
- Revisar coherencia  
- Revisar multi‑tenant  
- Revisar permisos  
- Revisar performance  

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Inventar métricas no basadas en datos reales  
❌ Exponer datos de otras empresas  
❌ Crear dashboards con frameworks SPA  
❌ Consultas SQL pesadas sin índices  
❌ Endpoints sin validación de rol  
❌ Métricas que rompan el flujo documental  
❌ Crear entidades nuevas para analítica  
❌ Usar librerías externas sin autorización  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿La métrica responde una pregunta real del negocio?  
- [ ] ¿La consulta respeta multi‑tenant?  
- [ ] ¿La consulta está optimizada?  
- [ ] ¿El endpoint valida roles y permisos?  
- [ ] ¿El dashboard es claro y útil?  
- [ ] ¿Usé HTML + Bootstrap + JS modular?  
- [ ] ¿No inventé campos ni entidades?  
- [ ] ¿El resultado es fácil de interpretar?  

---

## 8. Ejemplos de delegación correctos
- “Usá Data‑Insights‑Dashboards para crear un KPI de documentos vencidos por empresa.”  
- “Generá un dashboard simple con habilitaciones próximas a vencer.”  
- “Creá un endpoint de analítica para tiempos de aprobación.”  
- “Optimizar la consulta de documentos rechazados usando Data‑Insights‑Dashboards.”  
- “Diseñá un panel para responsables con métricas de carga de trabajo.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Crear KPIs  
- Crear dashboards  
- Crear endpoints de analítica  
- Optimizar consultas  
- Preparar datos para visualización  
- Documentar decisiones analíticas  

Este skill **NO puede**:

- Cambiar arquitectura  
- Introducir frameworks SPA  
- Inventar entidades o campos  
- Exponer datos entre empresas  
- Alterar el flujo documental  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **analista de datos senior**, transformando los datos de SGH‑V1 en información útil, sin romper la arquitectura ni las reglas del proyecto, y manteniendo dashboards claros, seguros y eficientes.

