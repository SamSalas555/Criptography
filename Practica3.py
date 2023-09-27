# Grafic Interface libraries
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
#Cryptographic library used 
from Crypto.Cipher import DES
from Crypto.Protocol.KDF import PBKDF2
import hashlib


data = []
# Clave de 8 bytes para DES (debe ser secreta)
user_key = b'g<=\xfd=\xf7\x8b\xf0'


def get_key_from_string(string_key):
    # Convert string into bytes using a codec 
    string_bytes = string_key.encode('utf-8')
    
    # Use PBKDF2 to derivate a key from String
    derivated_key = PBKDF2(string_bytes, b'', dkLen=8, count=1000000, prf=lambda p, s: hashlib.sha256(s + p).digest())
    
    return derivated_key

# Function to fill the message to 8 bites size
def pad_message(message):
    padding = b' ' * (8 - (len(message) % 8))
    return message + padding

def select_file():
    """data[2] = ruta absoluta del data_file"""
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
    messagebox.showinfo(title="Notificacion", message="Su data_file ha sido seleccionado")
    print(filename)

def encrypt_des(key_des, file_d):
    #Read the file to encript
    with open(file_d) as data_file:
        message = data_file.read()
    cipher = DES.new(key_des, DES.MODE_ECB)
    encrypted_message = cipher.encrypt(pad_message(message.encode('utf-8')))
    # New file name
    nombre_de_archivo_cifrado = "".join([char for char in file_d[:-4]])
    #It gets created in the same directory as the original file
    with open(f"{nombre_de_archivo_cifrado}_c.txt", mode="wb") as file:
        # Write encrypted data into new file
        file.write(encrypted_message)
    print(encrypted_message)

def decrypt_des(key_des, file_d):
        with open(file_d, 'rb') as data_file:
            encrypted_message = data_file.read()
        cipher = DES.new(key_des, DES.MODE_ECB)
        decrypted_message = cipher.decrypt(encrypted_message)
        # Nombre del data_file decifrado
        nombre_de_archivo_decifrado = "".join([char for char in file_d[:-4]])
        # Intentar decodificar los datos binarios como UTF-8
        decoded_text = decrypted_message.decode('utf-8')
        # Crear un nuevo data_file con extensión .dec para almacenar el texto decifrado
        with open(f"{nombre_de_archivo_decifrado}_d.txt", mode="w") as file:
            file.write(decoded_text)
        print(decoded_text)

def accion():
    # data = opcion, filepath, key_des
    data.append(int(key_des.get()))  #data[2]
    #Radio Button = 1 encrypt_des
    if data[0] == 1:
        # data[2] -> key_des, data[1] -> direccion de data_file(ruta absoluta)
        #TODO: LLAVE Usuario
        # encrypt_des(data[2], data[1])
        encrypt_des(user_key, data[1])
        messagebox.showinfo(title="Notificacion", message=f"Su data_file ha sido cifrado.")

    #Radio Button = 2 decrypt_des
    else:
        #TODO: Llave Usuario
        # decrypt_des(data[2], data[1])
        decrypt_des(user_key, data[1])
        messagebox.showinfo(title="Notificacion", message=f"Su data_file ha sido decifrado.")
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

key_des = Entry()
key_des.grid(column=2, row=3, columnspan=2, pady=20)

open_button = Button(text="Selecciona un archivo", command=select_file, width=20)
open_button.grid(column=1, row=4, columnspan=3)


realizar_btn = Button(text="Realizar", command=accion, width=5)
realizar_btn.grid(column=2, row=5)


window.mainloop()