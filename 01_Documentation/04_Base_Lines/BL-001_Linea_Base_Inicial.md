# BL-001 - Línea Base Inicial (Baseline 1.0)

## 1. Identificación del Elemento de Configuración (CI)
* **Código del CI:** BL-001
* **Proyecto:** SoftEdu-SCM
* **Versión de la Línea Base:** 1.0
* **Estado:** Aprobado y Congelado (Línea Base Oficial)
* **Fecha:** 10-10-2026
* **Responsable:** OWNER

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 10-10-2026 | Establecimiento formal de la Línea Base Inicial (BL-001) congelando los CIs aprobados. | OWNER |

---

## 3. Propósito y Alcance
* **Propósito:** Consolidar y congelar un conjunto de versiones estables y coherentes de los Elementos de Configuración (CIs) del sistema SoftEdu-SCM para que sirvan como punto de referencia oficial para el desarrollo posterior.
* **Alcance:** Incluye la especificación de requisitos, diseño de sistema, código fuente, casos de prueba y matriz de trazabilidad correspondientes a la versión 1.0.

---

## 4. Elementos de Configuración (CIs) Incluidos en la Línea Base
La siguiente tabla detalla el estado actual y versión de cada CI que conforma oficialmente esta línea base:

| Código de CI | Nombre del Elemento / Artefacto | Versión | Estado Aprobado | Ruta en el Repositorio |
| :--- | :--- | :--- | :--- | :--- |
| **REQ-001** | Especificación de Requisitos | `1.0` | Aprobado / Línea Base | `REQ-001.md` (o raíz) |
| **DIS-001** | Diseño del Sistema | `1.0` | Aprobado / Línea Base | `01_Documentacion/02_Diseno/DIS-001_Diseno_Sistema.md` |
| **SRC-001** | Código Fuente (Gestión) | `1.0` | Aprobado / Línea Base | `02_Codigo_Fuente/SRC-001_Gestion_Estudiantes.py` |
| **TST-001** | Plan y Casos de Prueba | `1.0` | Aprobado / Línea Base | `03_Pruebas/TST-001_Plan_Casos_Prueba.md` |
| **TRA-001** | Matriz de Trazabilidad | `1.0` | Aprobado / Línea Base | `01_Documentacion/03_Trazabilidad/TRA-001_Matriz_Trazabilidad.md` |

---

## 5. Política de Control de Cambios Posterior
> **Observación Obligatoria de SCM:** Al quedar establecida esta Línea Base (`BL-001`), **cualquier modificación, corrección o nuevo requerimiento posterior queda estrictamente prohibido de forma directa**. Todo cambio futuro sobre estos componentes requerirá obligatoriamente:
> 1. La emisión formal de una Solicitud de Cambio (CR).
> 2. La evaluación de impacto sobre los demás CIs vinculados.
> 3. La aprobación formal del comité o responsable antes de modificar el código o la documentación.