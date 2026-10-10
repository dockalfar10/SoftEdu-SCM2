# TRA-001 - Matriz de Trazabilidad de SoftEdu

## Información del elemento de configuración
- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: SoftEdu
- Versión: 1.1
- Estado: En modificación por CR-001
- Fecha: 16/09/2026
- Responsable: Equipo SoftEdu
- Responsable del cambio: Minerva2026410

## Historial de versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 09/09/2026 | Creación inicial de la matriz de trazabilidad | Equipo SoftEdu[cite: 40, 41] |
| `1.1` | 16/09/2026 | Actualización de la trazabilidad asociada a CR-001 - Agregar teléfono al estudiante | Minerva2026410[cite: 41] |

## 1. Objetivo
Relacionar los requisitos definidos para SoftEdu con los elementos de diseño, código fuente y pruebas que los implementan o verifican[cite: 41].  
La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado y registrar la trazabilidad de las solicitudes de cambio[cite: 41].

## 2. Matriz de trazabilidad
| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF-01** | Registrar estudiante | DIS-001 v1.1 - Entidad Estudiante[cite: 41] | SRC-001 v1.1 - Gestión de Estudiantes[cite: 41] | TST-001 v1.1 / CP-01[cite: 41] | Completa[cite: 41] |
| **RF-02** | Consultar estudiante | DIS-001 - Entidad Estudiante[cite: 41] | SRC-001 - Gestión de Estudiantes[cite: 41] | TST-001 / CP-02[cite: 41] | Completa[cite: 41] |
| **RF-03** | Registrar curso | DIS-001 - Entidad Curso[cite: 41] | Pendiente de implementación[cite: 41] | TST-001 / CP-03[cite: 41] | Parcial[cite: 41] |
| **RF-04** | Matricular estudiante | DIS-001 - Entidad Matrícula[cite: 42] | Pendiente de implementación[cite: 42] | TST-001 / CP-04[cite: 42] | Parcial[cite: 42] |

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
TRA-001 v1.1 - Actualización de la trazabilidad[cite: 41]

## 4. Trazabilidad por requisito

### RF-01 - Registrar estudiante
- **Requisito:** REQ-001 v1.1[cite: 41]
- **Cambio asociado:** CR-001 - Agregar teléfono al estudiante[cite: 41]
- **Diseño asociado:** DIS-001 v1.1 - Entidad Estudiante[cite: 41]
- **Código asociado:** SRC-001 v1.1 - Gestión de Estudiantes[cite: 41]
- **Caso de prueba asociado:** TST-001 v1.1 / CP-01[cite: 41]
- **Estado de trazabilidad:** Completa[cite: 41]
- **Estado del cambio:** En implementación, pendiente de revisión[cite: 42]

### RF-02 - Consultar estudiante
- **Requisito:** REQ-001[cite: 42]
- **Diseño asociado:** DIS-001 - Entidad Estudiante[cite: 42]
- **Código asociado:** SRC-001 - Gestión de Estudiantes[cite: 42]
- **Caso de prueba asociado:** TST-001 / CP-02[cite: 42]
- **Estado de trazabilidad:** Completa[cite: 42]

### RF-03 - Registrar curso
- **Requisito:** REQ-001[cite: 42]
- **Diseño asociado:** DIS-001 - Entidad Curso[cite: 42]
- **Código asociado:** Pendiente[cite: 42]
- **Caso de prueba asociado:** TST-001 / CP-03[cite: 42]
- **Estado de trazabilidad:** Parcial[cite: 42]

### RF-04 - Matricular estudiante
- **Requisito:** REQ-001[cite: 42]
- **Diseño asociado:** DIS-001 - Entidad Matrícula[cite: 42]
- **Código asociado:** Pendiente[cite: 42]
- **Caso de prueba asociado:** TST-001 / CP-04[cite: 42]
- **Estado de trazabilidad:** Parcial[cite: 42]

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
Commits asociados a CR-001  
↓  
Pull Request pendiente  
↓  
Revisión y decisión pendiente  
↓  
Nueva línea base, si el cambio es aprobado e integrado[cite: 42]

## 6. Registro de cambios trazables
| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| *Línea base inicial* | Sin cambios aprobados en la versión 1.0[cite: 42] | DIS-001 v1.0 | SRC-001 v1.0 | TST-001 v1.0 | v1.0 (Tag) | Aprobado |
| **CR-001** - Agregar teléfono al estudiante | REQ-001 v1.1 / RF-01[cite: 42] | DIS-001 v1.1[cite: 42] | SRC-001 v1.1[cite: 42] | TST-001 v1.1 / CP-01[cite: 42] | Commits realizados / PR pendiente[cite: 42] | En implementación[cite: 42] |

## 7. Observaciones
Este documento constituye el Elemento de Configuración TRA-001[cite: 42].  
La versión 1.0 representa la trazabilidad correspondiente a la configuración inicial de SoftEdu establecida en BL-001[cite: 42].  
La versión 1.1 registra el impacto y las relaciones generadas por la solicitud de cambio CR-001 - Agregar teléfono al estudiante[cite: 42, 43].  
CR-001 se encuentra aprobada para implementación, pero todavía está pendiente de revisión e integración en la rama principal[cite: 43].  
Una vez que el cambio sea revisado y aprobado mediante Pull Request, esta matriz deberá actualizar el estado de CR-001, registrar la referencia al Pull Request y reflejar la nueva línea base que se establezca[cite: 43].