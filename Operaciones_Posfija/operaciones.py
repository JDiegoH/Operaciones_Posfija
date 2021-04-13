from io import *

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return ''
    elif arbol.valor in ['+', '-', '*', '/']:
        return "(" + en_orden(arbol.izquierda) + str(arbol.valor) + en_orden(arbol.derecha) + ")"
    else:
        return str(arbol.valor)

def evaluar(arbol):
    if arbol == None:
        pass
    else:
        if arbol.valor == '+':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        if arbol.valor == '-':
            return evaluar(arbol.izquierda) - evaluar(arbol.derecha)
        if arbol.valor == '*':
            return evaluar(arbol.izquierda) * evaluar(arbol.derecha)
        if arbol.valor == '/':
            return evaluar(arbol.izquierda) // evaluar(arbol.derecha)
        return int(arbol.valor)

def abrir_archivo(titulo):

    archivo = open(titulo,"r")
    return archivo

def escribir_archivo(titulo):

    archivo = open(titulo,"w")
    return archivo

def leer_archivo(archivo):
    
    lista = archivo.readlines()
    
    for i in range(len(lista)):
        
        lista[i] = lista[i].replace('\n','')
    
    return(lista)

def meter_arbol(expresion, pila):

    while len(pila) > 0:

        if pila[-1].isnumeric():

            if expresion.derecha is None:
                expresion.derecha = Nodo(pila.pop())
                meter_arbol(expresion, pila)

            elif expresion.izquierda is None:
                expresion.izquierda = Nodo(pila.pop())
                meter_arbol(expresion, pila)

            else: 
                break
            
        else:
            if expresion.derecha is None:

                expresion.derecha = Nodo(pila.pop())
                meter_arbol(expresion.derecha, pila)

            elif expresion.izquierda is None:

                expresion.izquierda = Nodo(pila.pop())
                meter_arbol(expresion.izquierda, pila)
            
            else: 
                break

archivo = abrir_archivo("taller01/operaciones.txt")

lista = leer_archivo(archivo)

archivo.close()

resultados = escribir_archivo("taller01/resultados.txt")

while len(lista) > 0:

    pila = []

    for i in lista.pop():
    
        for j in i: 
        
            if j != " ":
            
                pila.append(j)

    raiz = pila.pop()

    expresion = Nodo(raiz)

    meter_arbol(expresion, pila)

    resultados.write(en_orden(expresion) + " = " + str(evaluar(expresion))+"\n")


resultados.close()