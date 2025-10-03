import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    
    cadena = cadena.lower()
    cadena = cadena.strip()
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    cadena = cadena.replace("ü", "u")
    cadena = cadena.replace("Á", "a")
    cadena = cadena.replace("É", "e")
    cadena = cadena.replace("Í", "i")
    cadena = cadena.replace("Ó", "o")
    cadena = cadena.replace("Ú", "u")
    cadena = cadena.replace("Ü", "u")
    return cadena

def ocultar(palabra_secreta, letras_usadas=""):
    resultado = ""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    if "_" in palabra_enmascarada:
        return False
    else:
        return True
    


# TODO: Implementa la función mostrar_estado
def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    
    print("Estado: ",palabra_enmascarada)
    if letras_usadas == "":
        print("Letras usadas: Ninguna")
    else:
        print("Letras usadas: ", letras_usadas)
    
    print("Intentos restantes: ", intentos_restantes)


# TODO: Implementa la función pedir_letra
def pedir_letra(letras_usadas):
     while True:
        letra = input("Introduce una letra: ")
        if len(letra) !=1:
            print("Introduce una sola letra")
        elif letra in letras_usadas:
            print("Ya has usado esa letra")
        else:
            return letra
# TODO: Implementa la función jugar
def jugar(palabra_secreta, intentos_maximos=6):

    palabra_secreta = normalizar(palabra_secreta)
    if palabra_secreta == "":
        return None
    
    palabra_enmascarada = ocultar(palabra_secreta)
    intentos_restantes = intentos_maximos
    letras_usadas = ""

    # Bucle principal
    while intentos_restantes > 0 and not ha_ganado(palabra_enmascarada):
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes)

        letra = pedir_letra(letras_usadas)
        letras_usadas += letra

        if letra in palabra_secreta:
            print("La letra se encuentra en la palabra")
            palabra_enmascarada = ocultar(palabra_secreta, letras_usadas)
        else:
            print("La letra no está en la palabra")
            intentos_restantes -= 1

    if ha_ganado(palabra_enmascarada):
        print("¡Has ganado! La palabra era:", palabra_secreta)
    else:
        print("Has perdido... La palabra era:", palabra_secreta)
                
# TODO: Escribe el programa principal
palabra = elige_palabra()
jugar(palabra)