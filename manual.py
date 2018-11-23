import Sokoban
import const
import math
import time
#Rutas de niveles =============================
# Niveles/nivel1.txt
# Niveles/nivel2.txt
# Niveles/nivel3.txt

# Fin rutas ===================================
def jugadorManual():
    arch = "Niveles/nivel2.txt"
    board = Sokoban.Board(arch)
    board.Print()

    gano = -1
    while (gano != 0 and gano != 2):
        mov = input()
        # crear funcion random para obtener una letra entre w,a,s,d
        # la letra obtenida se pasa a la funcion movimientos.
        board.movimientos(mov)
        print(board.playerpos)
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
    arch = "Niveles/nivel2.txt"
    board = Sokoban.Board(arch)
    board.Print()
    board.jugadorAutomatico()
    
def calculatedistance( P , J):
    #print(P)
    #print(J)
    x = P[0] - J[0]
    y = P[1] - J[1]
    x2 = x * x
    y2 = y * y
    z = x2 + y2
    R = math.sqrt(z)
    return R     

def ubicate(pos, C, board):
    i = C[1]
    j = C[0]
    ya = 0
    ya2 = 0
    k = 0
    board.Print()
    print("Pos", pos)
    carry = 0
    while (pos[1] != board.playerpos[0] or pos[0] != board.playerpos[1]):
        if (pos[1] == board.playerpos[0]):
            board.Print()
            print("Especial CASE before", board.playerpos[1], pos[0])
            if (pos[0] - 1 == board.playerpos[0]):
                print("Especial CASE")
                board.movimientos("D")
                carry = 1
            else:
                if (pos[0] + 1 == board.playerpos[0]):
                    board.movimientos("A")
                    carry = 1
        else:
            if (pos[0] == board.playerpos[1]):
                if (pos[1] - 1 == board.playerpos[1]):
                    print("Especial CASE")
                    board.movimientos("W")
                    carry = 1
            else:
                if (pos[1] + 1 == board.playerpos[1]):
                    board.movimientos("S")
                    carry = 1
        if carry == 0: 
            if (j < C[1] + 1 and ya == 0):
                #print(M[i][j])
                board.movimientos("A")
                print("A")
                j = j + 1
            else:
                ya = 1
                if (i <= C[0] + 1 and ya2 == 0):
                    #print(M[i][j])
                    board.movimientos("W")
                    print("W")
                    i = i + 1
                else:
                    ya2 = 1
                    if (j > C[1] - 1):
                        #print(M[i][j])
                        board.movimientos("S")
                        print("S")
                        j = j - 1
                    else:
                        if (i >= C[0] - 1):
                        #print(M[i][j])
                            board.movimientos("D")
                            print("D")
                            i = i - 1
        board.Print()
        k = k + 1



def gototherightplace(J, C, M, board):
    A = [J[0],J[1]]
    y = C[0] - M[0]
    x = C[1] - M[1]
    print("C: ",C)
    print("M: ",M)
    print("X: ",abs(x))
    print("Y: ",abs(y))
    if abs( x ) > abs( y ): #Si se mueve en x
        if x < 0: #Izquierda
            D = "A"
            pos = [ C[ 0 ] - 1,C[ 1 ] ]
            print("PosA:",pos)
        else: #derecha
            if x > 0:
                D = "D"
                pos = [ C[ 0 ] + 1,C[ 1 ] ]
                print("PosD:",pos)
        #end if
    else:
        if y < 0: # Si se mueve en y arriba
            D = "W"
            pos = [ C[ 0 ],C[ 1 ] - 1]
            print("PosW:",pos)
        else:
            if y > 0: #abajo
                D = "S"
                pos = [ C[ 0 ],C[ 1 ] + 1]
                print("PosS:",pos)
        #end if
    #end if
    print("Pos:",pos)
    ubicate(pos,C,board)

    







def movetobox ( J , C , M, board):
    #Codigo para mover al jugador hacia la caja
    A = [J[0],J[1]]
    distancia = calculatedistance( A, C )
    #print("distancia",distancia)
    while ( distancia > 1.0 ):
    #    print("J: ",J)#Jugador
    #    print("C: ",C)#Caja
        time.sleep(1.0)
        board.Print()
        y = C[0] - A[0]
        x = C[1] - A[1]
    #    print( abs(x) , abs(y) )
        if abs( x ) > abs( y ): #Si se mueve en x
    #        print("J-",J)
            if x < 0: #Derecha
    #            print("J-",A)
                board.movimientos("A")
     #           print("J-",A)
                P = board.playerpos
      #          print(J,P)
       #         print("A")
                if P[0] == A[0] and P[1] == A[1]:
                    #Si no se movio
                    if y > 0:
                        P = board.movimientos("S")
        #                print("SA")
                        A[0] = P[0]
                        A[1] = P[1]
                    else:
                        P = board.movimientos("W")
         #               print("WA")
                        A[0] = P[0]
                        A[1] = P[1]
                    #end if
                else:
                    #Si se movio
                    A[0] = P[0]
                    A[1] = P[1]
                #end if
            else: #Izquierda
                if x > 0:
                    P = board.movimientos("D")
          #          print("D")
                    if P[0] == A[0] and P[1] == A[1]:
                        #Si no se movio
                        if y > 0:
                            P = board.movimientos("S")
           #                 print("DS")
                            A[0] = P[0]
                            A[1] = P[1]
                        else:
                            P = board.movimientos("W")
            #                print("DW")
                            A[0] = P[0]
                            A[1] = P[1]
                        #end if
                    else:
                        #Si se movio
                        A[0] = P[0]
                        A[1] = P[1]
                    #end if
            #end if
        else:
            if y < 0: # Si se mueve en y arriba
                P = board.movimientos("W")
             #   print("W")
                if P[0] == A[0] and P[1] == A[1]:
                    #Si no se movio
                    if x > 0:
                        P = board.movimientos("D")
              #          print("WD")
                        A[0] = P[0]
                        A[1] = P[1]
                    else:
                        P = board.movimientos("A")
               #         print("WA")
                        A[0] = P[0]
                        A[1] = P[1]
                    #end if
                else:
                    #Si se movio
                    A[0] = P[0]
                    A[1] = P[1]
                #end if
            else:
                if y > 0: #abajo
                    P = board.movimientos("S")
                #    print("S")
                    if P[0] == A[0] and P[1] == A[1]:
                        #Si no se movio
                        if x > 0:
                            P = board.movimientos("D")
                 #           print("SD")
                            A[0] = P[0]
                            A[1] = P[1]
                        else:
                            P = board.movimientos("A")
                  #          print("SA")
                            A[0] = P[0]
                            A[1] = P[1]
                        #end if
                    else:
                        #Si se movio
                        A[0] = P[0]
                        A[1] = P[1]
                    #end if
            #end if
        #end if
        
        distancia = calculatedistance( A, C )
        #print("A: ",A)
        #print("C: ",C)
        #print("D---",distancia)
        #print("iteracion")
    #end while
    gototherightplace(A, C, M, board)
    
    #print("End while")
#end function

#def movebox (J, C, M,board):


def algoritmo():
    arch = "Niveles/nivel1.txt"
    board = Sokoban.Board(arch)
    tablero = board.Data
    cajas = []
    metas = []
    for i in range ( len( tablero ) - 1):
        for j in range ( len ( tablero[ i ] ) - 1 ):
            if tablero[ i ][ j ] == const.CAJA:
                cajas.append( [i,j] )
            #end if 
            if tablero[ i ][ j ] == const.META:
                metas.append( [i,j] )
            #end if
        #end for
    #end for
    #print(cajas)
    #print(metas)
    while ( len( cajas ) != 0 and board.estadoJugador()!=0 and board.estadoJugador() != 2): 
     #   print("CYCLE")
        min_d = 100000
        cajacercana = []
        for i in range ( len( cajas ) ):
            dis = calculatedistance( cajas[ i ] , board.playerpos)
            if dis < min_d:
                min_d = dis
                cajacercana = cajas[ i ]
            #end if
        #end for
        min_d = 100000
        metacercana = []
        for i in range ( len( metas ) ):
            dis = calculatedistance( cajacercana , metas[ i ] )
            if dis < min_d:
                min_d = dis
                metacercana = metas[ i ]
            #end if 
        #end for
      #  print( cajacercana ) #Print
        #print( metacercana ) #Print

        #MOVERSE HASTA LA CAJA Y PONERSE CONTRARIO A LA META
        movetobox(board.playerpos,cajacercana,metacercana,board)
        #INTENTAR MOVER LA CAJA
        #movebox(board.playerpos,cajacercana,metacercana,board)
        gano = board.estadoJugador()
        if gano != 0 and gano != 2:
            cajas.remove(cajacercana)
        else:
            if gano == 0:
                print("YOU LOSE")
            else:
                if gano == 2:
                    print("YOU WIN")
    




print ("==========MENU===========")
print ("1 ->  para jugador manual")
print ("2 -> para jugador automatico")
print ("3 -> para alogritmo pro")
selection = input()
if(selection == "1"):
    jugadorManual()
elif (selection == "2"):
    jugadorAutomatico()
elif (selection == "3"):
    algoritmo()
else:
    print("Mal dijitado")
    

