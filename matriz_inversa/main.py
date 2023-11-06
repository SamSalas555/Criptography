from tkinter import *
import numpy as np


tam_matriz = 0
matriz_inicial= []
matriz_res=[]

window = Tk()
window.title("Calculadora de Matrices")
window.minsize(width=300, height=400)
window.config(bg='DarkSeaGreen1', pady=30, padx=10)

title_label = Label(text="Calculadora de Matrices", font=("MS Sans Serif", 16, "bold"))
title_label.grid(column=0, row=0, columnspan=3)
title_label.config(bg='DarkSeaGreen1', pady=15)



def matriz():
    global tam_matriz, matriz_inicial
    if radio_state.get() == 2:
        tam_matriz = 2
    elif radio_state.get() == 3:
        tam_matriz = 3
    else:
        tam_matriz = 4

    for i in range(tam_matriz):
        fila = []
        for j in range(tam_matriz):
            entrada = Entry(width=7)
            entrada.grid(column=j, row=i + 4)
            fila.append(entrada)
        matriz_inicial.append(fila)

def crear_matriz_valores():
    """Esta funcion sirve para guardar/almacenar los valores enteros que el usuario ingresó en la GUI en una matriz"""
    global matriz_inicial, tam_matriz
    matriz_valores = []
    for i in range(tam_matriz):
        fila = []
        for j in range(tam_matriz):
            fila.append(int(matriz_inicial[i][j].get()))
        matriz_valores.append(fila)
    return matriz_valores

def calcular_determinante():
    matriz_valores = np.array(crear_matriz_valores())
    determinante = round(np.linalg.det(matriz_valores))
    modulo = int(modulo_entry.get())
    if 0 < determinante <= modulo:
        return determinante
    else:
        determinante = determinante%modulo
        return determinante

def mcd(modulo, determinante):
    while determinante:
        modulo, determinante = determinante, modulo % determinante
    return modulo

def existe_inversa_matriz(det, modulo):
    return mcd(modulo, det) == 1

def euclides_extendido(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = euclides_extendido(b, a % b)
        return (y, x - (a // b) * y)

def encontrar_inverso_multiplicativo_determinante():
    determinante = calcular_determinante()
    modulo = int(modulo_entry.get())
    x, y = euclides_extendido(determinante, modulo)
    if x < 0:
        x += modulo
    if mcd(determinante, modulo) == 1:
        return x



def matriz_inversa():

    inverso_mult_determinante = encontrar_inverso_multiplicativo_determinante()
    matriz_val = crear_matriz_valores()
    #Matriz Adjunta
    cofactores = np.zeros_like(matriz_val, dtype=float)
    for i in range(tam_matriz):
        for j in range(tam_matriz):
            sub_matrix = np.delete(np.delete(matriz_val, i, axis=0), j, axis=1)
            cofactor = (-1) ** (i + j) * np.linalg.det(sub_matrix)
            cofactores[i, j] = (cofactor * inverso_mult_determinante) % int(modulo_entry.get())
    #Matriz traspuesta
    adjunta = cofactores.T
    return adjunta
    # matrizFinal_entry.insert(0, adjunta)
    # print(adjunta)


#TODO: Debemos de sacar el inverso multiplicativo de 1/modulo y luego multiplicar ese valor por cada cofactor para despues sacarle el módulo

def matriz_final():
    global tam_matriz, matriz_res
    if radio_state.get() == 2:
        tam_matriz = 2
    elif radio_state.get() == 3:
        tam_matriz = 3
    else:
        tam_matriz = 4

    matrizFinal_label = Label(text="Matriz inversa:", font=("MS Sans Serif", 14))
    matrizFinal_label.config(bg='DarkSeaGreen1', pady=14)
    matrizFinal_label.grid(column=0, row=14)
    matriz_res = matriz_inversa()
    for i in range(tam_matriz):
        fila = []
        for j in range(tam_matriz):
            entrada = Entry(width=7)
            entrada.grid(column=j, row=i + 15)
            entrada.insert(0, str(round(matriz_res[i][j])))
            fila.append(entrada)
        matriz_inicial.append(fila)


red_label = Label(text="m (2, 3 o 4):", font=("MS Sans Serif", 12))
red_label.config(bg='DarkSeaGreen1', pady=10)
red_label.grid(column=0, row=3)
radio_state = IntVar()
radiobutton2 = Radiobutton(text="2", bg='DarkSeaGreen1', value=2, variable=radio_state, command=matriz)
radiobutton3 = Radiobutton(text="3", bg='DarkSeaGreen1', value=3, variable=radio_state, command=matriz)
radiobutton4 = Radiobutton(text="4", bg='DarkSeaGreen1', value=4, variable=radio_state, command=matriz)
radiobutton2.grid(column=1, row=3)
radiobutton3.grid(column=2, row=3)
radiobutton4.grid(column=3, row=3)



modulo_label = Label(text="Modulo:",  font=("MS Sans Serif", 12))
modulo_label.config(bg='DarkSeaGreen1', pady=10)
modulo_label.grid(column=0, row=10)
modulo_entry = Entry(width=15)
modulo_entry.grid(column=1, row=10)


calcular_inversa = Button(text="Calcular", command=matriz_final)
calcular_inversa.grid(column=0, row=12)



window.mainloop()







