from Crypto.Cipher import  AES
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox


cipher_modes={
    "ECB":AES.MODE_ECB,
    "CBC":AES.MODE_CBC,
    "CFB":AES.MODE_CFB,
    "OFB":AES.MODE_OFB
}

def seleccionar_archivo():
    global entrada_ruta
    ruta_archivo = fd.askopenfilename(
        title='Abrir un archivo',
        initialdir='./',
        filetypes=[('Archivos de imagen', '*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tif;*.tiff'), ('Todos los archivos', '*.*')]
    )
    if ruta_archivo:
        entrada_ruta.delete(0, tk.END)
        entrada_ruta.insert(0, ruta_archivo)

def cifrar_archivo():
    global entrada_ruta, entrada_contraseña, modo_encrypt
    
    ruta_archivo = entrada_ruta.get()
    contraseña = entrada_contraseña.get()
    modo = cipher_modes[modo_encrypt.get()]
    print(modo)
    
    if not ruta_archivo or not contraseña:
        tk.messagebox.showerror("Error", "Por favor, ingrese la ruta del archivo y la contraseña.")
        return

    try:
        iv = b'0123456789012345'  # Vector de inicialización fijo para AES (debe tener 16 bytes)
        cipher = AES.new(contraseña.encode(), modo, iv)

        with open(ruta_archivo, 'rb') as archivo_entrada:
            datos = archivo_entrada.read()
            datos = agregar_relleno(datos)

        datos_cifrados = cipher.encrypt(datos)

        with open(ruta_archivo, 'wb') as archivo_salida:
            archivo_salida.write(datos_cifrados)

        tk.messagebox.showinfo("Éxito", "El archivo se cifró correctamente.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Ocurrió un error al cifrar el archivo: {str(e)}")

def agregar_relleno(datos):
    tamaño_bloque = 16
    longitud_datos = len(datos)
    cantidad_relleno = tamaño_bloque - (longitud_datos % tamaño_bloque)
    relleno = bytes([cantidad_relleno]) * cantidad_relleno
    datos_con_relleno = datos + relleno
    return datos_con_relleno



def main():
    global opcion_var, entrada_contraseña, entrada_ruta, modo_encrypt

    window = tk.Tk()
    window.title("Práctica 3: Cifrador a Bloques")
    window.config(padx=50, pady=50, background="#E1FFEE")

    title_label = tk.Label(text="Práctica 3: Cifrador a Bloques", font=("Arial", 24, "bold"), pady=20, background="#E1FFEE")
    title_label.grid(column=1, row=0, columnspan=2)

    opcion_var = tk.IntVar()  # Como StringVar pero en entero
    opcion_var.set(1)  # Establecer encriptación como opción predeterminada

    selec_accion = tk.Label(window, text="Seleccionar Acción:",font=("Arial", 12, "normal"), background="#E1FFEE")
    selec_accion.grid(column=1, row=1)
    tk.Radiobutton(window, text="Cifrar", font=("Arial", 12, "normal"), variable=opcion_var, value=1, background="#E1FFEE").grid(column=1, row=2, pady=7)
    tk.Radiobutton(window, text="Descifrar", font=("Arial", 12, "normal"), variable=opcion_var, value=2, background="#E1FFEE").grid(column=2, row=2, pady=7)

    tk.Label(window, text="Ingrese la llave",  font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1, row=3)
    entrada_contraseña = tk.Entry(window, show="*")
    entrada_contraseña.grid(column=2, row=3)
    tk.Label(window,text="Modo de cifrado", font=("Arial", 12, "normal"), background="#E1FFEE").grid(column=1,row=4) 
    modo_encrypt = ttk.Combobox(window,values=list(cipher_modes.keys()))
    modo_encrypt.grid(column=2,row=4)
    print(modo_encrypt.get())
    mode = modo_encrypt
    tk.Label(window, text="Seleccionar Archivo:", font=("Arial", 12, "normal"),  background="#E1FFEE").grid(column=1, row=5)
    entrada_ruta = tk.Entry(window)
    entrada_ruta.grid(column=2, row=5)
    tk.Button(window, text="Explorar", font=("Arial", 10, "normal"),command=seleccionar_archivo).grid(column=1, columnspan= 3, row=6, pady=20)

    tk.Button(window, text="Realizar Acción", font=("Arial", 10, "normal"),command=cifrar_archivo).grid(column=3, row=7)

    window.mainloop()

if __name__ == "__main__":
    main()
