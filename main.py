from ferreteria.interfaz.menu import mostrar_menu
from ferreteria.operaciones.carga import cargar_herramientas, alta_producto
from ferreteria.operaciones.consultas import mostrar_inventario, consultar_stock, reporte_agotados
from ferreteria.operaciones.stock import actualizar_stock

def main():
    # El inventario se crea aquí y viaja exclusivamente por parámetro (sin variables globales)
    inventario = []
    opcion = 0
    
    # El menú se repite de forma persistente hasta que el usuario elige la opción 7
    while opcion != 7:
        mostrar_menu()
        try:
            opcion_str = input("Seleccione una opción (1 a 7): ")
            opcion = int(opcion_str)
            
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion == 7:
                print("Saliendo del sistema de control de inventario. ¡Hasta luego!")
            else:
                raise ValueError("Opción fuera de rango. Debe ser un número entero entre 1 y 7.")
                
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()