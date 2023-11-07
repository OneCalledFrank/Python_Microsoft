# Crea una variable llamada 'parsecs_input' como input
# el cual deja ingresar los datos.
parasecs_input = input("Ingrese el número de parasecs: ")

# Luego, convierte 'parasecs_input' a un integer, con int()
# y guarda el valor en 'parasecs'
parasecs = int(parasecs_input)

# Finaliza el calculo (parasecs * 3.26)
lightyears = parasecs * 3.26

# Muestra el resultado
print(f"{parasecs} parasecs son {lightyears} años luz")
