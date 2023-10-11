import tkinter as tk
from tkinter import messagebox
def mcd(n, aplha):
    while aplha:
        n, aplha= aplha, n % aplha
    return n


def a_validar(alpha, n):
    return mcd(n, alpha) == 1

def is_beta_within_n(beta, n):
    if 0 < beta <= n:
        return True
    else:
        return False
def euclides_extendido(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = euclides_extendido(b, a % b)
        return (y, x - (a // b) * y)

def encontrar_inverso_multiplicativo(aplha, n):
    x, y = euclides_extendido(aplha, n)
    if x < 0:
        x += n
    if mcd(aplha, n) == 1:
        return x
    else:
        return print("El inverso mult no existe")

# def fcifrado():
#     salida_fcifrado.delete(0, tk.END)
#     n = int(entrada_n.get())
#     alpha = int(entrada_a.get())
#     b = int(entrada_b.get())
#     if a_validar(alpha, n):
#         salida_fcifrado.insert(0, f'c = {alpha} p + {b} mod {n}')
def fcifrado():
    salida_fcifrado.delete(0, tk.END)
    n = int(entrada_n.get())
    alpha = int(entrada_a.get())
    b = int(entrada_b.get())

    while not a_validar(alpha, n):
        # Muestra un mensaje de error y solicita al usuario ingresar un valor válido
        tk.messagebox.showerror("Error", "El valor de alpha no es válido. Debe ser coprimo con n.")
        # alpha = int(input("Ingrese un valor válido para alpha: "))  # Solicitar una nueva entrada
        entrada_a.delete(0,tk.END)
        alpha = int(entrada_a.get())
    salida_fcifrado.insert(0, f'c = {alpha} p + {b} mod {n}')


def fdescifrado1():
    salida_fdescifrado1.delete(0, tk.END)
    n = int(entrada_n.get())
    alpha = int(entrada_a.get())
    b = int(entrada_b.get())

    a_inv = encontrar_inverso_multiplicativo(alpha, n)
    b_inv_adit = n - b
    salida_fdescifrado1.insert(0, f'p = {a_inv} [ C + ({b_inv_adit})] mod {n}')

def funciones_cifrado_descifrado():
    fcifrado()
    fdescifrado1()



window = tk.Tk()
window.title("Práctica 2: AE y AEE")
window.config(padx=50, pady=50, background="#E1FFEE")

title_label = tk.Label(text="Práctica 2: AE y AEEE", font=("Arial", 24, "bold"), pady=20, background="#E1FFEE")
title_label.grid(column=1, row=0, columnspan=2)

tk.Label(window, text="Ingresar n:",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=3)
entrada_n = tk.Entry(window)
entrada_n.grid(column=2, row=3)

tk.Label(window, text="Ingresar a:",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=4)
entrada_a = tk.Entry(window)
entrada_a.grid(column=2, row=4)

tk.Label(window, text="Ingresar b:",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=5)
entrada_b = tk.Entry(window)
entrada_b.grid(column=2, row=5)

tk.Button(window, text="Realizar Acción", command=funciones_cifrado_descifrado, font=("Arial", 10, "normal")).grid(column=3, row=6)

tk.Label(window, text="Funcion Cifrado:",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=7)
salida_fcifrado = tk.Entry(window)
salida_fcifrado.grid(column=2, row=7)

tk.Label(window, text="Funciones de Descifrado:",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=8)
salida_fdescifrado1 = tk.Entry(window)
salida_fdescifrado1.grid(column=2, row=8)

salida_fdescifrado2 = tk.Entry(window)
salida_fdescifrado2.grid(column=2, row=9)



window.mainloop()
# def algoritmo_de_euclide(aplha, n):
#     pass
#
#

#
#     # validar si alpha tiene inverso multiplicativo es decir si existe alpha a la menos 1
#     # TODO: verificar que mcd de alpha y n son coprimos (algoritmo de euclides) , si son coprimos existe alpha
#     # TODO: si son coprimos hacer el algoritmo extendido de euclides para encontrar alpha a la menos 1 (inverso mult)

#

#
#
#
#
# print(encontrar_inverso_multiplicativo(3,30))
