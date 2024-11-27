

import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("bienvenido al juego de adivinar el numero secreto!")

while not adivinado and cant_intentos <= cant_max_intentos :
    entrada = input("introduce un numero del 1 al 99: ") # TODO: convertir a numero
    numero = int(entrada)
    if numero == numero_secreto:
        print("!felicitaciones has adivinado el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")
    else:
        print("el numero es menor al ingresado")

    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("!GAME OVER! NO HAS PODIDO ADIVINAR EN LA CANTIDAD DE 5 INTENTOS")
    

        


