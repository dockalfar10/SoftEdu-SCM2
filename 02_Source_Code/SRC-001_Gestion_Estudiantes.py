"""
SRC-001: Módulo de Gestión (Código Fuente)
Proyecto: SoftEdu-SCM
Versión: 1.0
Descripción: Implementación de la clase lógica correspondiente al REQ-001 y DIS-001.
"""

class GestionProyectoEstudiante:
    def __init__(self):
        # Simulación de una base de datos o almacenamiento en memoria local
        self.registros = []

    def crear_registro(self, codigo: str, nombre: str, descripcion: str, responsable: str, estado: str):
        """Registra un nuevo elemento validando campos obligatorios."""
        if not codigo or not nombre or not responsable:
            raise ValueError("Los campos código, nombre y responsable son obligatorios.")
        
        nuevo_item = {
            "codigo": codigo,
            "nombre": nombre,
            "descripcion": descripcion,
            "responsable": responsable,
            "estado": estado
        }
        self.registros.append(nuevo_item)
        return f"Registro '{nombre}' creado exitosamente."

    def consultar_registros(self):
        """Retorna todos los registros almacenados."""
        return self.registros

    def actualizar_registro(self, codigo: str, nuevos_datos: dict):
        """Actualiza un registro existente según su código."""
        for item in self.registros:
            if item["codigo"] == codigo:
                item.update(nuevos_datos)
                return f"Registro con código '{codigo}' actualizado correctamente."
        return f"No se encontró el registro con código '{codigo}'."

    def eliminar_registro(self, codigo: str):
        """Da de baja/elimina un registro según su código."""
        for i, item in enumerate(self.registros):
            if item["codigo"] == codigo:
                eliminado = self.registros.pop(i)
                return f"Registro '{eliminado['nombre']}' eliminado correctamente."
        return f"No se encontró el registro con código '{codigo}'."


# --- Bloque de prueba local ---
if __name__ == "__main__":
    modulo = GestionProyectoEstudiante()
    
    # Prueba de creación
    print(modulo.crear_registro(
        codigo="PROJ-001",
        nombre="Plataforma Educativa",
        descripcion="Desarrollo del core de gestión escolar",
        responsable="OWNER",
        estado="Activo"
    ))
    
    # Prueba de consulta
    print("Listado actual:", modulo.consultar_registros())