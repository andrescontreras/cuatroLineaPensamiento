import Sokoban
#Rutas de niveles =============================
# Niveles/nivel1.txt
# Niveles/nivel2.txt
# Niveles/nivel3.txt

# Fin rutas ===================================
def jugadorManual():
    arch = "Niveles/nivel1.txt"
    board = Sokoban.Board(arch)
    board.Print()

    gano = -1
    while (gano != 0 and gano != 2):
        mov = input()
        # crear funcion random para obtener una letra entre w,a,s,d
        # la letra obtenida se pasa a la funcion movimientos.,
        board.movimientos(mov)
        print("====================================================================================")
        board.Print()
        gano = board.estadoJugador()
    print("GAME OVER")
    if gano == 0:
        print("YOU LOSE")
    else:
        if gano == 2:
            print("YOU WIN")

def jugadorAutomatico():
    arch = "Niveles/nivel1.txt"
    board = Sokoban.Board(arch)
    board.Print()
    board.jugadorAutomatico()


print ("==========MENU===========")
print ("1 ->  para jugador manual")
print ("2 -> para jugador automatico")
selection = input()
if(selection == "1"):
    jugadorManual()
elif (selection == "2"):
    jugadorAutomatico()
else:
    print("dato invalido")
    
