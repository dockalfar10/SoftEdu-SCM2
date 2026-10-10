# TRA-001 - Matriz de Trazabilidad de SoftEdu

## Información del elemento de configuración
- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: SoftEdu
- Versión: 1.1
- Estado: Aprobado para BL-002
- Fecha: 10-10-2026
- Responsable: Equipo SoftEdu
- Responsable del cambio: Minerva2026410

## Historial de versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 09/09/2026 | Creación inicial de la matriz de trazabilidad | Equipo SoftEdu |
| `1.1` | 10-10-2026 | Actualización y cierre de la trazabilidad asociada a CR-001 y aprobación para BL-002 | Minerva2026410 |

## 1. Objetivo
Relacionar los requisitos definidos para SoftEdu con los elementos de diseño, código fuente y pruebas que los implementan o verifican.  
La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado y registrar la trazabilidad de las solicitudes de cambio.

## 2. Matriz de trazabilidad
| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF-01** | Registrar estudiante | DIS-001 v1.1 - Entidad Estudiante | SRC-001 v1.1 - Gestión de Estudiantes | TST-001 v1.1 / CP-01 | Completa |
| **RF-02** | Consultar estudiante | DIS-001 - Entidad Estudiante | SRC-001 - Gestión de Estudiantes | TST-001 / CP-02 | Completa |
| **RF-03** | Registrar curso | DIS-001 - Entidad Curso | Pendiente de implementación | TST-001 / CP-03 | Parcial |
| **RF-04** | Matricular estudiante | DIS-001 - Entidad Matrícula | Pendiente de implementación | TST-001 / CP-04 | Parcial |

## 3. Relación entre elementos de configuración afectados por CR-001
CR-001 - Agregar teléfono al estudiante  
↓  
REQ-001 v1.1 - RF-01 Registrar estudiante  
↓  
DIS-001 v1.1 - Entidad Estudiante  
↓  
SRC-001 v1.1 - Gestión de Estudiantes  
↓  
TST-001 v1.1 - CP-01 Registrar estudiante correctamente  
↓  
TRA-001 v1.1 - Actualización y cierre de la trazabilidad

## 4. Trazabilidad por requisito

### RF-01 - Registrar estudiante
- **Requisito:** REQ-001 v1.1
- **Cambio asociado:** CR-001 - Agregar teléfono al estudiante
- **Diseño asociado:** DIS-001 v1.1 - Entidad Estudiante
- **Código asociado:** SRC-001 v1.1 - Gestión de Estudiantes
- **Caso de prueba asociado:** TST-001 v1.1 / CP-01 (Ejecutado y Exitoso)
- **Estado de trazabilidad:** Completa
- **Estado del cambio:** Aprobado e integrado a `main` (BL-002)

### RF-02 - Consultar estudiante
- **Requisito:** REQ-001
- **Diseño asociado:** DIS-001 - Entidad Estudiante
- **Código asociado:** SRC-001 - Gestión de Estudiantes
- **Caso de prueba asociado:** TST-001 / CP-02
- **Estado de trazabilidad:** Completa

### RF-03 - Registrar curso
- **Requisito:** REQ-001
- **Diseño asociado:** DIS-001 - Entidad Curso
- **Código asociado:** Pendiente
- **Caso de prueba asociado:** TST-001 / CP-03
- **Estado de trazabilidad:** Parcial

### RF-04 - Matricular estudiante
- **Requisito:** REQ-001
- **Diseño asociado:** DIS-001 - Entidad Matrícula
- **Código asociado:** Pendiente
- **Caso de prueba asociado:** TST-001 / CP-04
- **Estado de trazabilidad:** Parcial

## 5. Trazabilidad de cambios
Solicitud de cambio CR-001  
↓  
RF-01 de REQ-001 v1.1  
↓  
DIS-001 v1.1  
↓  
SRC-001 v1.1  
↓  
TST-001 v1.1 / CP-01  
↓  
Pull Request aprobado y fusionado (Merge)  
↓  
Establecimiento de la segunda línea base (BL-002 / v1.1)

## 6. Registro de cambios trazables
| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *Línea base inicial* | Sin cambios aprobados en la versión 1.0 | DIS-001 v1.0 | SRC-001 v1.0 | TST-001 v1.0 | v1.0 (Tag) | Aprobado (BL-001) |
| **CR-001** - Agregar teléfono al estudiante | REQ-001 v1.1 / RF-01 | DIS-001 v1.1 | SRC-001 v1.1 | TST-001 v1.1 / CP-01 | PR / Merge a main | Aprobado (BL-002) |

## 7. Observaciones
Este documento constituye el Elemento de Configuración TRA-001.  
La versión 1.0 representa la trazabilidad correspondiente a la configuración inicial establecida en BL-001.  
La versión 1.1 registra de forma definitiva el impacto, las relaciones y el cierre formal de la solicitud de cambio CR-001, respaldando la integración oficial bajo la segunda línea base del proyecto (**BL-002** / tag **v1.1**).