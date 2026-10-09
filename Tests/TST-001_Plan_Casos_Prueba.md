# TST-001 - Plan y Casos de Prueba

## 1. Identificación del Elemento de Configuración (CI)
* **Código del CI:** TST-001
* **Proyecto:** SoftEdu-SCM
* **Versión:** 1.0
* **Estado:** Borrador / En revisión
* **Fecha:** 10-10-2026
* **Responsable:** OWNER

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 10-10-2026 | Creación inicial del plan y casos de prueba para validación de la v1.0. | OWNER |

---

## 3. Propósito y Alcance
* **Propósito:** Definir el plan de pruebas y los casos de prueba formales para verificar que el módulo implementado cumple de forma correcta y robusta con los requerimientos funcionales y no funcionales especificados en el `REQ-001` y soportados por el código `SRC-001`.
* **Alcance:** Abarca las pruebas unitarias y funcionales sobre las operaciones CRUD de la clase `GestionProyectoEstudiante` implementada en el código fuente.

---

## 4. Trazabilidad con Requisitos y Artefactos
| Código de Requisito | Artefacto de Diseño Asociado | Artefacto de Código Fuente | Caso de Prueba Asociado |
| :--- | :--- | :--- | :--- |
| **REQ-001** | `DIS-001` (Entidad Proyecto) | `SRC-001_Gestion_Estudiantes.py` | **CP-001**, **CP-002**, **CP-003** |

---

## 5. Casos de Prueba

### Caso de Prueba 01: Creación Exitosa de Proyecto
* **ID:** CP-001
* **Requisito asociado:** REQ-001
* **Descripción:** Verificar que el sistema permita registrar un proyecto correctamente cuando se proporcionan todos los campos obligatorios.
* **Precondiciones:** La clase `GestionProyectoEstudiante` está instanciada y sin registros previos.
* **Pasos de prueba:**
  1. Invocar el método `crear_registro` enviando: `codigo="PROJ-001"`, `nombre="Plataforma Educativa"`, `descripcion="Core de gestión"`, `responsable="OWNER"`, `estado="Activo"`.
  2. Consultar el listado mediante `consultar_registros`.
* **Resultado esperado:** 
  - El método retorna un mensaje de éxito ("Registro 'Plataforma Educativa' creado exitosamente.").
  - El listado contiene exactamente 1 elemento con los datos proporcionados.
* **Estado:** [Pendiente / Aprobado]

---

### Caso de Prueba 02: Validación de Campos Obligatorios
* **ID:** CP-002
* **Requisito asociado:** REQ-001
* **Descripción:** Verificar que el sistema rechace el registro e interrumpa la ejecución si faltan campos obligatorios (como el código, nombre o responsable).
* **Precondiciones:** La clase `GestionProyectoEstudiante` está instanciada.
* **Pasos de prueba:**
  1. Invocar el método `crear_registro` dejando el parámetro `codigo=""` (vacío) u omitiendo el nombre/responsable.
* **Resultado esperado:** 
  - El sistema lanza una excepción del tipo `ValueError` indicando que los campos obligatorios no pueden estar vacíos.
* **Estado:** [Pendiente / Aprobado]

---

### Caso de Prueba 03: Actualización y Consulta de Registros
* **ID:** CP-003
* **Requisito asociado:** REQ-001
* **Descripción:** Validar que un proyecto existente pueda ser consultado y actualizado de manera correcta.
* **Precondiciones:** Existe un registro previo con `codigo="PROJ-001"`.
* **Pasos de prueba:**
  1. Invocar `actualizar_registro(codigo="PROJ-001", nuevos_datos={"estado": "Finalizado"})`.
  2. Consultar los registros con `consultar_registros()`.
* **Resultado esperado:**
  - El mensaje de actualización es exitoso.
  - Al consultar el registro, el campo `estado` muestra el valor actualizado ("Finalizado").
* **Estado:** [Pendiente / Aprobado]

---

## 6. Control de Cambios y Línea Base
> **Observación de Gestión de Configuración:** Cualquier modificación en los casos de prueba o en los criterios de aceptación **posterior a la línea base** deberá registrarse bajo el procedimiento de control de cambios de SoftEdu-SCM.