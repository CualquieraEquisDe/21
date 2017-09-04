#-------------------------------------------------------------------------------

from builtins import int
from array import array

# Name:        mazo

# Purpose:

#

# Author:      Sebastian Vargas

#

# Created:     28/08/2017

#-------------------------------------------------------------------------------


def main():

    pass


if __name__ == '__main__':

    main()


from random import*
import time
import sys


def crearMazo():
    return sample([(x, y) for x in ['A', 'J', 'Q', 'K'] + list(range(2, 11)) for y in ['picas', 'treboles', 'diamantes', 'corazones']], 52)


def repartir(mazo):
    jugar([mazo[0], mazo[1]], [mazo[2], mazo[3]], mazo[4:])


def jugar(jugador, computador, mazo):
    print("--------------------------------------------")
    print("Jugador:")
    mostrarCartas(jugador)
    print("Pc:")
    mostrarComputador(computador)
    print("Usted lleva ", acumulado(jugador, len(jugador)))
    if acumulado(jugador, len(jugador)) <= 21:
        print("Digite 1 para pedir una nueva carta")
        if int(input()) == 1:
            jugar(darCarta(jugador, mazo), computador, mazo[1:])
        else:
            print("El jugador se planta con ", acumulado(jugador, len(jugador)))        
    else:
        print("El jugador se paso de 21")
    time.sleep(2)    
    print("Turno del pc:")
    turnoPc(jugador, computador, mazo)


def darCarta(array, mazo):
    return array + [mazo[0]]


def acumulado(array, tamano):
    if az(array, len(array)) == 0:
        return suma(array, len(array))
    else:
        if az(array, len(array)) != 0:
            if suma(array, len(array)) <= 11:
                return 10 + suma(array, len(array))
            else:
                return suma(array, len(array))     
        
        
def suma(array, tamano):
    if tamano == 1:
        return cambio(array[tamano - 1][0])
    else:
        return cambio(array[tamano - 1][0]) + suma(array, tamano - 1) 
        # return int(array[tamano - 1][0]) + suma(array, tamano - 1)


def cambio(carta):
    if carta == 'K' or carta == 'Q' or carta == 'J':
        return 10
    if carta == 'A':
        return 1
    else:
        return(carta)
    
def az(array , tamano):
    
    if tamano  == 1:
        if array[tamano - 1][0] == 'A':
            return 1
        else: 
            return 0 
    else :
        if array[tamano - 1][0] == 'A':
            return 1 + az(array, tamano - 1)
        else:
            return az(array, tamano - 1)
        

def mostrarCartas(array):
    print(array)


def mostrarComputador(array):

    print(array[0], "*******")
    print("--------------------------------------------")


def turnoPc(jugador, computador, mazo):
    print("--------------------------------------------")
    print("Jugador:")
    mostrarCartas(jugador)
    print("Computador:")
    mostrarCartas(computador)
    print("--------------------------------------------")
    print("Jugador: ", acumulado(jugador, len(jugador)))
    print("Computador: ", acumulado(computador, len(computador)))
    time.sleep(5)
    if acumulado(computador, len(computador)) < 18 and acumulado(computador, len(computador)) <= acumulado(jugador, len(jugador)) and acumulado(jugador, len(jugador)) <= 21:
        print("El pc pide una carta")
        turnoPc(jugador, darCarta(computador,mazo), mazo[1:])
    else:
        if acumulado(computador, len(computador)) <= 21:
            print("El pc se planta con ", acumulado(computador, len(computador)))
        else:
            print("El pc se paso de 21")
    
    ganador(jugador, computador)
    sys.exit()
        

def numeroRojas(array,tamano):
    if tamano == 0:
        return rojas(array, tamano)
    else:
        return rojas(array, tamano) + numeroRojas(array, tamano - 1)

    
def rojas(array,tamano):
    if tamano == 0:
        return 0
    else:
        if array[tamano - 1][1] == 'corazones' or  array[tamano - 1][1] == 'diamantes':
            return 1
        else:
            return 0    
    
def ganador(jugador, computador):
    print("---------------Resultado---------------")
    print("Jugador:")
    mostrarCartas(jugador)
    print("Pc:")
    mostrarCartas(computador)
    print("---------------------------------------")
    if acumulado(jugador, len(jugador)) == acumulado(computador, len(computador)) and (acumulado(jugador, len(jugador)) <= 21 and acumulado(computador, len(computador)) <= 21):
        empate(jugador,computador)
    else:
        if acumulado(jugador, len(jugador)) > acumulado(computador, len(computador)) and (acumulado(jugador, len(jugador)) <= 21 and acumulado(computador, len(computador)) <= 21) or acumulado(computador, len(computador)) > 21:
            print("El jugador ha ganado la partida con ", acumulado(jugador, len(jugador)))
        else:
            if acumulado(computador, len(computador)) <= 21:
                print("El Pc ha ganado la partida con ", acumulado(computador, len(computador)))
            else:
                print("Empate")                


def empate(jugador,computador):
    print("Numero de rojas jugador: ", numeroRojas(jugador, len(jugador)))
    print("Numero de rojas Pc: ", numeroRojas(computador, len(computador)))
    if numeroRojas(jugador, len(jugador)) == numeroRojas(computador, len(computador)):
        print("Empate")
    else:
        if numeroRojas(jugador, len(jugador)) > numeroRojas(computador, len(computador)):
            print("El jugador ha ganado la partida")
        else:
            print("El Pc ha ganado la partida")
        

#-------------------------------EJECUCION------------------------

repartir(crearMazo())
