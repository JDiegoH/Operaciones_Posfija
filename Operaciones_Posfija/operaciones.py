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

def abrir_archivo():

    archivo = open("taller01/operaciones.txt","r")
    return archivo

def cerrar_archivo(archivo):

    archivo.close()

def leer_archivo(archivo):
    
    lista = archivo.readlines()
    
    for i in range(len(lista)):
        
        lista[i] = lista[i].replace('\n','')
    
    return(lista)

'''expresion = Nodo('-', Nodo('+', Nodo('-', Nodo(10), Nodo(5)), Nodo('*', Nodo(2), Nodo(3))), Nodo('/', Nodo(5), Nodo(2)))

expresion1 = Nodo(1,2) 

print(en_orden(expresion) + " = " + str(evaluar(expresion)))'''

archivo = abrir_archivo()

lista = leer_archivo(archivo)

pila = []

for i in lista[0]:
    
    for j in i:
        
        if j != " ":
            
            pila.append(j)

print(pila)

raiz = pila.pop()

expresion = Nodo(raiz)

while len(pila) != 0:
    
    if pila[len(pila)-1].isnumeric():
        
        expresion.izquierda = pila.pop()
        
    else:
        
        expresion.derecha = Nodo(pila.pop())

print(en_orden(expresion))

archivo.close()

































