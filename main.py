from random import randint

numero_azar = randint(0,20)

print("Hola, bienvenido a adivina el numero!\n")

try:
	for i in range(5):
		estimacion = int(input("\nIngresa una estimación: "))

		if estimacion == numero_azar:
			print("Has ganado el juego en {0} intentos".format(i + 1))
			exit()
		elif estimacion > numero_azar:
			print("El numero estimado es muy grande!")
		else:
			print("El numero estimado es muy pequeño!")

except Exception:
	print("\nLa entrada de datos no es la correcta!!!")

print("\nLo siento, has perdido el juego :(")
