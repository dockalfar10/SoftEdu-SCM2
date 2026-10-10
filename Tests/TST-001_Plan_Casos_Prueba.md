# TST-001 - Plan y Casos de Prueba de SoftEdu

## Información del elemento de configuración
- Código del CI: TST-001
- Nombre: Plan y Casos de Prueba
- Proyecto: SoftEdu
- Versión: 1.1
- Estado: En modificación por CR-001
- Fecha: 16/09/2026
- Responsable: Equipo SoftEdu
- Responsable del cambio: Minerva2026410

## Historial de versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 09/09/2026 | Creación inicial del plan y casos de prueba | Equipo SoftEdu[cite: 38, 39] |
| `1.1` | 16/09/2026 | Se actualiza CP-01 para validar el atributo teléfono según CR-001 | Minerva2026410[cite: 39] |

## 1. Objetivo
Validar que las funcionalidades principales de SoftEdu cumplan con los requisitos definidos en REQ-001 versión 1.1[cite: 39].

## 2. Alcance de las pruebas
Las pruebas cubren:
- Registro de estudiantes.
- Consulta de estudiantes.
- Registro de cursos.
- Matrícula de estudiantes[cite: 39].

## 3. Casos de prueba

### CP-01 - Registrar estudiante correctamente
- **Requisito asociado:** RF-01[cite: 39]
- **Diseño asociado:** DIS-001 - Entidad Estudiante[cite: 39]
- **Código asociado:** SRC-001[cite: 39]
- **Precondición:** El estudiante no debe existir previamente[cite: 39].

**Datos de entrada:**
- Identificación: 1001
- Nombre completo: Ana Pérez
- Correo electrónico: ana@email.com
- Teléfono: 3001234567[cite: 22, 39]

**Resultado esperado:**
El sistema crea correctamente el estudiante y almacena identificación, nombre completo, correo electrónico y teléfono[cite: 39].

**Estado de la prueba:** Pendiente de ejecución[cite: 22, 39].

### CP-02 - Consultar estudiante existente
- Requisito asociado: RF-02[cite: 39]
- Diseño asociado: DIS-001 - Entidad Estudiante[cite: 39]
- Código asociado: SRC-001[cite: 39]
- Precondición: El estudiante debe estar registrado[cite: 39].

**Resultado esperado:**
El sistema muestra correctamente los datos del estudiante consultado[cite: 39].

**Estado:** Aprobado en la línea base v1.0; sin cambios por CR-001[cite: 39].

### CP-03 - Registrar curso
- Requisito asociado: RF-03[cite: 39]
- Diseño asociado: DIS-001 - Entidad Curso[cite: 39]

**Datos de entrada:**
- Código: IS101
- Nombre: Introducción a Sistemas
- Créditos: 3[cite: 39, 40]

**Resultado esperado:**
El curso queda registrado correctamente[cite: 40].

**Estado:** Aprobado en la línea base v1.0; sin cambios por CR-001.

### CP-04 - Matricular estudiante
- Requisito asociado: RF-04[cite: 40]
- Diseño asociado: DIS-001 - Entidad Matrícula[cite: 40]

**Precondiciones:**
- El estudiante debe existir.
- El curso debe existir[cite: 40].

**Resultado esperado:**
El estudiante queda asociado correctamente al curso seleccionado[cite: 40].

**Estado:** Aprobado en la línea base v1.0; sin cambios por CR-001.

## 4. Trazabilidad de pruebas
| Caso de prueba | Requisito | Diseño | Código |
| :--- | :--- | :--- | :--- |
| CP-01 | RF-01 | DIS-001 v1.1[cite: 40] | SRC-001 v1.1[cite: 40] |
| CP-02 | RF-02 | DIS-001[cite: 40] | SRC-001[cite: 40] |
| CP-03 | RF-03 | DIS-001[cite: 40] | No aplica en esta versión[cite: 40] |
| CP-04 | RF-04 | DIS-001[cite: 40] | No aplica en esta versión[cite: 40] |

## 5. Observaciones de configuración
Este documento constituye el Elemento de Configuración TST-001[cite: 40].  
La versión 1.1 de TST-001 se actualiza como consecuencia de la solicitud de cambio CR-001 - Agregar teléfono al estudiante, con el propósito de validar el cambio incorporado en REQ-001 v1.1, DIS-001 v1.1 y SRC-001 v1.1[cite: 40].  
Los casos de prueba deberán actualizarse cuando una solicitud de cambio modifique los requisitos, el diseño o el código relacionado[cite: 40].