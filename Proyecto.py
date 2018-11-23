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
        arch = "Niveles/nivel2.txt"
        self.board = Sokoban.Board(arch)
        Jugador.tablero = self.board.Data
        self.buscarCajasMetas()
        while (len(self.cajas) != 0 and self.board.estadoJugador() != 0 and self.board.estadoJugador() != 2):
            cajacercana = self.getCajaCercana()
            metacerca = self.getMetaCercana(cajacercana)
            self.moverJugadorAcaja(cajacercana)
            self.posicionarJugador()
            while(cajacercana != metacerca):
                movimientos = self.decisionCamino(cajacercana, metacerca)
                self.hacerMovimientos(movimientos)
                self.cajas.remove(cajacercana)
                self.metas.remove(metacerca)



    def buscarCajasMetas(self):
        for i in range(len(self.tablero) - 1):
            for j in range(len(self.tablero[i]) - 1):
                if self.tablero[i][j] == const.CAJA:
                    self.cajas.append([i, j])
                # end if
                if self.tablero[i][j] == const.META:
                    self.metas.append([i, j])
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
        print("aaaa")

    def posicionarJugador(self):
        print("bbb")

    def moverCaja(self):
        print("bbb")

    def decisionCamino(self, cajacercana, metacerca):
        if(self.direccion == True):
            dir = metacerca[0]-cajacercana[0]
            return dir
        else:
            dir = cajacercana[1]-metacerca[1]
            return dir
    def hacerMovimientos(self, movimientos):
        pos = self.board.playerpos()
        if(self.direccion == True and movimientos > 0):
            for i in range(movimientos):
                posFinal = self.board.movimientos("D")
                if(pos == posFinal):
                    self.direccion = !self.direccion
                    return
            self.direccion = !self.direccion
        elif(self.direccion == True and movimientos < 0):
            for i in range(movimientos):
                posFinal = self.board.movimientos("A")
                if(pos == posFinal):
                    self.direccion = !self.direccion
                    return
            self.direccion = !self.direccion
        elif(self.direccion == False and movimientos > 0):
            for i in range(movimientos):
                posFinal = self.board.movimientos("W")
                if(pos == posFinal):
                    self.direccion = !self.direccion
                    return
            self.direccion = !self.direccion
        elif(self.direccion == False and movimientos < 0):
            for i in range(movimientos):
                posFinal = self.board.movimientos("S")
                if(pos == posFinal):
                    self.direccion = !self.direccion
                    return
            self.direccion = !self.direccion
        
