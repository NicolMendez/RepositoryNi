#Codigo que evalua contraseñas cmbio ;
def evaluar_seguridad(password):
    """Evalúa la fortaleza de una contraseña basandose en su longitud."""
    longitud = len(password)
    
    if longitud < 6:
        return "Nivel: Débil (Muy corta)"
    elif 6 <= longitud < 10:
        return "Nivel: Media"
    else:
        return "Nivel: Fuerte"

print("--- Sistema de Validación de Credenciales ---")
clave = input("Ingresa la contraseña para analizar: ")
resultado = evaluar_seguridad(clave)

print(f"\nResultado del análisis: {resultado}")
print("Recomendación: Usa siempre más de 10 caracteres.")