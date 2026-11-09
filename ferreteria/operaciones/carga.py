from ferreteria.utilidades.validaciones import validar_nombre, buscar_herramienta

def cargar_herramientas(inventario: list):
    """Opción 1: Carga múltiple de herramientas con existencias iniciales."""
    while True:
        try:
            cantidad_str = input("¿Cuántas herramientas distintas desea cargar?: ")
            cantidad_cargas = int(cantidad_str)
            if cantidad_cargas <= 0:
                raise ValueError("La cantidad de herramientas a cargar debe ser mayor a 0.")
            break
        except ValueError as e:
            if "desea cargar" in str(e) or "mayor a 0" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: La cantidad ingresada debe ser un número entero válido.")

    for _ in range(cantidad_cargas):
        # Validación del nombre con reintento interno
        while True:
            try:
                nombre_ingresado = input("Ingrese el nombre de la herramienta: ")
                nombre_valido = validar_nombre(nombre_ingresado, inventario)
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Validación del stock inicial con reintento interno, conservando el nombre
        while True:
            try:
                stock_str = input(f"Ingrese el stock inicial para '{nombre_valido}': ")
                stock_inicial = int(stock_str)
                if stock_inicial < 0:
                    raise ValueError("El stock inicial no puede ser negativo.")
                break
            except ValueError as e:
                if "negativo" in str(e):
                    print(f"Error: {e}")
                else:
                    print("Error: El stock debe ser un número entero válido.")

        # Se agrega directamente a la lista de diccionarios (sin diccionarios sueltos)[cite: 10]
        inventario.append({'herramienta': nombre_valido, 'cantidad': stock_inicial})
        print(f"¡Herramienta '{nombre_valido}' cargada exitosamente!")

def alta_producto(inventario: list):
    """Opción 5: Alta de nuevo producto (los errores se propagan a main)."""
    nombre_ingresado = input("Ingrese el nombre de la nueva herramienta: ")
    nombre_valido = validar_nombre(nombre_ingresado, inventario)
    
    stock_str = input(f"Ingrese el stock inicial para '{nombre_valido}': ")
    stock_inicial = int(stock_str)
    if stock_inicial < 0:
        raise ValueError("El stock inicial no puede ser negativo.")
        
    inventario.append({'herramienta': nombre_valido, 'cantidad': stock_inicial})
    print(f"¡Nueva herramienta '{nombre_valido}' dada de alta exitosamente!")