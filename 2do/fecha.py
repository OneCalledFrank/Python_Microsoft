# Para importar la fecha de importa el módulo 'DATE'
from datetime import date

# Se puede llamar a una función con la que se quiere trabajar
# para obtener la fecha de hoy, puede llamar a la función 'today()'

date.today()

# Para mostrar por consola, es con print()

print(date.today())

# Podemos experimentar

# print("La fecha de hoy es: " + date.today()) -> Da error
# Por el tipo de dato

print("La fecha de hoy es: " + str(date.today()))


# Funcionará con F-strings?

print(f"La fecha de hoy es: {date.today()}")

# Sí funciona.
