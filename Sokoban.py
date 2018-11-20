import const
import time
import random
class Board:
    
     ## Atributos  =========================================================
    Data = [[]]
    Width = 0
    Height = 0
    playerpos = [0,0]
    cajas = 0

    ## ---------------------------------------------------------------------
    #Funcion inicial que lee el archivo
    ## Fin atributos ====================================================================

    ## Inicio Contructor ===============================================================
    def __init__( self, arch ):
         print(const.CAJA)
         with open(arch) as f:
            lines = f.readlines()
            self.Width = int(lines[0])
            self.Height = int(lines[1])
            self.llenarMatriz(lines)    
         f.close()
         print("Width: ",self.Width)
         print("Height: ",self.Height)
         print("jugador: ", self.playerpos)
         #print("tabla")
         #print(self.Data)
    ## FIN Contructor ==================================================================

    #Funcion que llena la matriz con el flujo que le llega del archivo

    ## Inicio llenarMatriz ==============================================================
    def llenarMatriz(self,lines):
        print("W: ",self.Width, "H: ",self.Height)
        self.Data = [ [ (0) for j in range(self.Height)] for i in range(self.Width) ]
        for i in range (2,self.Height+2):
            for j in range (0,self.Width):
                self.Data[i-2][j] = lines[i][j]
                if(self.Data[i-2][j] == const.JUGADOR or self.Data[i-2][j] == const.JUGADORM):
                    self.playerpos = [i-2,j]
                if (self.Data[i-2][j] == const.CAJA or self.Data[i-2][j] == const.CAJAM):
                    self.cajas = self.cajas + 1
    #Funcion de movimiento individual. 
    #Entradas: Comando {W,A,S,D}
    #Salidas: La posicion del jugador en el tablero
    ## Fin llenarMatriz ===============================================================

    ## Inicio movimientos ==============================================================
    def movimientos (self,cadena):
        if len( cadena ) == 1:
            self.mover(cadena)
        else:
            for c in range (0, len( cadena ) ):
                self.mover(cadena[c])
                self.Print()
                time.sleep(0.2)
        return self.playerpos
    ## Fin movimientos =================================================================

    ## Inicio cajaBloqueda ===========================================================
    def cajaBloqueada (self,posx,posy):
        if(self.bloqueoPared(posx,posy) == 0):
            return 0
        if(self.cajasbloq(posx,posy) == 0):
            return 0
        if(self.cuatrocajas(posx,posy) == 0):
            return 0
        return 1
    ## Fin cajaBloqueda ===========================================================

    
    def bloqueoPared(self,posx,posy):
        if((self.Data[posx -1][posy] == const.MURO and (
        self.Data[posx][posy + 1] == const.MURO or
        self.Data[posx][posy - 1] == const.MURO 
        )) or
        (self.Data[posx +1][posy] == const.MURO and (
        self.Data[posx][posy + 1] == const.MURO or
        self.Data[posx][posy - 1] == const.MURO))):
            return 0
        return 1

    

    ## cajasbloq ====================================================================
    #revisa si hay dos cajas juntas junto a paredes
    def cajasbloq(self,posx,posy):
        if((self.Data[posx][posy +1] == const.CAJA or self.Data[posx][posy +1] == const.CAJAM) and (
           ( self.Data[posx -1][posy] == const.MURO and
            self.Data[posx-1][posy +1] == const.MURO )
            or
            (self.Data[posx +1][posy] == const.MURO and
             self.Data[posx +1][ posy+1] == const.MURO ))):
            return 0
        if((self.Data[posx+1][posy] == const.CAJA or self.Data[posx+1][posy] == const.CAJAM ) and (
           ( self.Data[posx][posy-1] == const.MURO and
            self.Data[posx+1][posy -1] == const.MURO )
            or
            (self.Data[posx][posy+1] == const.MURO and
             self.Data[posx +1][ posy+1] == const.MURO ))):
            return 0
        return 1

    def cajasbloqM(self,posx,posy):
        if((self.Data[posx][posy +1] == const.CAJA) and (
           ( self.Data[posx -1][posy] == const.MURO and
            self.Data[posx-1][posy +1] == const.MURO )
            or
            (self.Data[posx +1][posy] == const.MURO and
             self.Data[posx +1][ posy+1] == const.MURO ))):
            return 0
        if((self.Data[posx+1][posy] == const.CAJA ) and (
           ( self.Data[posx][posy-1] == const.MURO and
            self.Data[posx+1][posy -1] == const.MURO )
            or
            (self.Data[posx][posy+1] == const.MURO and
             self.Data[posx +1][ posy+1] == const.MURO ))):
            return 0
        return 1

    def cuatrocajas(self,posx,posy):
        if(self.Data[posx +1][posy] == const.CAJA and
            self.Data[posx][posy+1] == const.CAJA and
            self.Data[posx +1][posy +1] == const.CAJA):
            return 0
        return 1
        

    ## Inicio estadodeljudagor ====================================================
    def estadoJugador(self):
        cont = 0
        for filas in range (0, len(self.Data) - 1):
            for columnas in range (0, len(self.Data[0]) - 1 ):
                if self.Data[filas][columnas] == const.CAJAM:
                    cont = cont + 1
                    if(self.cajasbloqM(filas,columnas) == 0):
                        return 0
                if self.Data[filas][columnas] == const.CAJA:
                    if (self.cajaBloqueada(filas,columnas) == 0):
                        return 0
                
        if cont == self.cajas:
            return 2
        else: 
            return 1
    ## Fin estadodeljudagor ====================================================

    ## Inicio print ==================================================================
    def Print (self):
        print('\n'.join(['  '.join([str(cell) for cell in row]) for row in self.Data]))
    ## Fin print =====================================================================

    ## Inicio jugadorAutomatico ======================================================
    def jugadorAutomatico(self):
        gano = -1
        movimientos = ["W","A","S","D"]
        while (gano != 0 and gano != 2):
            mov = movimientos[random.randint(0,3)]
            #print("Movimiento ",mov)
            ##mov = input()
            # crear funcion random para obtener una letra entre w,a,s,d
            # la letra obtenida se pasa a la funcion movimientos.
            self.movimientos(mov)
            print("====================================================================================")
            self.Print()
            gano = self.estadoJugador()
            time.sleep(0.3)
        print("GAME OVER")
        if gano == 0:
            print("YOU LOSE")
        else:
            if gano == 2:
                print("YOU WIN")

    ## Fin jugadorAutomatico =========================================================


    ## Inicio mover ==================================================================
    def mover (self,direccion):
        if (direccion=='A'):
            #W
			#Avanzar Arriba
            if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                #Si la casilla actual es un jugador
                if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.LIBRE):
                    # Y la siguiente casilla es libre
                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                    self.playerpos[1] = self.playerpos[1] - 1
                    return self.playerpos
                else: 
                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.META):
                        # Y la siguiente casilla es meta
                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                        self.playerpos[1] = self.playerpos[1] - 1
                        return self.playerpos
                    else:
                        if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJA):
                            #Y la siguiente es una caja
                            if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                #Y la siguiente es un espacio libre
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                self.playerpos[1] = self.playerpos[1] - 1
                                return self.playerpos
                            else:
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                    #Y la siguiente es una meta
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                    self.playerpos[1] = self.playerpos[1] - 1
                                    return self.playerpos
                                else:
                                    #No se puede mover
                                    return self.playerpos
                        else:
                            if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJAM):
                                # Y la siguiente es una caja sobre meta
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                    #Y la siguiente es un espacio libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                    self.playerpos[1] = self.playerpos[1] - 1
                                    return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                        #Y la siguiente es una meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                        self.playerpos[1] = self.playerpos[1] - 1
                                        return self.playerpos
                                    else:
                                        #No se puede mover
                                        return self.playerpos
            else:###############################
                if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                    #Si la casilla acutal es un jugador sobre la meta
                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.LIBRE):
                        # Y la siguiente casilla es libre
                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                        self.playerpos[1] = self.playerpos[1] - 1
                        return self.playerpos
                    else:
                        if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.META):
                            # Y la siguiente casilla es meta
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                            self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                            self.playerpos[1] = self.playerpos[1] - 1
                            return self.playerpos
                        else:
                            if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJA):
                                #Y la siguiente es una caja
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                    #Y la siguiente es un espacio libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                    self.playerpos[1] = self.playerpos[1] - 1
                                    return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                        #Y la siguiente es una meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                        self.playerpos[1] = self.playerpos[1] - 1
                                        return self.playerpos
                                    else:
                                        #No se puede mover
                                        return self.playerpos
                            else:
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJAM):
                                    # Y la siguiente es una caja sobre meta
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                        self.playerpos[1] = self.playerpos[1] - 1
                                        return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                            self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                            self.playerpos[1] = self.playerpos[1] - 1
                                            return self.playerpos
                                        else:
                                            #No se puede mover
                                            return self.playerpos
        else:
            if (direccion=='W'):
                #A
                #Avanzar Izquierda
                if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                    #Si la casilla actual es un jugador
                    if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.LIBRE):
                        # Y la siguiente casilla es libre
                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                        self.Data[self.playerpos[0]- 1 ][self.playerpos[1]] = const.JUGADOR
                        self.playerpos[0] = self.playerpos[0] - 1
                        return self.playerpos
                    else:
                        if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.META):
                            # Y la siguiente casilla es meta
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                            self.playerpos[0] = self.playerpos[0] - 1
                            return self.playerpos
                        else:
                            if (self.Data[self.playerpos[0]- 1][self.playerpos[1]] == const.CAJA):
                                #Y la siguiente es una caja
                                if (self.Data[self.playerpos[0]- 2][self.playerpos[1]] == const.LIBRE):
                                    #Y la siguiente es un espacio libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                    self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                    self.playerpos[0] = self.playerpos[0] - 1
                                    return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                        #Y la siguiente es una meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                        self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                        self.playerpos[0] = self.playerpos[0] - 1
                                        return self.playerpos
                                    else:
                                        #No se puede mover
                                        return self.playerpos
                            else:
                                if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.CAJAM):
                                    # Y la siguiente es una caja sobre meta
                                    if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                        self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                        self.playerpos[0] = self.playerpos[0] - 1
                                        return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                            self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                            self.playerpos[0] = self.playerpos[0] - 1
                                            return self.playerpos
                                        else:
                                            #No se puede mover
                                            return self.playerpos
                else:###############################
                    if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                        #Si la casilla acutal es un jugador sobre la meta
                        if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.LIBRE):
                            # Y la siguiente casilla es libre
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                            self.playerpos[0] = self.playerpos[0] - 1
                            return self.playerpos
                        else:
                            if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.META):
                                # Y la siguiente casilla es meta
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                self.playerpos[0] = self.playerpos[0] - 1
                                return self.playerpos
                            else:
                                if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.CAJA):
                                    #Y la siguiente es una caja
                                    if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                        self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                        self.playerpos[0] = self.playerpos[0] - 1
                                        return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                            self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                            self.playerpos[0] = self.playerpos[0] - 1
                                            return self.playerpos
                                        else:
                                            #No se puede mover
                                            return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.CAJAM):
                                        # Y la siguiente es una caja sobre meta
                                        if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                            self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                            self.playerpos[0] = self.playerpos[0] - 1
                                            return self.playerpos
                                        else:
                                            if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                                self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                                self.playerpos[0] = self.playerpos[0] - 1
                                                return self.playerpos
                                            else:
                                                #No se puede mover
                                                return self.playerpos
            else:
                if (direccion=='D'):
                    #S
					#Avanzar Abajo
                    if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                        #Si la casilla actual es un jugador
                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.LIBRE):
                            # Y la siguiente casilla es libre
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                            self.playerpos[1] = self.playerpos[1] + 1
                            return self.playerpos
                        else:
                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.META):
                                # Y la siguiente casilla es meta
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                self.playerpos[1] = self.playerpos[1] + 1
                                return self.playerpos
                            else:
                                if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJA):
                                    #Y la siguiente es una caja
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                        self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                        self.playerpos[1] = self.playerpos[1] + 1
                                        return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                            self.playerpos[1] = self.playerpos[1] + 1
                                            return self.playerpos
                                        else:
                                            #No se puede mover
                                            return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJAM):
                                        # Y la siguiente es una caja sobre meta
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                            self.playerpos[1] = self.playerpos[1] + 1
                                            return self.playerpos
                                        else:
                                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                                self.playerpos[1] = self.playerpos[1] + 1
                                                return self.playerpos
                                            else:
                                                #No se puede mover
                                                return self.playerpos
                    else:###############################
                        if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                            #Si la casilla acutal es un jugador sobre la meta
                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.LIBRE):
                                # Y la siguiente casilla es libre
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                self.playerpos[1] = self.playerpos[1] + 1
                                return self.playerpos
                            else: 
                                if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.META):
                                    # Y la siguiente casilla es meta
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                    self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                    self.playerpos[1] = self.playerpos[1] + 1
                                    return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJA):
                                        #Y la siguiente es una caja
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                            self.playerpos[1] = self.playerpos[1] + 1
                                            return self.playerpos
                                        else:
                                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                                self.playerpos[1] = self.playerpos[1] + 1
                                                return self.playerpos
                                            else:
                                                #No se puede mover
                                                return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJAM):
                                            # Y la siguiente es una caja sobre meta
                                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                                #Y la siguiente es un espacio libre
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                                self.playerpos[1] = self.playerpos[1] + 1
                                                return self.playerpos
                                            else:
                                                if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                                    #Y la siguiente es una meta
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                    self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                                    self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                                    self.playerpos[1] = self.playerpos[1] + 1
                                                    return self.playerpos
                                                else:
                                                    #No se puede mover
                                                    return self.playerpos
                else:
                    if (direccion=='S'):
                        #D
						#Avanzar Derecha
                        if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                            #Si la casilla actual es un jugador
                            if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.LIBRE):
                                # Y la siguiente casilla es libre
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                self.Data[self.playerpos[0]+ 1 ][self.playerpos[1]] = const.JUGADOR
                                self.playerpos[0] = self.playerpos[0] + 1
                                return self.playerpos
                            else:
                                if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.META):
                                    # Y la siguiente casilla es meta
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                    self.playerpos[0] = self.playerpos[0] + 1
                                    return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0]+ 1][self.playerpos[1]] == const.CAJA):
                                        #Y la siguiente es una caja
                                        if (self.Data[self.playerpos[0]+ 2][self.playerpos[1]] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                            self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                            self.playerpos[0] = self.playerpos[0] + 1
                                            return self.playerpos
                                        else:
                                            if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                                self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                self.playerpos[0] = self.playerpos[0] + 1
                                                return self.playerpos
                                            else:
                                                #No se puede mover
                                                return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.CAJAM):
                                            # Y la siguiente es una caja sobre meta
                                            if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.LIBRE):
                                                #Y la siguiente es un espacio libre
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                                self.playerpos[0] = self.playerpos[0] + 1
                                                return self.playerpos
                                            else:
                                                if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                    #Y la siguiente es una meta
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                    self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                    self.playerpos[0] = self.playerpos[0] + 1
                                                    return self.playerpos
                                                else:
                                                    #No se puede mover
                                                    return self.playerpos
                        else:###############################
                            if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                                #Si la casilla acutal es un jugador sobre la meta
                                if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.LIBRE):
                                    # Y la siguiente casilla es libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                    self.playerpos[0] = self.playerpos[0] + 1
                                    return self.playerpos
                                else:
                                    if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.META):
                                        # Y la siguiente casilla es meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                        self.playerpos[0] = self.playerpos[0] + 1
                                        return self.playerpos
                                    else:
                                        if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.CAJA):
                                            #Y la siguiente es una caja
                                            if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.LIBRE):
                                                #Y la siguiente es un espacio libre
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                                self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                                self.playerpos[0] = self.playerpos[0] + 1
                                                return self.playerpos
                                            else:
                                                if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                    #Y la siguiente es una meta
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                                    self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                    self.playerpos[0] = self.playerpos[0] + 1
                                                    return self.playerpos
                                                else:
                                                    #No se puede mover
                                                    return self.playerpos
                                        else:
                                            if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.CAJAM):
                                                # Y la siguiente es una caja sobre meta
                                                if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.LIBRE):
                                                    #Y la siguiente es un espacio libre
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                    self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                                    self.playerpos[0] = self.playerpos[0] + 1
                                                    return self.playerpos
                                                else:
                                                    if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                        #Y la siguiente es una meta
                                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                        self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                        self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                        self.playerpos[0] = self.playerpos[0] + 1
                                                        return self.playerpos
                                                    else:
                                                        #No se puede mover
                                                        return self.playerpos
    ## Fin mover ==================================================================
