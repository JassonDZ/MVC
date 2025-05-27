# Controlador de tareas se conecta a la vista y al modelo
from tarea_model import TareaModel
from tarea_view import TareaView

class TareaController:
    def __init__(self):
        self.modelo = TareaModel()
        self.vista = TareaView()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostar_menu()
            if opcion == "1":
                tareas= self.modelo.obtener_tareas()
                self.vista.mostrar_tareas(tareas)
            elif opcion == "2":
                nueva = self.vista.pedir_tarea()
                self.modelo.agregar_tarea(nueva)
            elif opcion == "3":
                self.vista.mostrar_tareas(self.modelo.obtener_tareas())
                idx=self.vista.pedir_indice_eliminar()
                self.modelo.eliminar_tarea(idx)
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")