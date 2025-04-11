class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def __str__(self):
        estado = "[X]" if self.completada else "[ ]"
        return f"{estado} {self.descripcion}"

class ToDoList:
    def __init__(self, archivo="tareas.txt"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        """Carga las tareas desde el archivo."""
        try:
            archivo = open(self.archivo, "r")
            tareas = []
            for linea in archivo:
                datos = linea.strip().split(" | ", 1)
                if len(datos) == 2:
                    completada, descripcion = datos
                    tareas.append(Tarea(descripcion, completada == "1"))
            archivo.close()
            return tareas
        except:
            return []

    def guardar_tareas(self):
        """Guarda las tareas en el archivo."""
        archivo = open(self.archivo, "w")
        for tarea in self.tareas:
            archivo.write(f"{int(tarea.completada)} | {tarea.descripcion}\n")
        archivo.close()

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista."""
        self.tareas.append(Tarea(descripcion))
        self.guardar_tareas()

    def listar_tareas(self):
        """Muestra la lista de tareas."""
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        for i in range(len(self.tareas)):
            print(f"{i + 1}. {self.tareas[i]}")

    def marcar_completada(self, numero):
        """Marca una tarea como completada."""
        if 1 <= numero <= len(self.tareas):
            self.tareas[numero - 1].completada = True
            self.guardar_tareas()

    def eliminar_tarea(self, numero):
        """Elimina una tarea de la lista."""
        if 1 <= numero <= len(self.tareas):
            self.tareas.pop(numero - 1)
            self.guardar_tareas()

# Ejemplo de uso sin menú
lista = ToDoList()

# Agregar tareas
lista.agregar_tarea("Estudiar para el examen")
lista.agregar_tarea("Hacer ejercicio")
lista.agregar_tarea("Leer un libro")

# Listar tareas
print("\nLista de tareas:")
lista.listar_tareas()

# Marcar una tarea como completada
lista.marcar_completada(2)

# Listar tareas después de marcar como completada
print("\nLista de tareas después de completar una:")
lista.listar_tareas()

# Eliminar una tarea
lista.eliminar_tarea(1)

# Listar tareas después de eliminar
print("\nLista de tareas después de eliminar una:")
lista.listar_tareas()
