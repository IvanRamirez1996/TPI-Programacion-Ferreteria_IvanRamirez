from ferreteria.utilidades.validaciones import buscar_herramienta

def mostrar_inventario(inventario: list):
    """Opción 2: Muestra el listado completo de herramientas y su stock."""
    if not inventario:
        print("Aviso: Todavía no hay herramientas cargadas en el inventario.")
        return
    
    print("\n--- LISTADO DE INVENTARIO ---")
    for producto in inventario:
        print(f"Herramienta: {producto['herramienta']} | Stock: {producto['cantidad']}")
    print("-" * 30)

def consultar_stock(inventario: list):
    """Opción 3: Consulta el stock de una herramienta específica."""
    if not inventario:
        print("Aviso: Todavía no hay herramientas cargadas en el inventario.")
        return
    
    nombre_ingresado = input("Ingrese el nombre de la herramienta a consultar: ")
    nombre_limpio = nombre_ingresado.strip()
    if not nombre_limpio:
        raise ValueError("El nombre a consultar no puede estar vacío.")
        
    producto = buscar_herramienta(nombre_limpio, inventario)
    if producto is None:
        print(f"Aviso: La herramienta '{nombre_limpio}' no se encuentra en el catálogo.")
    else:
        print(f"Stock disponible de '{producto['herramienta']}': {producto['cantidad']} unidades.")

def reporte_agotados(inventario: list):
    """Opción 4: Reporta productos con stock igual a cero."""
    if not inventario:
        print("Aviso: Todavía no hay herramientas cargadas en el inventario.")
        return
    
    agotados = [p for p in inventario if p['cantidad'] == 0]
    
    if not agotados:
        print("Aviso: Ninguna herramienta tiene stock cero en este momento.")
    else:
        print("\n--- REPORTE DE HERRAMIENTAS AGOTADAS (STOCK 0) ---")
        for producto in agotados:
            print(f"Herramienta: {producto['herramienta']}")
        print("-" * 48)