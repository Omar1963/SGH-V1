---
description: Crear, mantener y mejorar vistas HTML, componentes Bootstrap y JavaScript modular
---

---
name: frontend-ui-html-bootstrap-js
description: Skill avanzado para crear, mantener y mejorar vistas HTML, componentes Bootstrap y JavaScript modular en SGH‑V1, respetando el Prompt Maestro y la arquitectura oficial.
---

# Frontend‑UI‑HTML‑Bootstrap‑JS  
Skill profesional para desarrollo de interfaz en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en el **frontend de SGH‑V1**, garantizando:

- Vistas HTML limpias, claras y modulares  
- Uso correcto de Bootstrap 5  
- JavaScript modular organizado por pantallas  
- Integración con la API mediante `fetch()` y `api.js`  
- Respeto por roles, permisos y multi‑tenant  
- Flujo documental visible y entendible para el usuario  
- Experiencia de usuario clara, sin fricciones  

El objetivo es **crear interfaces funcionales, seguras y fáciles de usar**, sin introducir frameworks no autorizados.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Crear o modificar archivos HTML en `frontend/*.html`
- Crear o modificar scripts JS en `frontend/js/*.js`
- Diseñar formularios, tablas, modales o componentes UI
- Integrar pantallas con la API FastAPI
- Mejorar la experiencia del usuario (UX)
- Validar roles y permisos en la interfaz
- Mostrar estados del flujo documental
- Manejar errores y mensajes al usuario
- Optimizar carga, navegación o interacción

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No usar frameworks SPA (React, Vue, Angular, etc.)**
- **No inventar campos ni entidades**
- **No modificar roles ni estados**
- **No romper el flujo documental**
- **No exponer datos de otras empresas**
- **No cambiar la estructura del repositorio**
- **Usar siempre Bootstrap + JS modular**
- **Usar api.js como wrapper para fetch()**

---

## 4. Estructura obligatoria del frontend SGH‑V1
El agente debe trabajar dentro de esta estructura:

frontend/
├── index.html
├── personas.html
├── documentos.html
├── habilitaciones.html
├── js/
│    ├── api.js
│    ├── personas.js
│    ├── documentos.js
│    ├── habilitaciones.js
│    └── utils.js
└── css/ (opcional)


---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Identificar la pantalla**
- Ubicar el archivo HTML correspondiente  
- Revisar si existe un JS asociado  
- Verificar roles que pueden acceder  

### **Paso 2 — Diseñar la estructura HTML**
- Usar contenedores Bootstrap (`container`, `row`, `col`)  
- Usar componentes estándar (cards, tables, forms, alerts, modals)  
- Mantener una jerarquía clara y semántica  

### **Paso 3 — Conectar con JS modular**
- Crear o actualizar el archivo en `frontend/js/<modulo>.js`  
- Importar funciones desde `api.js`  
- Manejar eventos (`submit`, `click`, `change`)  
- Actualizar DOM de forma clara y segura  

### **Paso 4 — Integrar con la API**
- Usar `api.js` para todas las llamadas  
- Manejar estados de carga (spinners, disabled)  
- Manejar errores (alerts, mensajes claros)  
- Validar permisos según rol  

### **Paso 5 — Respetar multi‑tenant**
- No permitir seleccionar empresas ajenas  
- No mostrar datos de otras empresas  
- Validar que los endpoints usados ya filtran por empresa  

### **Paso 6 — Mostrar el flujo documental**
- Mostrar estados (`PENDIENTE_EMPRESA`, `PENDIENTE_REVISION`, etc.)  
- Mostrar acciones permitidas según rol  
- Mostrar mensajes claros en cada transición  

### **Paso 7 — Validar UX**
- Formularios simples y claros  
- Botones visibles y accesibles  
- Mensajes de error comprensibles  
- Evitar pasos innecesarios  

### **Paso 8 — Generar el código final**
- HTML limpio y ordenado  
- JS modular, sin duplicaciones  
- Bootstrap bien aplicado  
- Comentarios mínimos pero útiles  

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Usar frameworks SPA (React, Vue, Angular)  
❌ Escribir lógica de negocio en el frontend  
❌ Llamar a la API sin pasar por `api.js`  
❌ Manipular datos de otras empresas  
❌ Crear pantallas que rompan el flujo documental  
❌ Usar estilos inline excesivos  
❌ Crear JS monolítico o no modular  
❌ Duplicar código en múltiples pantallas  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿Usé Bootstrap correctamente?  
- [ ] ¿El JS está en un archivo modular?  
- [ ] ¿Usé `api.js` para las llamadas?  
- [ ] ¿Validé roles y permisos?  
- [ ] ¿Respeté el flujo documental?  
- [ ] ¿No expongo datos de otras empresas?  
- [ ] ¿La UI es clara y fácil de usar?  
- [ ] ¿El código es limpio y mantenible?  

---

## 8. Ejemplos de delegación correctos
- “Usá Frontend‑UI‑HTML‑Bootstrap‑JS para crear una tabla de Documentos con filtros y paginación.”  
- “Conectá el formulario de Personas a la API usando Frontend‑UI‑HTML‑Bootstrap‑JS.”  
- “Mejorá la pantalla de Habilitaciones mostrando el estado del flujo documental.”  
- “Agregá validaciones de formulario usando Frontend‑UI‑HTML‑Bootstrap‑JS.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Crear pantallas nuevas  
- Mejorar UI/UX  
- Integrar con la API  
- Manejar errores y estados  
- Optimizar interacción  
- Documentar decisiones  

Este skill **NO puede**:

- Cambiar arquitectura  
- Introducir frameworks SPA  
- Modificar roles o estados  
- Alterar el flujo documental  
- Inventar campos o entidades  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **frontend senior**, creando interfaces claras, seguras y consistentes, sin bloquear la velocidad del desarrollo y respetando la arquitectura SGH‑V1.