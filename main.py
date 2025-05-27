# El main permite el ejecutar el programa
from tarea_model import TareaModel
from tarea_view import TareaView
from tarea_controller import TareaController

if __name__ == "__main__":
    modelo= TareaModel()
    vista = TareaView()
    controlador = TareaController() 
controlador.ejecutar()
# Controlador de tareas se conecta a la vista y al modelo