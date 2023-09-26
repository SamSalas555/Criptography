# Para interfaz grafica
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
#Para usar este proyecto debe instalarse la libreria pycryptodome
#pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

data = []
# Clave de 8 bytes para DES (debe ser secreta)
llave_usuario = get_random_bytes(8)
llave_usuario = b'g<=\xfd=\xf7\x8b\xf0'

# Función para rellenar el mensaje para que sea múltiplo de 8 bytes
def pad_message(message):
    padding = b' ' * (8 - (len(message) % 8))
    return message + padding

# Función para cifrar un mensaje utilizando DES
def encrypt_message(key, message):
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_message = cipher.encrypt(pad_message(message))
    return encrypted_message

# Función para descifrar un mensaje cifrado utilizando DES
def decrypt_message(key, encrypted_message):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.rstrip(b' ')

# Clave de 8 bytes para DES (debe ser secreta)
key = get_random_bytes(8)

# Mensaje que deseas cifrar
mensaje_original = "Hola, este es un mensaje secreto."

# Cifrar el mensaje
mensaje_cifrado = encrypt_message(key, mensaje_original.encode('utf-8'))
print("Mensaje cifrado:", mensaje_cifrado)

# Descifrar el mensaje
mensaje_descifrado = decrypt_message(key, mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado.decode('utf-8'))

def select_file():
    """data[2] = ruta absoluta del archivo"""
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    # ABSOLUTE PATH
    # data[2]
    data.append(filename)
    messagebox.showinfo(title="Notificacion", message="Su archivo ha sido seleccionado")
    print(filename)

def cifrar(llave, direccion_archivo):
    with open(direccion_archivo) as archivo:
        mensaje_original = archivo.read()

    # Cifrar el mensaje
    texto_cifrado = encrypt_message(llave, mensaje_original.encode('utf-8'))
    # Cadena que sera nombre de nuevo archivo
    nombre_de_archivo_cifrado = "".join([char for char in direccion_archivo[:-4]])
    #se crea en directorio de archivo original
    with open(f"{nombre_de_archivo_cifrado}_c.txt", mode="wb") as file:
        # escribir texto cifrado en archivo nuevo
        file.write(texto_cifrado)

    print(texto_cifrado)
def decifrar(llave, direccion_archivo):
        with open(direccion_archivo, 'rb') as archivo:
            texto_cifrado = archivo.read()
        # TODO:LLAVE USUARIO
        # Desencriptar el mensaje
        texto_decifrado = decrypt_message(llave_usuario, texto_cifrado)

        # Nombre del archivo decifrado
        nombre_de_archivo_decifrado = "".join([char for char in direccion_archivo[:-4]])

        # Intentar decodificar los datos binarios como UTF-8
        texto_decodificado = texto_decifrado.decode('utf-8')

        # Crear un nuevo archivo con extensión .dec para almacenar el texto decifrado
        with open(f"{nombre_de_archivo_decifrado}_d.txt", mode="w") as file:
            file.write(texto_decodificado)

        print(texto_decodificado)

def accion():
    # data = opcion, filepath, llave
    data.append(int(llave.get()))  #data[2]
    #Radio Button = 1 cifrar
    if data[0] == 1:
        # data[2] -> llave, data[1] -> direccion de archivo(ruta absoluta)
        #TODO: LLAVE Usuario
        # cifrar(data[2], data[1])
        cifrar(llave_usuario, data[1])
        messagebox.showinfo(title="Notificacion", message=f"Su archivo ha sido cifrado.")

    #Radio Button = 2 decifrar
    else:
        #TODO: Llave Usuario
        # decifrar(data[2], data[1])
        decifrar(llave_usuario, data[1])
        messagebox.showinfo(title="Notificacion", message=f"Su archivo ha sido decifrado.")
    print(data)
    data.clear()
def selec():
    if len(data) <= 0:
        data.append(opcion.get())
        print(opcion.get())

window = Tk()
window.title("Practica 1: Criptografia")
window.config(padx=50, pady=50, background="#E1FFEE")

title_label = Label(text="Practica 1: Cryptografia", font=("Arial", 24, "bold"), pady=20, background="#E1FFEE")
title_label.grid(column=1, row=0, columnspan=2)


opcion = IntVar() # Como StrinVar pero en entero

Radiobutton(window, text="Cifrar", variable=opcion,
            value=1, command=selec, background="#E1FFEE").grid(column=0, row=2)
Radiobutton(window, text="Decifrar", variable=opcion,
            value=2, command=selec, background="#E1FFEE").grid(column=1, row=2)


llave_label = Label(text="Llave:", font=("Arial", 12, "normal"), background="#E1FFEE")
llave_entry = Entry()
llave_label.grid(column=1, row=3)

llave = Entry()
llave.grid(column=2, row=3, columnspan=2, pady=20)

open_button = Button(text="Selecciona un archivo", command=select_file, width=20)
open_button.grid(column=1, row=4, columnspan=3)


realizar_btn = Button(text="Realizar", command=accion, width=5)
realizar_btn.grid(column=2, row=5)


window.mainloop()