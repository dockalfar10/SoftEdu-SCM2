# DIS-001 - Diseño del Sistema

## 1. Identificación del Elemento de Configuración (CI)
* **Código del CI:** DIS-001
* **Proyecto:** SoftEdu-SCM
* **Versión:** 1.0
* **Estado:** Borrador / En revisión
* **Fecha:** 09-10-2026
* **Responsable:** OWNER

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 09-10-2026 | Creación inicial del diseño del sistema. | OWNER |

---

## 3. Propósito y Alcance
* **Propósito:** Definir la arquitectura de datos, los componentes principales, los flujos de interacción y la trazabilidad con los requisitos funcionales del sistema SoftEdu-SCM.
* **Alcance:** Abarca el diseño lógico del módulo central de gestión de proyectos, especificando entidades de base de datos y flujos operacionales principales.

---

## 4. Trazabilidad con Requisitos
| Código de Requisito (REQ) | Componente / Módulo de Diseño Asociado | Descripción de la Relación |
| :--- | :--- | :--- |
| **REQ-001** | Módulo de Proyectos / Entidad `Proyecto` | El diseño de la base de datos y la interfaz de gestión implementan directamente las operaciones CRUD definidas en el REQ-001. |

---

## 5. Diseño de Entidades y Atributos

### Entidad: `Proyecto`
Representa la información principal de cada proyecto registrado en la plataforma.

| Atributo | Tipo de Dato | Restricciones / Clave | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | UUID / INT | PK, Not Null | Identificador único del proyecto. |
| `codigo` | VARCHAR(50) | Unique, Not Null | Código alfanumérico de identificación interna del proyecto. |
| `nombre` | VARCHAR(150) | Not Null | Nombre descriptivo del proyecto. |
| `descripcion` | TEXT | Nullable | Resumen detallado del propósito del proyecto. |
| `responsable` | VARCHAR(100) | Not Null | Nombre o ID del usuario a cargo del proyecto. |
| `estado` | VARCHAR(30) | Not Null (Ej: Activo, Pausado, Finalizado) | Estado actual en el ciclo de vida del proyecto. |
| `fecha_inicio` | DATE | Not Null | Fecha de inicio planificada. |
| `fecha_fin` | DATE | Nullable | Fecha estimada o real de finalización. |
| `created_at` | TIMESTAMP | Default CURRENT_TIMESTAMP | Fecha de creación del registro. |
| `updated_at` | TIMESTAMP | Default CURRENT_TIMESTAMP | Fecha de última modificación. |

---

## 6. Flujos del Sistema y Diagrama Lógico

### Flujo Principal: Gestión y Registro de Proyectos
1. **Inicio:** El usuario administrador accede a la sección de proyectos en la interfaz de gestión.
2. **Validación de Identidad:** El sistema valida los permisos y roles del usuario autenticado (relacionado con el cumplimiento de seguridad).
3. **Operación CRUD:**
   * *Crear/Actualizar:* El usuario ingresa los datos requeridos. El sistema valida que los campos obligatorios no estén vacíos antes de enviarlos a la capa de persistencia.
   * *Consultar/Eliminar:* El sistema busca o da de baja el registro único correspondiente en la entidad `Proyecto`.
4. **Cierre:** El sistema confirma la transacción con un mensaje de éxito o alerta de error en caso de fallo en las validaciones.

---

## 7. Control de Cambios y Línea Base
> **Observación de Gestión de Configuración:** Cualquier modificación arquitectónica o estructural sobre este diseño **posterior al establecimiento de la línea base** deberá gestionarse formalmente mediante el proceso de control de cambios de SoftEdu-SCM.