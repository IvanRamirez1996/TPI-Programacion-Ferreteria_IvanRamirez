def validar_nombre(nombre: str, inventario: list) -> str:
    """Valida que el nombre no esté vacío y no esté duplicado en el inventario."""
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la herramienta no puede estar vacío o contener solo espacios.")
    
    for producto in inventario:
        if producto['herramienta'].lower() == nombre_limpio.lower():
            raise ValueError(f"La herramienta '{nombre_limpio}' ya existe en el inventario.")
            
    return nombre_limpio

def buscar_herramienta(nombre: str, inventario: list) -> dict:
    """Busca una herramienta en el inventario ignorando mayúsculas y espacios extremos."""
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
        
    for producto in inventario:
        if producto['herramienta'].lower() == nombre_limpio.lower():
            return producto
    return None