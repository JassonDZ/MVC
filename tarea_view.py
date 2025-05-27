#Define la vista e interfaz de usuario de la tarea

class TareaView:
    def mostrar_tareas(self, tareas):
        print("\nLista de Tareas:")
        if not tareas:
            print(" (Sin tareas)")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
    
    def pedir_tarea(self):
        return input("Escribe una nueva tarea: ")
    
    def pedir_indice_eliminar(self):
        return int(input("Escribe el número de la tarea a eliminar: ")) - 1
    
    def mostar_menu(self):
        print("\n--- Menú de Tareas ---")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea por índice")
        print("4. Salir")
        return input("Selecciona una opción: ")