# BL-002 - Segunda línea base de SoftEdu

## 1. Identificación del Elemento de Configuración (CI)
* **Código del CI:** BL-002
* **Proyecto:** SoftEdu-SCM
* **Versión del producto:** 1.1
* **Cambio incorporado:** CR-001 - Agregar teléfono al estudiante[cite: 44]
* **Estado:** Aprobada[cite: 44]
* **Fecha:** 10-10-2026
* **Responsable:** Equipo SoftEdu / Minerva2026410

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.1` | 10-10-2026 | Establecimiento formal de la segunda línea base (BL-002) tras integrar CR-001. | Equipo SoftEdu |

---

## 3. Propósito y Alcance
* **Propósito:** Consolidar y congelar la segunda línea base oficial del proyecto SoftEdu-SCM, incorporando formalmente los cambios de la solicitud `CR-001` (adición del atributo teléfono al estudiante).
* **Alcance:** Incluye la versión actualizada de todos los elementos de configuración que conforman el sistema en su versión 1.1.

---

## 4. Elementos de Configuración (CIs) Incluidos en la Línea Base BL-002
La siguiente tabla detalla el conjunto concreto de versiones aprobadas que integran esta línea base:

| Código de CI | Nombre del Elemento / Artefacto | Versión | Estado Aprobado | Ruta en el Repositorio |
| :--- | :--- | :--- | :--- | :--- |
| **REQ-001** | Especificación de Requisitos | `1.1` | Aprobado / Línea Base BL-002 | `01_Documentacion/01_Requisitos/REQ-001_Especificacion_Requisitos.md` |
| **DIS-001** | Diseño del Sistema | `1.1` | Aprobado / Línea Base BL-002 | `01_Documentacion/02_Diseno/DIS-001_Diseno_Sistema.md` |
| **SRC-001** | Código Fuente (Gestión) | `1.1` | Aprobado / Línea Base BL-002 | `02_Codigo_Fuente/SRC-001_Gestion_Estudiantes.py` |
| **TST-001** | Plan y Casos de Prueba | `1.1` | Aprobado / Línea Base BL-002 | `03_Pruebas/TST-001_Plan_Casos_Prueba.md` |
| **TRA-001** | Matriz de Trazabilidad | `1.1` | Aprobado / Línea Base BL-002 | `01_Documentacion/03_Trazabilidad/TRA-001_Matriz_Trazabilidad.md` |

---

## 5. Evidencia de Aprobación
* **Mecanismo:** Pull Request de cierre aprobado e integrado (`Merge`) en la rama principal `main` con cierre automático del Issue vinculado (`CR-001`)[cite: 44].
* **Verificación:** Todos los casos de prueba asociados (`CP-01`) fueron ejecutados y validados de manera exitosa.