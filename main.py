import ahorcado_diagramas
import palabras

seleccionRandom=palabras.seleccionRandom
#print(seleccionRandom)

print("---------- A H O R C A D O ----------")

print("La palabra que debes adivinar tiene", len(seleccionRandom), "letras y es un animal")

palabra = ["_" for _ in seleccionRandom]
letras_incorrectas = []

diagrama_actual=ahorcado_diagramas.diagramas[0]
indice_diagrama = 0

print(diagrama_actual)
print(" ".join(palabra))


while True:
    letraUsuario = input("Escriba una letra: ").lower()

    if letraUsuario in seleccionRandom and len(letraUsuario) == 1:
        print(f"{letraUsuario} es correcta")
        for i in range(len(seleccionRandom)):
            if seleccionRandom[i] == letraUsuario:
                palabra[i] = letraUsuario
        print(diagrama_actual)
        print(" ".join(palabra))
    elif len(letraUsuario) > 1:
        print("Respuesta inválida, introduce sólo una letra")
    elif letraUsuario == " ":
        print("Respuesta vacía, introduce una letra")
    else:
        print(f"{letraUsuario} es incorrecta")
        letras_incorrectas.append(letraUsuario)
        indice_diagrama += 1
        if indice_diagrama < len(ahorcado_diagramas.diagramas):
            diagrama_actual = ahorcado_diagramas.diagramas[indice_diagrama]
            print(diagrama_actual)
            print(" ".join(palabra))
        else:
            print("Te has quedado sin intentos --- A h o r c a d o ---")
            break

    if "_" not in palabra:
        print("Adivinaste la palabra ---", seleccionRandom)
        print("Felicidades, ganaste!")
        break
        
    print("Respuestas incorrectas:", letras_incorrectas)
