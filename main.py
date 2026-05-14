import os
from funcion_n import suma, resta, multiplicacion

# Uso de las funciones
print("La suma de 5 y 3 es:", suma(5, 3))
print("La resta de 10 y 4 es:", resta(10, 4))
print("La multiplicación de 2 y 6 es:", multiplicacion(2, 6))

# Generación de la carpeta y archivos falsos para la prueba de Git
os.makedirs('resultados', exist_ok=True)

with open('resultados/grafica.png', 'w') as f:
    f.write('Archivo de imagen generado')
    
with open('resultados/diagrama.eps', 'w') as f:
    f.write('Archivo de vector generado')

print("Hello world")