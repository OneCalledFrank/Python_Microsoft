fact = "The Moon has no atmosphere."
print(fact)


multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline)


print("temperatures and facts about the moon".title())


temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
# Muestra donde está la primera ocurrencia del valor
# Si no lo encuentra, muestra -1
# 0 - >


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
# Count() muestra las veces que se repiten las palabras.


print("The Moon And The Earth".lower())
# Deja todo en minúsculas

print("The Moon And The Earth".upper())
# Deja todo en mayúsculas

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
# Se puede separar por el valor que se le entrega
# Así obtenemos la temperatura, separada del texto.

# .isnumeric(), .isdecimal()
# Se usan para buscar números y decimales
# Devuelve True o False

# .startswith()
# # Empieza por y devuelve el valor True o False

# .endswith()
# Lo mismo que startswith pero en termina con. También devuelve True o False

# .replace()
# Remplaza una palabra por otra
# .replace("Celsius", "C")

moon_facts = ["The Moon is drifting away from the Earth.",
              "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
# Se usa el ' ' para unir todos los elementos de la lista.
# Salida: The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year.
