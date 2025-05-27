#Aquí se define la lógica y los datos (modelo) de la tarea

class TareaModel:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 0<= indice < len(self.tareas):
            del self.tareas[indice]

    def obtener_tareas(self):
        return self.tareas