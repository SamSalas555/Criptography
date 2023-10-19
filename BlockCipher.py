from Crypto.Cipher import  AES
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox


cipher_modes={
    1:AES.MODE_ECB,
    2:AES.MODE_CBC,
    3:AES.MODE_CFB,
    4:AES.MODE_OFB
}

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
    modo_encrypt = ttk.Combobox(window,values=["CBC","CBF","CFB","OFB"]).grid(column=2,row=4)
    
    tk.Label(window, text="Seleccionar Archivo:", font=("Arial", 12, "normal"),  background="#E1FFEE").grid(column=1, row=5)
    entrada_ruta = tk.Entry(window)
    entrada_ruta.grid(column=2, row=5)
    tk.Button(window, text="Explorar", font=("Arial", 10, "normal"),command=seleccionar_archivo).grid(column=1, columnspan= 3, row=6, pady=20)

    tk.Button(window, text="Realizar Acción", font=("Arial", 10, "normal")).grid(column=3, row=7)

    window.mainloop()

if __name__ == "__main__":
    main()
