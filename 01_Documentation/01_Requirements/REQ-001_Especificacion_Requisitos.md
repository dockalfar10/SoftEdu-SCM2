# REQ-001 - Especificación de Requisitos

## 1. Identificación del Elemento de Configuración (CI)
* **Código del CI:** REQ-001
* **Proyecto:** SoftEdu-SCM
* **Versión:** 1.0
* **Estado:** Aprobado para línea base inicial
* **Fecha:** 09-10-2026
* **Responsable:** OWNER

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 09-10-2026 | Creación inicial del requerimiento y establecimiento de línea base. | OWNER |

---

## 3. Propósito y Alcance
* **Propósito:** Establecer los cimientos funcionales y de seguridad para la gestión de proyectos dentro de la plataforma SoftEdu-SCM, permitiendo un control centralizado de su información principal.
* **Alcance:** Aplica al módulo core de administración de proyectos del sistema SoftEdu-SCM, abarcando las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de proyectos y la protección de sus datos frente a accesos no autorizados.

---

## 4. Requisitos Funcionales y No Funcionales

### Requisitos Funcionales
* **RF-01 - Gestión de la información principal del proyecto**
  * **Descripción:** El sistema deberá permitir registrar, consultar, actualizar y eliminar la información principal del proyecto, incluyendo código, nombre, descripción, responsable, fechas relevantes y estado actual.
  * **Criterios de aceptación:**
    * El sistema debe mantener un registro único para cada proyecto.
    * La información del proyecto debe poder visualizarse y editarse desde una interfaz de gestión.
    * Los campos obligatorios deben validarse antes de guardar la información.
    * El sistema debe permitir identificar claramente el responsable y el estado del proyecto en cualquier momento.

### Requisitos No Funcionales
* **RNF-01 - Seguridad y confidencialidad de la información**
  * **Descripción:** El sistema deberá proteger la información del proyecto mediante mecanismos de autenticación, autorización y control de accesos, garantizando la confidencialidad, integridad y disponibilidad de los datos durante la operación normal del sistema.
  * **Criterios de aceptación:**
    * Acceso restringido exclusivamente a usuarios autenticados con roles autorizados.
    * Integridad de los datos asegurada ante transacciones concurrentes.

---

## 5. Control de Cambios y Línea Base
> **Observación de Gestión de Configuración:** Cualquier cambio, modificación o actualización realizado en este documento o en el código asociado **posterior a esta línea base** deberá ser estrictamente controlado y registrado mediante el procedimiento formal de Gestión de Cambios de SoftEdu-SCM.