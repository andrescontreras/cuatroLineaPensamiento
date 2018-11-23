import Sokoban
import const
import math
import time


class Jugador:
    cajas = []
    metas = []
    direccion = True  # true -> horizontal ,false -> vertical
    tablero = [[]]
    board = []

    def jugar(self):
        arch = "Niveles/nivel1.txt"
        self.board = Sokoban.Board(arch)
        Jugador.tablero = self.board.Data
        self.buscarCajasMetas()
        while (len(self.cajas) != 0 and self.board.estadoJugador() != 0 and self.board.estadoJugador() != 2):
            cajacercana = self.getCajaCercana()
            metacerca = self.getMetaCercana(cajacercana)
            self.moverJugadorAcaja(cajacercana)
            while(cajacercana != metacerca):
                time.sleep(2.0)
                movimientos = self.decisionCamino(cajacercana, metacerca)
                self.posicionarJugador(cajacercana, metacerca)
                self.hacerMovimientos(movimientos,cajacercana)
                print("========", cajacercana)
                print("cajas--", self.cajas)
                print("metas--",self.metas)
            self.cajas.remove(cajacercana)
            self.metas.remove(metacerca)

    def buscarCajasMetas(self):
        for i in range(len(self.tablero) - 1):
            for j in range(len(self.tablero[i]) - 1):
                if self.tablero[i][j] == const.CAJA:
                    self.cajas.append([j, i])
                # end if
                if self.tablero[i][j] == const.META:
                    self.metas.append([j, i])
                # end if
            # end for
        # end for

    def getCajaCercana(self):
        cajacercana = []
        min_d = 100000
        for i in range(len(self.cajas)):
            dis = self.calcularDistancia(
                self.cajas[i], self.board.playerpos)
            if dis < min_d:
                min_d = dis
                cajacercana = self.cajas[i]
            # end if
            # end for
        return cajacercana

    def getMetaCercana(self, cajacercana):
        min_d = 100000
        metacercana = []
        for i in range(len(self.metas)):
            dis = self.calcularDistancia(cajacercana, self.metas[i])
            if dis < min_d:
                min_d = dis
                metacercana = self.metas[i]
            # end if
        # end for
        return metacercana

    def calcularDistancia(self, P, J):
        # print(P)
        # print(J)
        x = P[0] - J[0]
        y = P[1] - J[1]
        x2 = x * x
        y2 = y * y
        z = x2 + y2
        R = math.sqrt(z)
        return R

    def moverJugadorAcaja(self, cajacercana):
        # Codigo para mover al jugador hacia la caja
        A = self.board.playerpos

        distancia = self.calcularDistancia(A, cajacercana)
        # print("distancia",distancia)
        while (distancia > 1.0):
        #    print("J: ",J)#Jugador
        #    print("C: ",C)#Caja
            time.sleep(2.0)
            self.board.Print()
            y = cajacercana[0] - A[0]
            x = cajacercana[1] - A[1]
        #    print( abs(x) , abs(y) )
            if abs(x) > abs(y):  # Si se mueve en x
        #        print("J-",J)
                if x < 0:  # Derecha
        #            print("J-",A)
                    self.board.movimientos("A")
        #           print("J-",A)
                    P = self.board.playerpos
        #          print(J,P)
        #         print("A")
                    if P[0] == A[0] and P[1] == A[1]:
                        # Si no se movio
                        if y > 0:
                            P = self.board.movimientos("S")
            #                print("SA")
                            A[0] = P[0]
                            A[1] = P[1]
                        else:
                            P = self.board.movimientos("W")
            #               print("WA")
                            A[0] = P[0]
                            A[1] = P[1]
                        # end if
                    else:
                        # Si se movio
                        A[0] = P[0]
                        A[1] = P[1]
                    # end if
                else:  # Izquierda
                    if x > 0:
                        P = self.board.movimientos("D")
            #          print("D")
                        if P[0] == A[0] and P[1] == A[1]:
                            # Si no se movio
                            if y > 0:
                                P = self.board.movimientos("S")
            #                 print("DS")
                                A[0] = P[0]
                                A[1] = P[1]
                            else:
                                P = self.board.movimientos("W")
                #                print("DW")
                                A[0] = P[0]
                                A[1] = P[1]
                            # end if
                        else:
                            # Si se movio
                            A[0] = P[0]
                            A[1] = P[1]
                        # end if
                # end if
            else:
                if y < 0:  # Si se mueve en y arriba
                    P = self.board.movimientos("W")
                #   print("W")
                    if P[0] == A[0] and P[1] == A[1]:
                        # Si no se movio
                        if x > 0:
                            P = self.board.movimientos("D")
                #          print("WD")
                            A[0] = P[0]
                            A[1] = P[1]
                        else:
                            P = self.board.movimientos("A")
                #         print("WA")
                            A[0] = P[0]
                            A[1] = P[1]
                        # end if
                    else:
                        # Si se movio
                        A[0] = P[0]
                        A[1] = P[1]
                    # end if
                else:
                    if y > 0:  # abajo
                        P = self.board.movimientos("S")
                    #    print("S")
                        if P[0] == A[0] and P[1] == A[1]:
                            # Si no se movio
                            if x > 0:
                                P = self.board.movimientos("D")
                    #           print("SD")
                                A[0] = P[0]
                                A[1] = P[1]
                            else:
                                P = self.board.movimientos("A")
                    #          print("SA")
                                A[0] = P[0]
                                A[1] = P[1]
                            # end if
                        else:
                            # Si se movio
                            A[0] = P[0]
                            A[1] = P[1]
                        # end if
                # end if
            # end if

            distancia = self.calcularDistancia(A, cajacercana)
            # print("A: ",A)
            # print("C: ",C)
            # print("D---",distancia)
            # print("iteracion")
        # end while

        # print("End while")

    def posicionarJugador(self,cajacercana, metacerca):
         if(self.direccion == True):
            dir = metacerca[0]-cajacercana[0]
            print("xxxxxx ", dir)
         else:
            dir = cajacercana[1]-metacerca[1]
            print("xxxxxx ",dir)
         if(self.direccion == False and dir > 0):
            self.board.movimientos("SA")
            
    def decisionCamino(self, cajacercana, metacerca):
        if(self.direccion == True):
            dir = metacerca[0]-cajacercana[0]
            print("xxxxxx ",dir)
            return dir
        else:
            dir = cajacercana[1]-metacerca[1]
            print("xxxxxx ",dir)
            return dir
    def hacerMovimientos(self, movimientos,cajacercana):
        pos = self.board.playerpos
        if(self.direccion == True and movimientos > 0):
            for i in range(movimientos):
                posFinal = self.board.movimientos("D")
                self.board.Print()
                if self.board.playerpos==cajacercana:
                    cajacercana[0]=cajacercana[0]+1
                    if(pos == posFinal):
                        self.direccion = not(self.direccion)
                        return
            self.direccion = not(self.direccion)
            print("DDDDDDDDDDD")
        elif(self.direccion == True and movimientos < 0):
            for i in range(abs(movimientos)):
                posFinal = self.board.movimientos("A")
                self.board.Print()
                if self.board.playerpos==cajacercana:
                    cajacercana[0]=cajacercana[0]-1
                    if(pos == posFinal):
                        self.direccion = not(self.direccion)
                        return
            self.direccion = not(self.direccion)
            print("AAAAAAAAAAAAAA")
        elif(self.direccion == False and movimientos > 0):
            for i in range(movimientos):
                print("ENTRO''''''''''''''")
                posFinal = self.board.movimientos("W")
                self.board.Print()
                if self.board.playerpos==cajacercana:
                    cajacercana[1]=cajacercana[1]-1
                    if(pos == posFinal):
                        self.direccion = not(self.direccion)
                        return
            self.direccion = not(self.direccion)
           
        elif(self.direccion == False and movimientos < 0):
            for i in range(abs(movimientos)):
                posFinal = self.board.movimientos("S")
                self.board.Print()
                if self.board.playerpos==cajacercana:
                    cajacercana[1]=cajacercana[1]+1         
                    if(pos == posFinal):
                        self.direccion = not(self.direccion)
                        return
            self.direccion = not(self.direccion)

x = Jugador()
x.jugar()
        
