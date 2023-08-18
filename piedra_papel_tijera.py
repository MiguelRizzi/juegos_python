from random import randint 

def jugadas_jugador():
    jugada_jugador = int(input("ingresa 1 para piedra, 2 papel o 3 tijeras: "))
    
    if jugada_jugador == 1:
        print("\nElegiste piedra ✊") 
    elif jugada_jugador == 2:
        print("\nElegiste papel ✋")
    elif jugada_jugador == 3:
        print("\nElegiste tijeras ✌️")
    else:
        print("\nElegiste mal 👎")
    
    return jugada_jugador

def jugadas_pc ():
    jugada_pc = randint(1,3)

    if jugada_pc == 1:
        print("La maquina eligio piedra ✊") 
    elif jugada_pc == 2:
        print("La maquina eligio papel ✋")
    else:
        print("La maquina eligio tijeras ✌️")

    return jugada_pc


def mensaje_final(victorias_jugador, victorias_pc):
    print(f"\nGanaste {victorias_jugador} veces, la maquina gano {victorias_pc} veces.")
    if victorias_jugador == 3:
        print("Felicitaciones ganaste!!!!!😊😊😊")
    else:
        print("Gano la maquina 😔😔😔")

def main():
    victorias_jugador = 0
    victorias_pc = 0
    while victorias_jugador < 3 and victorias_pc <3:
        jugada_jugador = jugadas_jugador()
        jugada_pc = jugadas_pc()
        if jugada_jugador == 1 and jugada_pc == 3:
            print("Ganaste 😊\n")
            victorias_jugador += 1
        elif jugada_jugador == 2 and jugada_pc == 1:
            print("Ganaste 😊\n")
            victorias_jugador += 1
        elif jugada_jugador == 3 and jugada_pc == 2:
            print("Ganaste 😊\n")
            victorias_jugador += 1
        elif jugada_jugador == jugada_pc:
            print("Empate 😑\n")
        else:
            print("Perdiste 😔\n")
            victorias_pc += 1
    mensaje_final(victorias_jugador, victorias_pc)
   
            
main()