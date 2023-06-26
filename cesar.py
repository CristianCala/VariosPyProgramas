posicion = 3

texto = "HOLA AMIGO"

dato_cifrado = ""

for c in texto:

    if c.isupper():
        c_unicode = ord(c)
        indice = ord(c) - ord("A")
        nueva_pos = (indice + posicion) % 26
        nuevo_unicode = nueva_pos + ord("A")
        nuevo_caracter = chr(nuevo_unicode)
        dato_cifrado = dato_cifrado + nuevo_caracter
    else:

        dato_cifrado += c

print("Texto:",texto)

print("Texto Encriptado:",dato_cifrado)
