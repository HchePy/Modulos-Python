# Modulo de menu para facilitarme la vida :)
def mostrar_menu(opciones):
    # Opciones es una lista 
    """
    Muestra un menú con las opciones proporcionadas y solicita al usuario que seleccione una.
    
    Args:
        opciones (list): Lista de cadenas que representan las opciones del menú.
    
    Returns:
        int: El índice de la opción seleccionada (comenzando desde 1).
    """
    while True:
        # Mostrar las opciones
        print("\n--- Menú ---")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")
        print("0. Salir")

        # Solicitar la selección del usuario
        try:
            seleccion = int(input("\nSelecciona una opción: "))
            if 0 <= seleccion <= len(opciones):
                return seleccion
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")