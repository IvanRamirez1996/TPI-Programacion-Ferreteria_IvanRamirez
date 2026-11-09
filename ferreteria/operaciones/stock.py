from ferreteria.utilidades.validaciones import buscar_herramienta

def actualizar_stock(inventario: list):
    """Opción 6: Actualiza el stock mediante venta o ingreso."""
    if not inventario:
        print("Aviso: Todavía no hay herramientas cargadas en el inventario.")
        return
        
    nombre_ingresado = input("Ingrese el nombre de la herramienta a actualizar: ")
    nombre_limpio = nombre_ingresado.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
        
    producto = buscar_herramienta(nombre_limpio, inventario)
    if producto is None:
        print(f"Aviso: La herramienta '{nombre_limpio}' no existe en el catálogo.")
        return
        
    print("Tipos de movimiento:")
    print("1. Venta")
    print("2. Ingreso")
    tipo_movimiento = input("Seleccione el tipo de movimiento (1 o 2 / venta o ingreso): ").strip().lower()
    
    if tipo_movimiento not in ['1', '2', 'venta', 'ingreso']:
        print("Error: Tipo de movimiento inválido. Debe ser 'venta' o 'ingreso'.")
        return
        
    unidades_str = input("Ingrese la cantidad de unidades: ")
    unidades = int(unidades_str)
    if unidades <= 0:
        raise ValueError("Las unidades del movimiento deben ser mayores a 0.")
        
    if tipo_movimiento in ['1', 'venta']:
        if producto['cantidad'] < unidades:
            raise ValueError(f"Stock insuficiente. Stock actual: {producto['cantidad']}, unidades a vender: {unidades}.")
        producto['cantidad'] -= unidades
        print(f"¡Venta realizada con éxito! Nuevo stock de '{producto['herramienta']}': {producto['cantidad']}.")
    else:
        producto['cantidad'] += unidades
        print(f"¡Ingreso registrado con éxito! Nuevo stock de '{producto['herramienta']}': {producto['cantidad']}.")