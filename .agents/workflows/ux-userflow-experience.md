---
description: Analizar, mejorar y optimizar la experiencia del usuario, flujos de interacción y claridad operativa
---

name: ux-userflow-experience
description: Skill avanzado para analizar, mejorar y optimizar la experiencia del usuario, flujos de interacción y claridad operativa en SGH‑V1, respetando el Prompt Maestro y la arquitectura oficial.
---

# UX‑UserFlow‑Experience  
Skill profesional para experiencia de usuario en SGH‑V1  
Versión: Avanzada pero flexible

---

## 1. Propósito del skill
Este skill guía al agente para trabajar en la **experiencia de usuario (UX)** de SGH‑V1, garantizando:

- Flujos claros y fáciles de entender  
- Interacciones simples y eficientes  
- Formularios intuitivos  
- Tablas legibles y navegables  
- Mensajes de error comprensibles  
- Acciones visibles según rol  
- Reducción de fricción en tareas frecuentes  
- Coherencia visual y funcional  
- Respeto por el flujo documental y multi‑tenant  

El objetivo es **mejorar la usabilidad sin alterar la arquitectura**, manteniendo HTML + Bootstrap + JS modular.

---

## 2. Cuándo debe activarse este skill
Usar este skill cuando la tarea implique:

- Mejorar pantallas existentes  
- Rediseñar flujos de interacción  
- Simplificar formularios  
- Mejorar tablas, filtros o paginación  
- Optimizar mensajes de error o confirmación  
- Revisar accesibilidad o claridad visual  
- Detectar fricciones en el uso diario  
- Alinear la UI con roles y permisos  
- Preparar pantallas para dashboards o analítica  
- Revisar la experiencia completa de un módulo  

---

## 3. Reglas clave del proyecto (Prompt Maestro)
El agente debe respetar SIEMPRE:

- **No usar frameworks SPA**  
- **No modificar roles ni estados**  
- **No alterar el flujo documental**  
- **No inventar campos ni entidades**  
- **No romper el aislamiento multi‑tenant**  
- **No cambiar arquitectura**  
- **No introducir librerías externas no autorizadas**  
- **Usar Bootstrap + JS modular**  

---

## 4. Principios de UX obligatorios en SGH‑V1
El agente debe aplicar:

### **Claridad**
- Cada pantalla debe tener un propósito evidente  
- Los botones deben indicar claramente su acción  
- Los estados del flujo documental deben ser visibles  

### **Consistencia**
- Mismos estilos, colores y patrones en todas las pantallas  
- Mismos nombres para acciones similares  
- Mismo orden de campos en formularios similares  

### **Eficiencia**
- Minimizar clics innecesarios  
- Formularios cortos y directos  
- Tablas con filtros útiles  

### **Accesibilidad**
- Contraste adecuado  
- Tamaños de fuente legibles  
- Botones accesibles en dispositivos móviles  

### **Seguridad**
- Mostrar solo acciones permitidas por rol  
- No mostrar datos de otras empresas  

---

## 5. Pasos que debe seguir el agente (flujo profesional)
### **Paso 1 — Analizar la pantalla o flujo**
- Identificar el objetivo del usuario  
- Identificar el rol que la usa  
- Identificar el estado del flujo documental  
- Identificar puntos de fricción  

### **Paso 2 — Evaluar estructura visual**
- Revisar uso de Bootstrap  
- Revisar jerarquía visual (títulos, secciones, cards)  
- Revisar legibilidad de tablas y formularios  

### **Paso 3 — Evaluar interacción**
- Revisar botones, acciones y eventos  
- Revisar validaciones de formularios  
- Revisar mensajes de error y éxito  
- Revisar tiempos de respuesta y feedback visual  

### **Paso 4 — Revisar roles y permisos**
- Mostrar solo acciones permitidas  
- Ocultar botones no autorizados  
- Evitar confusión entre roles  

### **Paso 5 — Revisar multi‑tenant**
- Validar que la UI no permita seleccionar empresas ajenas  
- Validar que no se muestren datos cruzados  

### **Paso 6 — Proponer mejoras**
- Simplificar pasos  
- Reorganizar elementos  
- Mejorar textos y etiquetas  
- Agregar feedback visual (spinners, alerts, badges)  
- Mejorar accesibilidad  

### **Paso 7 — Generar el código final**
- HTML limpio y ordenado  
- Bootstrap bien aplicado  
- JS modular y claro  
- Mensajes claros y útiles  

---

## 6. Anti‑patrones prohibidos
El agente debe evitar:

❌ Formularios largos sin necesidad  
❌ Botones ambiguos (“Aceptar”, “Procesar”, “Enviar”)  
❌ Tablas sin filtros o sin paginación  
❌ Mensajes de error técnicos o confusos  
❌ Mostrar acciones no permitidas por rol  
❌ Mostrar datos de otras empresas  
❌ Usar colores no estándar o inconsistentes  
❌ Crear pantallas que rompan el flujo documental  
❌ Usar frameworks SPA o librerías externas  

---

## 7. Checklist rápido antes de generar código
- [ ] ¿La pantalla es clara y fácil de entender?  
- [ ] ¿Los botones indican claramente su acción?  
- [ ] ¿Los formularios son simples y directos?  
- [ ] ¿Las tablas tienen filtros útiles?  
- [ ] ¿Los mensajes de error son comprensibles?  
- [ ] ¿Respeté roles y permisos?  
- [ ] ¿Respeté el flujo documental?  
- [ ] ¿No expongo datos de otras empresas?  
- [ ] ¿Usé Bootstrap correctamente?  
- [ ] ¿El JS es modular y mantenible?  

---

## 8. Ejemplos de delegación correctos
- “Usá UX‑UserFlow‑Experience para mejorar la pantalla de Documentos y hacer más claro el flujo de carga.”  
- “Simplificá el formulario de Personas usando UX‑UserFlow‑Experience.”  
- “Revisá la tabla de Habilitaciones y agregá filtros útiles.”  
- “Mejorá los mensajes de error del login usando UX‑UserFlow‑Experience.”  
- “Asegurá que las acciones visibles dependan del rol actual.”  

---

## 9. Alcance permitido
Este skill **puede**:

- Mejorar pantallas  
- Optimizar flujos  
- Simplificar formularios  
- Mejorar tablas y filtros  
- Mejorar mensajes y feedback  
- Alinear UI con roles y permisos  
- Detectar fricciones y proponer mejoras  
- Documentar decisiones de UX  

Este skill **NO puede**:

- Cambiar arquitectura  
- Introducir frameworks SPA  
- Modificar roles o estados  
- Alterar el flujo documental  
- Inventar campos o entidades  
- Exponer datos de otras empresas  

---

## 10. Cierre
Este skill permite que el agente trabaje como un **especialista senior en UX**, mejorando la experiencia del usuario sin romper la arquitectura SGH‑V1, manteniendo claridad, eficiencia y seguridad en todas las pantallas.

