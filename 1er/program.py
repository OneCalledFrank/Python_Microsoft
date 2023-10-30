# Programa con python .py

from datetime import date
primer = 1 + 2
print(primer)

# Función print()

print("Muestra ésto por consola")

# Variables en python

# sum = 1 + 2  # 3
product = sum * 2
print(product)

# Tipos de datos
# Numérico = int, float, complex, no = 3
# Texto = str = "un string literal"
# Booleano = continue = true/false

# Fragmento que muestra ejemplos

planetas_en_el_sistema_solar = 8  # int, plutón era el 9eno, pero es muy pequeño
distancia_a_alpha_centauri = 4.367  # float, años luz
puede_lanzamiento = True  # boleano
llego_a_la_luna = "Apollo 11"  # string

# Se puede detectar con la función "type()"
# Se debe añadir la función print() para que te muestre por consola

print(type(distancia_a_alpha_centauri))  # <class 'float'>
print(type(planetas_en_el_sistema_solar))
print(type(puede_lanzamiento))
print(type(llego_a_la_luna))

# Operadores aritméticos
# + - / *
# 1 + 1
# 1 - 2
# 10 / 2
# 2 * 2

# Operadores de asignación
# = , += , -= , /= , *=

# x = 2
# x += 2 ahora tiene dos más
# x -= 2 ahora tiene dos menos
# x /= 2 ahora es dividido por dos
# x *= 2 ahora es multiplicado por dos

# Fechas
# para trabajar con fechas de hace una importación del módulo date
# <from datetime import date>

date.today()
print(date.today())

# Quiere usar fecha con algo, una cadena.
# print("La fecha de hoy es: " + date.today())
# Esto envía un error
# Porque se combina dos tipos de datos diferentes
# Para que el código funcione se debe convertir
print("La fecha de hoy es: " + str(date.today()))
