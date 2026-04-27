---
description: 
---

---
name: security-rbac-jwt-multitenant
description: Skill avanzado para implementar, revisar y reforzar JWT, RBAC y aislamiento multi-tenant en SGH‑V1, respetando el Prompt Maestro y la arquitectura oficial.
---

# Security‑RBAC‑JWT‑Multitenant  
Skill profesional para seguridad en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en la **seguridad del backend de SGH‑V1**, garantizando:

- Autenticación robusta con JWT  
- Autorización basada en roles (RBAC)  
- Aislamiento multi‑tenant por empresa  
- Protección de endpoints  
- Validación de permisos según rol  
- Integridad del flujo documental  
- No exposición de datos entre empresas  

El objetivo es **asegurar el sistema sin bloquear el desarrollo**, manteniendo la arquitectura y las reglas del Prompt Maestro.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Crear o modificar dependencias de seguridad en FastAPI  
- Revisar o corregir validación de tokens JWT  
- Implementar o ajustar RBAC  
- Proteger endpoints existentes  
- Revisar filtrado por empresa  
- Validar que roles y permisos sean correctos  
- Revisar seguridad en routers, servicios o repositorios  
- Detectar vulnerabilidades o inconsistencias  
- Asegurar que el flujo documental no pueda ser manipulado  

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No modificar roles existentes**  
- **No inventar permisos nuevos**  
- **No alterar el flujo documental**  
- **No exponer datos de otras empresas**  
- **No cambiar la estructura del token JWT**  
- **No permitir accesos sin autenticación**  
- **No permitir accesos sin validar empresa**  
- **No mezclar lógica de seguridad con lógica de negocio**  

---

## 4. Estructura obligatoria de seguridad en SGH‑V1
El agente debe trabajar dentro de esta estructura:

backend/
└── app/
├── core/
│    ├── security.py
│    ├── auth.py
│    └── rbac.py
├── api/
│    └── routes/
└── domain/
└── <modulo>/
├── service.py
└── repository.py

---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Revisar el contexto de seguridad**
- Identificar roles involucrados  
- Identificar empresa del usuario  
- Identificar permisos requeridos  
- Identificar estado del flujo documental  

### **Paso 2 — Validar JWT**
- Verificar firma  
- Verificar expiración  
- Verificar payload  
- Verificar empresa asociada  
- Verificar roles del usuario  

### **Paso 3 — Aplicar RBAC**
- Validar que el rol tenga permiso para la acción  
- Validar que el rol pueda ver/editar el recurso  
- Validar que el rol pueda cambiar estados  

### **Paso 4 — Validar multi‑tenant**
- Filtrar SIEMPRE por empresa  
- Evitar acceso a IDs de otras empresas  
- Validar que los repositorios respeten el aislamiento  

### **Paso 5 — Proteger endpoints**
- Usar dependencias de seguridad  
- No permitir endpoints públicos salvo login  
- Validar permisos antes de ejecutar lógica  

### **Paso 6 — Revisar flujo documental**
- Validar que el usuario pueda cambiar el estado actual  
- Validar que el estado destino sea permitido  
- Evitar saltos ilegales en el flujo  

### **Paso 7 — Generar el código final**
- Código claro y modular  
- Dependencias bien definidas  
- Validaciones explícitas  
- Sin duplicaciones  

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Endpoints sin autenticación  
❌ Endpoints sin validación de rol  
❌ Consultas sin filtro por empresa  
❌ Permitir acceso a datos de otra empresa  
❌ Modificar roles o permisos  
❌ Alterar el flujo documental  
❌ Validar seguridad dentro del router con lógica improvisada  
❌ Crear tokens JWT con campos no autorizados  
❌ Permitir acciones administrativas a roles no autorizados  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿Validé JWT correctamente?  
- [ ] ¿Validé roles y permisos?  
- [ ] ¿Filtré por empresa?  
- [ ] ¿Respeté el flujo documental?  
- [ ] ¿El endpoint está protegido?  
- [ ] ¿No expongo datos de otras empresas?  
- [ ] ¿No modifiqué roles ni estados?  
- [ ] ¿El código es claro y modular?  

---

## 8. Ejemplos de delegación correctos
- “Usá Security‑RBAC‑JWT‑Multitenant para proteger los endpoints de Documentos y validar roles.”  
- “Revisá el filtrado por empresa en Habilitaciones usando Security‑RBAC‑JWT‑Multitenant.”  
- “Corregí la dependencia de seguridad para que valide correctamente el rol CONSULTORA.”  
- “Asegurá que el flujo documental no pueda saltarse estados usando Security‑RBAC‑JWT‑Multitenant.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Revisar y corregir seguridad  
- Proteger endpoints  
- Validar roles y permisos  
- Reforzar multi‑tenant  
- Mejorar dependencias de seguridad  
- Documentar decisiones  

Este skill **NO puede**:

- Crear roles nuevos  
- Cambiar estados del flujo documental  
- Alterar la arquitectura  
- Inventar campos en el JWT  
- Exponer datos de otras empresas  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **especialista senior en seguridad**, reforzando JWT, RBAC y multi‑tenant sin bloquear el desarrollo y manteniendo la integridad del sistema SGH‑V1.



