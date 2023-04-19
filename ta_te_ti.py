tablero = [" " for i in range(9)]

def print_tablero():
    fila1 = f"| {tablero[0]} | {tablero[1]} | {tablero[2]} |"
    fila2 = f"| {tablero[3]} | {tablero[4]} | {tablero[5]} |"
    fila3 = f"| {tablero[6]} | {tablero[7]} | {tablero[8]} |"

    print()
    print(fila1)
    print(fila2)
    print(fila3)
    print()

def jugador_mov(icono):
    if icono == "X":
        numero = 1
    elif icono == "O":
        numero = 2
    print(f"Tu turno jugador {numero}")
    eleccion = int(input("Ingrese su movimiento (1-9): ").strip())
    if tablero[eleccion - 1] == " ":
        tablero[eleccion - 1] = icono
    else:
        print()
        print("Ese espacio esta ocupado.")
    
def es_victoria(icono):
    if (tablero[0] == icono and tablero[1] == icono and tablero[2] == icono) or \
       (tablero[3] == icono and tablero[4] == icono and tablero[5] == icono) or \
       (tablero[6] == icono and tablero[7] == icono and tablero[8] == icono) or \
       (tablero[0] == icono and tablero[3] == icono and tablero[6] == icono) or \
       (tablero[1] == icono and tablero[4] == icono and tablero[7] == icono) or \
       (tablero[2] == icono and tablero[5] == icono and tablero[8] == icono) or \
       (tablero[0] == icono and tablero[4] == icono and tablero[8] == icono) or \
       (tablero[2] == icono and tablero[4] == icono and tablero[6] == icono):
        return True
    else:
        return False

def es_empate():
    if " " not in tablero:
        return True
    else:
        return False

while True:
    print_tablero()
    jugador_mov("X")
    print_tablero()
    if es_victoria("X"):
        print_tablero()
        print("X es el ganador, felicitaciones.")
        break
    elif es_empate():
        print("Esto es empate.")
        break
    jugador_mov("O")
    if es_victoria("O"):
        print_tablero()
        print("O es el ganador, felicitaciones.")
        break
    elif es_empate():
        print("Esto es empate.")
        break
    

