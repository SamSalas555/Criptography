#Para usar este proyecto debe instalarse la libreria pycryptodome
#pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

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
