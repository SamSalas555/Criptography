from Crypto.Cipher import  AES
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image
import sys

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
    if not ruta_archivo or not contraseña:
        tk.messagebox.showerror("Error", "Por favor, ingrese la ruta del archivo y la contraseña.")
        return

    try:
        #TODO: Quitar el vector de inicio en la funcion que no corresponde, se recomienda un IF
        iv = b'0123456789012345'  # Vector de inicialización fijo para AES (debe tener 16 bytes)
        cipher = AES.new(contraseña.encode(), modo,iv)
        datos = colors_to_bytes(ruta_archivo)
        datos_cifrados = cipher.encrypt(agregar_relleno(datos))
        img_salida = bytes_to_image(datos_cifrados)
        print("M3q")
        #TODO: Quitar mensajes de debugging y corregir nombre de los archivos para que tengan la extencion correcta
        img_salida.save("img_c.bmp")

        tk.messagebox.showinfo("Éxito", "El archivo se cifró correctamente.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Ocurrió un error al cifrar el archivo: {str(e)}")

def decifrar_archivo():
    global entrada_ruta, entrada_contraseña, modo_encrypt
    
    ruta_archivo = entrada_ruta.get()
    contraseña = entrada_contraseña.get()
    modo = cipher_modes[modo_encrypt.get()]
    if not ruta_archivo or not contraseña:
        tk.messagebox.showerror("Error", "Por favor, ingrese la ruta del archivo y la contraseña.")
        return

    try:
        #TODO: Quitar el vector de inicio en la funcion que no corresponde, se recomienda un IF
        iv = b'0123456789012345'  # Vector de inicialización fijo para AES (debe tener 16 bytes)
        cipher = AES.new(contraseña.encode(), modo,iv)
        datos = colors_to_bytes(ruta_archivo)
        datos_cifrados = cipher.decrypt(agregar_relleno(datos))
        img_salida = bytes_to_image(datos_cifrados)
        print("M3q")
        #TODO: Quitar mensajes de debugging y corregir nombre de los archivos para que tengan la extencion correcta
        img_salida.save("img_d.bmp")

        tk.messagebox.showinfo("Éxito", "El archivo se cifró correctamente.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Ocurrió un error al cifrar el archivo: {str(e)}")

def agregar_relleno(datos):
    tamaño_bloque = 16
    longitud_datos = len(datos)
    cantidad_relleno = tamaño_bloque - (longitud_datos % tamaño_bloque)
    relleno = bytes([0] * cantidad_relleno)
    datos_con_relleno = datos + relleno
    return datos_con_relleno


def colors_to_bytes(uri_image):
    byte_data = bytearray()
    img = Image.open(uri_image)
    ancho, alto = img.size
    pixeles = img.load()

    for x in range(ancho):
        for y in range(alto):
            color = pixeles[x, y]
            byte_data.append(color[0])
            byte_data.append(color[1])
            byte_data.append(color[2])
    return bytes(byte_data)


def bytes_to_image(data):
    width, height = 1152, 648
    img = Image.new("RGB", (width, height))
    pixels = img.load()
    index = 0
    print("Andamos aqui")
    for x in range(width):
        for y in range(height):
            if index + 2 < len(data):
                r = data[index]
                g = data[index + 1]
                b = data[index + 2]
                pixels[x, y] = (r, g, b)
                index += 3
    return img




def main():
    global opcion_var, entrada_contraseña, entrada_ruta, modo_encrypt

    window = tk.Tk()
    window.title("Práctica 3: Cifrador a Bloques")
    window.config(padx=50, pady=50, background="#E1FFEE")

    title_label = tk.Label(text="Práctica 3: Cifrador a Bloques", font=("Arial", 24, "bold"), pady=20, background="#E1FFEE")
    title_label.grid(column=1, row=0, columnspan=2)

    opcion_var = tk.IntVar()  # Como StringVar pero en entero
    opcion_var.set(1)  # Establecer encriptación como opción predeterminada
    #TODO: Usar el checkbox para determinar la operación

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

    tk.Button(window, text="Realizar Acción", font=("Arial", 10, "normal"),command=decifrar_archivo).grid(column=3, row=7)

    window.mainloop()

if __name__ == "__main__":
    main()


