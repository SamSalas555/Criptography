import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Protocol.KDF import PBKDF2
import hashlib
import os
# Variables globales
opcion_var = None
entrada_contraseña = None
entrada_ruta = None

def obtener_clave_des_desde_contraseña(contraseña):
    # Genera una clave segura a partir de la contraseña del usuario utilizando PBKDF2
    sal = b'valor_de_sal'  # Debes usar una sal aleatoria
    clave = PBKDF2(contraseña.encode('utf-8'), sal, dkLen=8, count=1000000, prf=lambda p, s: hashlib.sha256(s + p).digest())
    return clave

def completar_mensaje(mensaje):
    relleno = b' ' * (8 - (len(mensaje) % 8))
    return mensaje + relleno

def seleccionar_archivo():
    global entrada_ruta
    ruta_archivo = fd.askopenfilename(
        title='Abrir un archivo',
        initialdir='/',
        filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')]
    )
    if ruta_archivo:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta_archivo)

def realizar_accion():
    global opcion_var, entrada_contraseña, entrada_ruta
    accion = opcion_var.get()
    ruta_archivo = entrada_ruta.get()
    contraseña = entrada_contraseña.get()

    if not ruta_archivo:
        messagebox.showerror("Error", "Por favor, selecciona un archivo.")
        return

    if not contraseña:
        messagebox.showerror("Error", "Por favor, ingresa una contraseña.")
        return

    clave = obtener_clave_des_desde_contraseña(contraseña)
    cifrador = DES.new(clave, DES.MODE_ECB)

    try:
        with open(ruta_archivo, 'rb') as archivo:
            datos = archivo.read()

        # Obtener la extensión del archivo original
        nombre_base, extension = os.path.splitext(ruta_archivo)

        if accion == 1:  # Cifrados
            datos_cifrados = cifrador.encrypt(completar_mensaje(datos))
            nueva_ruta_archivo = nombre_base + "_c" + extension  # Agregar _c antes de la extensión
            with open(nueva_ruta_archivo, 'wb') as archivo:
                archivo.write(datos_cifrados)
            messagebox.showinfo("Éxito", "Archivo cifrado exitosamente.")
        elif accion == 2:  # Decifrar
            datos_decifrados = cifrador.decrypt(datos)
            nueva_ruta_archivo = nombre_base + "_d" + extension  # Agregar _d antes de la extensión
            with open(nueva_ruta_archivo, 'wb') as archivo:
                archivo.write(datos_decifrados)
            messagebox.showinfo("Éxito", "Archivo decifrado exitosamente.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    global opcion_var, entrada_contraseña, entrada_ruta

    window = tk.Tk()
    window.title("Práctica 1: Criptografía")
    window.config(padx=50, pady=50, background="#E1FFEE")

    title_label = tk.Label(text="Práctica 1: Criptografía", font=("Arial", 24, "bold"), pady=20, background="#E1FFEE")
    title_label.grid(column=1, row=0, columnspan=2)

    opcion_var = tk.IntVar()  # Como StringVar pero en entero
    opcion_var.set(1)  # Establecer encriptación como opción predeterminada

    selec_accion = tk.Label(window, text="Seleccionar Acción:",font=("Arial", 12, "normal"), background="#E1FFEE")
    selec_accion.grid(column=1, row=1)
    tk.Radiobutton(window, text="Cifrar", font=("Arial", 12, "normal"), variable=opcion_var, value=1, background="#E1FFEE").grid(column=1, row=2, pady=7)
    tk.Radiobutton(window, text="Descifrar", font=("Arial", 12, "normal"), variable=opcion_var, value=2, background="#E1FFEE").grid(column=2, row=2, pady=7)

    tk.Label(window, text="Ingresar Contraseña:",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=3)
    entrada_contraseña = tk.Entry(window, show="*")
    entrada_contraseña.grid(column=2, row=3)

    tk.Label(window, text="Seleccionar Archivo:", font=("Arial", 12, "normal"),  background="#E1FFEE").grid(column=1, row=4)
    entrada_ruta = tk.Entry(window)
    entrada_ruta.grid(column=2, row=4)
    tk.Button(window, text="Explorar", font=("Arial", 10, "normal"), command=seleccionar_archivo).grid(column=1, columnspan= 3, row=5, pady=20)

    tk.Button(window, text="Realizar Acción", font=("Arial", 10, "normal"),  command=realizar_accion).grid(column=3, row=6)

    window.mainloop()

if __name__ == "__main__":
    main()
