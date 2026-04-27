---
description: 
---

---
name: testing-qa-automation
description: Skill avanzado para diseñar, mantener y ejecutar pruebas unitarias, de integración y validación funcional en SGH‑V1, respetando el Prompt Maestro y la arquitectura oficial.
---

# Testing‑QA‑Automation  
Skill profesional para pruebas y aseguramiento de calidad en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en la **calidad del sistema SGH‑V1**, garantizando:

- Pruebas unitarias con pytest  
- Pruebas de integración backend  
- Validación de roles y permisos (RBAC)  
- Validación del flujo documental  
- Validación del aislamiento multi‑tenant  
- Pruebas de frontend (JS) cuando corresponda  
- Detección temprana de errores  
- Prevención de regresiones  

El objetivo es **asegurar que SGH‑V1 funcione correctamente en cada módulo**, sin bloquear el desarrollo y manteniendo la coherencia del proyecto.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Crear o modificar tests de backend (pytest)  
- Crear o modificar tests de frontend (Vitest/Jest o JS nativo)  
- Validar flujos completos (documentos, personas, habilitaciones)  
- Validar roles y permisos  
- Validar multi‑tenant  
- Testear endpoints nuevos o modificados  
- Testear servicios y repositorios  
- Detectar inconsistencias o regresiones  
- Revisar errores reportados por usuarios  

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No modificar roles ni estados**  
- **No alterar el flujo documental**  
- **No inventar entidades ni campos**  
- **No romper el aislamiento multi‑tenant**  
- **No cambiar arquitectura**  
- **No usar frameworks no autorizados**  
- **No mezclar lógica de negocio en los tests**  
- **No depender de datos manuales o externos**  

---

## 4. Estructura obligatoria de pruebas en SGH‑V1
El agente debe trabajar dentro de esta estructura:

backend/
└── tests/
├── conftest.py
├── test_personas.py
├── test_documentos.py
├── test_habilitaciones.py
├── test_auth.py
└── utils/


Para frontend:

rontend/
└── tests/
├── test_personas.js
├── test_documentos.js
└── utils/


---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Identificar el alcance**
- ¿Es unitario? (servicio, repositorio, función)  
- ¿Es integración? (endpoint, flujo completo)  
- ¿Es validación de roles?  
- ¿Es validación de multi‑tenant?  

### **Paso 2 — Preparar el entorno de pruebas**
- Usar fixtures de BD temporales  
- Usar cliente de prueba FastAPI  
- Mockear dependencias externas  
- No usar datos reales  

### **Paso 3 — Diseñar casos de prueba**
Cada funcionalidad debe tener:

- Caso exitoso  
- Caso con datos inválidos  
- Caso con permisos insuficientes  
- Caso multi‑tenant  
- Caso de flujo documental (si aplica)  

### **Paso 4 — Implementar pruebas unitarias**
- Testear servicios y repositorios  
- Validar lógica de negocio  
- Validar restricciones  
- Validar integridad  

### **Paso 5 — Implementar pruebas de integración**
- Testear endpoints con cliente FastAPI  
- Validar JWT + RBAC  
- Validar multi‑tenant  
- Validar estados del flujo documental  

### **Paso 6 — Implementar pruebas de frontend (si aplica)**
- Testear funciones JS  
- Testear integración con API (mock fetch)  
- Testear validaciones de formularios  

### **Paso 7 — Validar resultados**
- Revisar códigos HTTP  
- Revisar payloads  
- Revisar errores esperados  
- Revisar que no existan regresiones  

### **Paso 8 — Generar el código final**
- Tests limpios, claros y reproducibles  
- Sin dependencias externas  
- Sin duplicaciones  
- Con nombres descriptivos  

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Tests que dependan de datos reales  
❌ Tests que modifiquen roles o estados  
❌ Tests que ignoren multi‑tenant  
❌ Tests que mezclen lógica de negocio  
❌ Tests que no validen errores  
❌ Tests que dependan del orden de ejecución  
❌ Tests que llamen a servicios externos reales  
❌ Tests que rompan la arquitectura  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿El test cubre caso exitoso?  
- [ ] ¿El test cubre caso inválido?  
- [ ] ¿El test cubre permisos insuficientes?  
- [ ] ¿El test valida multi‑tenant?  
- [ ] ¿El test respeta el flujo documental?  
- [ ] ¿El test usa fixtures correctamente?  
- [ ] ¿El test no inventa campos ni entidades?  
- [ ] ¿El código es claro y mantenible?  

---

## 8. Ejemplos de delegación correctos
- “Usá Testing‑QA‑Automation para crear tests del flujo de aprobación de Habilitaciones.”  
- “Validá que un rol EMPRESA no pueda acceder a Documentos de otra empresa.”  
- “Creá tests para el endpoint de Personas usando Testing‑QA‑Automation.”  
- “Agregá tests de integración para Documentos con JWT y RBAC.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Crear tests unitarios  
- Crear tests de integración  
- Validar roles y permisos  
- Validar multi‑tenant  
- Validar flujo documental  
- Detectar errores y regresiones  
- Documentar casos de prueba  

Este skill **NO puede**:

- Cambiar roles o estados  
- Alterar arquitectura  
- Inventar entidades o campos  
- Modificar lógica de negocio  
- Crear datos reales en producción  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **QA Engineer senior**, asegurando que SGH‑V1 sea estable, seguro y consistente, sin bloquear el desarrollo y respetando todas las reglas del proyecto.





