# TRA-001 - Matriz de Trazabilidad

## 1. Identificación del Elemento de Configuración (CI)
* **Código del CI:** TRA-001
* **Proyecto:** SoftEdu-SCM
* **Versión:** 1.0
* **Estado:** Borrador / En revisión
* **Fecha:** 10-10-2026
* **Responsable:** OWNER

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 10-10-2026 | Creación inicial de la matriz de trazabilidad para la versión 1.0. | OWNER |

---

## 3. Propósito y Alcance
* **Propósito:** Vincular de forma bidireccional los diferentes artefactos del ciclo de vida del software (Requisitos, Diseño, Código Fuente y Pruebas) para garantizar la coherencia y permitir un análisis de impacto preciso ante futuras modificaciones.
* **Alcance:** Cubre los elementos de configuración iniciales definidos para la versión 1.0 del sistema SoftEdu-SCM (enfocados en la gestión de proyectos/entidades core).

---

## 4. Matriz de Relación (Requisitos vs Artefactos)
La siguiente tabla asocia cada requisito con su respectivo diseño, código fuente y casos de prueba correspondientes:

| Requisito (REQ) | Diseño Asociado (DIS) | Código Fuente (SRC) | Casos de Prueba (TST) | Estado de Trazabilidad |
| :--- | :--- | :--- | :--- | :--- |
| **REQ-001** (Gestión de la información principal del proyecto) | `DIS-001` (Entidad Proyecto y flujos CRUD) | `SRC-001_Gestion_Estudiantes.py` | `CP-001`, `CP-002`, `CP-003` | **Completa** |

> **Nota sobre el estado:** La trazabilidad se considera **Completa** debido a que cada requisito funcional y no funcional cuenta con un diseño lógico, una implementación en código fuente y casos de prueba explícitos que lo validan.

---

## 5. Análisis de Impacto por Cambios
Esta sección responde a la pregunta clave: *Si un elemento base sufre modificaciones, ¿qué otros componentes deben revisarse y actualizarse?*

* **Escenario 1: Si cambia el Requisito (ej. REQ-001)**
  * *Componentes afectados a revisar:* 
    1. **Diseño (`DIS-001`):** Se deben actualizar las entidades, atributos y diagramas de flujo para reflejar los nuevos requerimientos.
    2. **Código Fuente (`SRC-001`):** Se debe modificar la clase lógica y los métodos de validación/CRUD.
    3. **Pruebas (`TST-001`):** Se deben actualizar o añadir nuevos casos de prueba para cubrir los cambios introducidos.

* **Escenario 2: Si cambia el Diseño (ej. `DIS-001`)**
  * *Componentes afectados a revisar:*
    1. **Código Fuente (`SRC-001`):** Ajustar la estructura de clases/datos según la nueva especificación de diseño.
    2. **Pruebas (`TST-001`):** Verificar si los pasos o resultados esperados de los casos de prueba se ven alterados.

---

## 6. Trazabilidad de Cambios (Futuras Solicitudes)
*Esta sección se mantendrá en blanco en la versión 1.0 y se llenará conforme surjan solicitudes de cambio (Change Requests - CR) en versiones posteriores.*

| ID Solicitud de Cambio (CR) | Requisito Afectado | Artefactos Modificados (DIS / SRC / TST) | Versión Resultante |
| :--- | :--- | :--- | :--- |
| *Ninguna registrada* | *N/A* | *N/A* | `v1.0` (Línea base inicial) |

---

## 7. Control de Cambios y Línea Base
> **Observación de Gestión de Configuración:** Cualquier modificación en la estructura de relaciones de esta matriz **posterior a la línea base** deberá gestionarse formalmente mediante el procedimiento de control de cambios de SoftEdu-SCM.