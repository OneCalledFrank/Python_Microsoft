# Para capturar información del usuario, use la función input()
print("Bienvenido al programa 'saludos'")
nombre = input("Ingrese su nombre:\n")
print("Bienvenid@ " + nombre)

# Lo guarda en una variable 'nombre' y lo ejecuta cuando el usuario
# termine de ingresar su dato.

# También se puede trabajar con números
print("PROGRAMA CALCULADORA")
prim_num = input("El primer número es: ")
segu_num = input("El segúndo número es: ")
# Si no le colocamos que sea 'int()'
# Nos dará un 'str'
# Y si el primer número es 1
# Y el segundo es 2
# El resultado será: 12
print(int(prim_num) + int(segu_num))
