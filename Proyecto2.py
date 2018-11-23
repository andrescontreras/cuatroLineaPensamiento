import Sokoban
import const
import math
import time

class Jugador:
    cajas = []
    metas = []
    direccion = True  # true -> horizontal ,false -> vertical
    board = []
    cont =0

    def jugar(self):
        arch = "Niveles/nivel1.txt"
        self.board = Sokoban.Board(arch)
        self.buscarCajasMetas()
        self.board.Print()
        while (len(self.cajas) != 0 and self.board.estadoJugador() != 0 and self.board.estadoJugador() != 2):
            cajacercana = self.getCajaCercana()
            metacerca = self.getMetaCercana(cajacercana)
            self.moverJugadorAcaja(cajacercana)
            while(self.cajas[cajacercana] !=  self.metas[metacerca]):
                time.sleep(2.0)
                movimientos = self.decisionCamino(self.cajas[cajacercana], self.metas[metacerca])

            

    
    def buscarCajasMetas(self):
        for i in range(len(self.board.Data) - 1):
            for j in range(len(self.board.Data[i]) - 1):
                if self.board.Data[i][j] == const.CAJA:
                    self.cajas.append([j, i])
                # end if
                if self.board.Data[i][j] == const.META:
                    self.metas.append([j, i])
                # end if
            # end for
        # end for
        print("C",self.cajas);
        print("M",self.metas)
        print("J",self.board.getPlayerPos())
        self.board.Print()

    def getCajaCercana(self):
        cajacercana = []
        min_d = 100000
        for i in range(len(self.cajas)):
            dis = self.calcularDistancia(
                self.cajas[i], self.board.getPlayerPos())
            if dis < min_d:
                min_d = dis
                cajacercana = i
            # end if
            # end for
        return cajacercana

    def getMetaCercana(self, cajacercana):
        min_d = 100000
        metacercana = []
        for i in range(len(self.metas)):
            dis = self.calcularDistancia(self.cajas[cajacercana], self.metas[i])
            if dis < min_d:
                min_d = dis
                metacercana = i
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

    def decisionCamino(self, cajacercana, metacerca):
        if(self.direccion == True):
            dir = metacerca[0]-cajacercana[0]
            return dir
        else:
            dir = cajacercana[1]-metacerca[1]
            return dir
    
    def posicionarJugador(self,cajacercana, metacerca):
        

    
    def moverJugadorAcaja(self,cajacercana):
        # Codigo para mover al jugador hacia la caja
        A = self.board.getPlayerPos()

        distancia = self.calcularDistancia(A, self.cajas[cajacercana])
        # print("distancia",distancia)
        while (distancia > 1.0):
        #    print("J: ",J)#Jugador
        #    print("C: ",C)#Caja
            time.sleep(2.0)
            self.board.Print()
            y = cajacercana[1] - A[1]
            x = cajacercana[0] - A[0]
        #    print( abs(x) , abs(y) )
            if abs(x) > abs(y):  # Si se mueve en x
        #        print("J-",J)
                if x < 0:  # Derecha
        #            print("J-",A)
                    self.board.movimientos("A")
        #           print("J-",A)
                    P = self.board.playerpos
                    aux2=[0,0]
                    aux2[0] = P[1]
                    aux2[1] = P[0]
                    P = aux2

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

x = Jugador()
x.jugar()
