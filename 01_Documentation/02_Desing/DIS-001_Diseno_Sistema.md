# DIS-001 - Diseño del Sistema SoftEdu

## Información del elemento de configuración
- Código del CI: DIS-001
- Nombre: Diseño del Sistema
- Proyecto: SoftEdu
- Versión: 1.1
- Estado: En modificación por CR-001
- Fecha: 16/09/2026
- Responsable: Equipo SoftEdu
- Responsable del cambio: Minerva2026410

## Historial de versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :--- | :--- | :--- | :--- |
| `1.0` | 09/09/2026 | Diseño inicial del sistema | Equipo SoftEdu[cite: 36] |
| `1.1` | 16/09/2026 | Se agrega el atributo teléfono a la entidad Estudiante según CR-001 | Minerva2026410[cite: 36] |

## 1. Descripción general
SoftEdu se organiza en tres componentes principales:
1. Gestión de estudiantes.
2. Gestión de cursos.
3. Gestión de matrículas.[cite: 36]

## 2. Entidades principales

### Estudiante
La entidad Estudiante contiene los siguientes atributos:
- identificacion
- nombreCompleto
- correoElectronico
- telefono[cite: 36]

### Curso
La entidad Curso contiene:
- codigoCurso
- nombreCurso
- numeroCreditos[cite: 36, 37]

### Matricula
La entidad Matricula contiene:
- identificacionEstudiante
- codigoCurso
- fechaMatricula[cite: 37]

## 3. Relación entre requisitos y diseño
| Requisito | Elemento de diseño asociado |
| :--- | :--- |
| RF-01 Registrar estudiante | Entidad Estudiante (incluye atributo telefono)[cite: 37] |
| RF-02 Consultar estudiante | Entidad Estudiante[cite: 37] |
| RF-03 Registrar curso | Entidad Curso[cite: 37] |
| RF-04 Matricular estudiante | Entidad Matricula[cite: 37] |

## 4. Flujo general

### Registro de estudiante
1. El usuario ingresa la información del estudiante.
2. El sistema valida los datos obligatorios.
3. El sistema crea un objeto Estudiante.
4. El sistema almacena la información.[cite: 37]

### Registro de curso
1. El usuario ingresa los datos del curso.
2. El sistema valida la información.
3. El sistema almacena el curso.[cite: 37]

### Matrícula
1. El usuario selecciona un estudiante.
2. El usuario selecciona un curso.
3. El sistema verifica que ambos existan.
4. El sistema registra la matrícula.[cite: 37]

## 5. Trazabilidad de diseño
Este diseño se deriva de los requisitos definidos en el elemento de configuración REQ-001 versión 1.1[cite: 37].  
La versión 1.1 de DIS-001 se actualiza como consecuencia de la solicitud de cambio CR-001 - Agregar teléfono al estudiante[cite: 37].  
Cualquier modificación que afecte la estructura de estudiantes, cursos o matrículas deberá evaluarse para determinar su impacto sobre este elemento de configuración[cite: 37].