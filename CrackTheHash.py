#Script para hacer fuerza bruta en local a un hash de contraseña
#Desarrollado por xXJuanDavidXx
#
import hashlib
import time
import argparse
from concurrent.futures import ThreadPoolExecutor
import os
import math
from pwn import log


print("""

⠐⡠⠀⢄⠠⠀⡄⠠⢀⠄⠠⡀⠄⢠⠀⠄⡠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⠠⠀⠄⢠⠀⠄⡠⠀⢄⠠⠀⡄⠠⢀⠄⠠⡀⠄⢠⠀⠄⠂
⠂⠄⡁⠂⠄⠡⢀⠁⠂⠌⡐⠠⠈⠄⡈⠐⠠⠁⠌⠠⠁⢌⣠⣁⣌⣤⣡⣌⣤⣥⣬⣤⣥⣬⣤⣥⣬⣄⣡⣌⣤⣁⣌⡠⠉⡐⠠⢈⠐⠠⢁⠂⠄⠡⢀⠁⠂⠌⡐⠠⠈⠄⡈⠄⡁
⡁⠂⠄⠡⢈⠐⠠⢈⠐⠄⠠⠁⠌⡐⠠⢁⣂⣥⠾⠒⠛⡉⠡⠀⠄⡀⠄⡀⠠⢀⠠⠀⠄⠠⠀⠄⡀⠠⢀⠠⠀⠄⡈⢉⠛⠒⠶⣤⣈⠐⠠⠈⠄⡁⠂⠌⡐⠠⢀⠡⢈⠐⡀⠂⠄
⠄⠡⢈⠐⠠⢈⠐⠠⠈⠄⠡⠘⠠⠐⣠⠞⡁⠠⠐⡈⠐⠠⠁⠌⡐⢀⠂⠄⡁⠂⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⢂⠐⠄⣈⠐⠠⠀⠌⠳⣆⢁⠂⠄⡁⠂⠄⡁⢂⠐⡀⠂⠄⡁⠂
⠌⡐⠠⢈⠐⠠⠈⠄⠡⠈⢄⠁⢂⢱⠇⡐⠠⢁⠂⠄⡁⢂⠁⢂⠐⠠⢈⠐⠠⠁⠌⠠⢁⠂⠄⡁⠂⠄⡁⢂⠐⠠⢈⠐⠠⢈⠡⠈⠄⠡⠸⡆⡈⠐⠠⢁⠂⡐⢀⠂⠄⡁⠂⠄⡁
⠂⠄⡁⠂⠌⠠⠁⠌⠠⢁⠂⠌⡀⡟⠠⢀⠡⠀⠌⣐⣀⣂⡌⡠⢈⠐⠠⠈⠄⠡⢈⠐⠠⢈⠐⠠⢁⠂⡐⠠⢈⡐⣠⣈⣐⣀⠂⠡⠈⠄⡁⢿⠀⡁⠂⠄⢂⠐⠠⢈⠐⠠⢁⠂⠄
⡁⠂⠄⠡⠈⠄⠡⢈⠐⠠⠌⡐⢠⡇⢁⠂⢤⡷⣿⣭⣿⣿⣿⣿⣿⣶⢥⣌⠠⢁⠂⠌⡐⠠⢈⠐⡀⣢⡴⣷⣿⣿⣿⣿⣿⣭⣿⢦⡅⢂⠐⢸⠂⠄⠡⠈⠄⣈⠐⠠⢈⠐⠠⠈⠄
⠄⠡⠈⠄⠡⢈⠐⠠⢈⠐⠄⡐⢠⡇⠠⢨⣯⠿⠋⢉⠉⡉⠙⠻⠿⣿⣿⣿⣭⠂⠌⡐⠠⢁⠂⡐⣭⣷⣿⣿⠿⠟⠋⢉⠉⡉⠙⠿⣽⡆⢈⢸⡃⠌⠠⢁⠂⠄⡈⢐⠠⠈⠄⡁⠂
⠌⠠⠁⠌⡐⠠⢈⠐⠠⢈⠐⠠⢸⠇⡀⡏⠁⠄⡈⠄⠂⠄⡁⢂⠐⡈⠙⠻⠟⠃⡐⠠⢁⠂⡐⠈⠿⠟⠋⡁⠐⠠⢁⠂⡐⠠⢁⠂⠌⢹⠀⢸⡇⠠⢁⠂⠌⡐⢀⠂⠄⡁⠂⠄⡁
⠌⠠⢁⠂⠄⡁⠂⠌⡐⠠⢈⠐⣸⡁⢣⠁⠌⡐⠠⢈⣰⣤⣴⣤⣦⣄⡁⠂⠌⠠⢹⡆⢀⢢⡟⠀⢂⠐⢠⣠⣥⣦⣤⣦⣀⠁⠂⠌⡐⠈⣜⠠⡇⠂⠄⡈⠐⡀⠂⠌⡐⠠⢁⠂⠄
⠌⡐⠠⢈⠐⠠⢁⠂⠄⡁⢂⠐⣾⠀⡘⣧⡂⠠⣱⡟⣫⣭⣶⣾⣯⣽⣛⢷⡌⠐⣀⡇⠂⢼⡀⠌⢠⡾⢟⣯⣽⣶⣾⣭⣝⣻⣦⠂⢠⣽⠁⠄⣿⢀⠂⠌⡐⠠⢁⠂⠄⡁⠂⠌⡀
⠂⠄⡁⠂⠌⡐⠠⢈⠐⡀⠂⢄⡏⡐⢀⣬⣷⣿⣿⣜⣛⠿⠿⠿⠿⣛⣻⡼⠋⠠⢸⡇⢈⢸⡇⠠⠙⣷⣟⣻⠿⠿⠿⢿⣛⣣⣿⣿⣾⣅⡀⢂⢹⡠⢈⠐⠠⢁⠂⠌⡐⠠⢁⠂⠄
⡁⠂⠄⡁⠂⠄⡁⠂⠄⠡⢈⠸⣇⣰⣿⠞⠉⡀⠄⡉⠛⠛⠛⠛⠛⢋⠡⢀⠁⢂⢸⡇⠠⢸⡇⠠⢁⠠⢈⠙⠛⠛⠛⠛⠛⠉⡀⠄⡉⠺⣽⣆⣼⡃⠠⢈⠐⠠⢈⠐⠠⢁⠂⠌⡀
⠄⡁⠂⠄⡁⠂⠄⠡⢈⠡⢀⠸⣿⠴⠁⡀⢂⠐⠠⠄⠡⠈⠄⠡⠈⠄⠂⠄⡈⠄⣾⠁⡐⠈⣷⠐⡀⠂⠤⠈⠄⠡⠈⠄⡁⢂⠐⢠⠀⠡⠈⠧⣿⠆⢁⠂⠌⡐⠠⢈⠐⠠⢈⠐⡀
⠂⠄⡁⠂⠄⠡⢈⠐⡀⠆⠠⢘⣿⡆⡐⡀⠂⠌⡐⠈⠄⠡⠈⠄⠡⢈⣰⠀⡐⢸⡏⠐⠠⢁⢹⡇⠠⢁⣂⠡⠈⠄⡁⢂⠐⠠⠈⠄⡈⠄⢡⢸⣿⠂⠄⡈⠐⠠⢁⠂⠌⡐⢀⠂⠄
⡁⠂⠄⠡⢈⠐⡀⢂⠐⡈⠐⡀⢿⢷⡹⣦⣁⠂⠄⠡⠈⠄⢡⣨⣴⣾⡇⠐⠠⢸⠂⡁⠂⠄⣈⡇⠐⠠⢹⣷⣮⣔⠀⠂⠌⠠⢁⠂⣐⣼⢏⡾⡿⢀⠂⠄⡑⢀⠂⠌⡐⢀⠂⠌⡀
⠄⠡⢈⠐⡀⢂⠐⡀⠂⠌⡐⢀⠺⡏⣧⣨⣿⡷⣾⣤⣷⠾⠛⠋⡁⠘⢧⣈⣴⣬⣣⠠⢁⠂⡜⣥⣼⣀⡼⠃⡈⠙⠻⠷⣾⣴⣶⢾⣿⣅⣼⢱⡇⠠⢈⠐⡀⠂⠌⡐⢀⠂⠌⡐⠀
⠌⡐⢀⠂⡐⢀⠂⠄⡁⠂⠔⠠⠈⣧⠘⣧⣻⣷⡜⣿⣿⣧⡠⠁⠄⡁⠂⠌⣹⣿⣿⣿⣿⣿⣿⣿⣏⠁⠄⠂⠄⡁⢂⣼⣿⣿⢣⣾⡿⣼⠃⣼⠀⡁⢂⠐⠠⢁⠂⡐⠠⢈⠐⠠⠁
⢂⠐⡀⢂⠐⠠⢈⠐⠠⠁⠌⠠⢁⢹⡄⠘⣧⣳⡿⣌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡿⣡⢿⢟⡼⠁⢤⡏⠐⡀⠂⠌⡐⢀⠂⠄⡁⠂⠌⠠⠁
⢂⠐⡀⠂⠌⡐⠠⠈⠄⠡⢈⡐⠠⢈⣧⠐⠈⢷⡻⣝⢦⣙⠛⠛⠛⠛⠛⠛⠛⠿⠿⣤⢥⡬⠽⠟⠛⠛⠛⠛⠛⠛⠛⢋⡴⣫⢟⡾⠁⠌⣸⠁⠂⠄⡁⢂⠐⠠⢈⠐⠠⠁⠌⠠⠁
⢂⠐⠠⢁⠂⠄⠡⠈⠄⡁⠂⠄⡁⢂⠸⣆⠁⢂⠻⣝⢦⡙⠲⣬⣀⠡⠈⠄⡁⠂⠄⠠⢀⠀⠂⠌⠠⠁⠌⢠⣁⣬⠞⢋⡴⣫⠟⠀⠌⣰⠋⠄⡁⢂⠐⠠⢈⠐⠠⠈⠄⠡⠈⠄⡁
⠂⠌⡐⠠⠈⠄⠡⢈⠐⠠⢁⠂⠰⢀⠂⠙⣎⡠⢀⠛⣮⢳⡄⠠⢉⠙⠛⠛⠓⢻⣶⣷⣶⣾⣾⡞⠛⠛⠛⠋⢉⠀⣐⠞⣵⠋⠠⢁⣼⠋⢀⠂⡐⠠⢈⠐⠠⠈⠄⠡⠈⠄⡁⠂⠄
⡁⠂⠄⠡⠈⠄⡁⠂⠌⡐⠠⢈⠐⠠⢈⠐⡈⠳⣄⠂⡈⢷⡙⢦⠀⠌⠠⢁⠂⠄⣿⣿⣿⣿⣿⠀⡐⠠⠁⠌⡀⡲⢋⡾⠁⠠⣡⠞⢁⠀⢂⠐⠠⢁⠂⠌⠠⠁⠌⠠⢁⠂⠄⡁⠂
⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⠂⠌⡐⠀⠆⠠⢁⠘⠷⣄⠀⠻⣦⠋⠠⢁⠂⠌⡐⣿⣿⣿⣿⣿⠃⠠⠁⠌⡐⠘⣵⠋⠄⣈⡶⠉⡐⠠⠈⠄⣈⠐⠠⠈⠄⠡⠈⠄⡁⠂⠌⡐⠠⠁
⠌⠠⢁⠂⠄⡁⠂⠄⡁⠂⠄⡁⠂⠄⠡⢈⠐⠄⠂⠄⡉⠷⣄⡈⢷⡅⠂⠌⡐⢀⢹⣿⣿⣿⡏⠠⠁⠌⡐⢠⡟⢁⣰⠞⢉⠀⡐⠠⠁⠌⡐⠠⠈⠄⠡⠈⠄⡁⠂⠄⡁⠂⠄⡁⠂
⠌⡐⠠⢈⠐⠠⢁⠂⠄⡁⠂⠄⠡⢈⠐⠠⠈⠄⡑⠠⠐⠠⢈⠻⢤⡙⢧⡐⢀⠂⠄⣿⣿⣿⠀⢂⠁⢂⡴⢋⡴⠞⠁⡐⢀⠂⠄⠡⢈⠐⠠⠁⠌⠠⠁⠌⡐⠠⢁⠂⠄⡁⠂⠄⡁
⠂⠄⡁⠂⠌⡐⠠⢈⠐⠠⠁⠌⡐⠠⠈⠄⡁⠂⠄⠡⢈⠐⡠⠐⠠⠙⠲⢽⡦⢬⣀⢿⣿⡿⣀⡦⢼⡯⠖⠋⡀⢂⠡⠐⠠⠈⠄⡁⠂⠌⠠⠁⠌⠠⢁⠂⠄⡁⠂⠌⡐⠠⢁⠂⠄
⡁⠂⠄⡁⠂⠄⡁⠂⠌⠠⢁⠂⠄⠡⢈⠐⠠⠁⠌⡐⢀⠂⠄⡁⢂⠡⠈⠄⡉⢉⠩⢉⠛⡉⠉⠍⡉⠠⢀⠡⠐⡀⢂⠁⢂⠁⠂⠄⠡⠈⠄⠡⢈⠐⠠⢈⠐⠠⢁⠂⠄⡁⠂⠌⡀
Developed by: xXJuanDavidXx ⠰⢀⠂⠄⠂⠄⡁⠂⠄⡁⠂⠄⠡⠐⠠⠈⠄⡈⠌⠠⠁⠌⠠⢁⠂⠌⡐⠠⢈⠐⠠⢈⠐⠠⢁⠂⠄

      """)

print("[+] -h para saber como usar el script")


time.sleep(0.5)


def tipo_de_hash(tipo_hash):
    """
    Función que retorna el tipo de hash que se va a utilizar para realizar la fuerza bruta

    args:
        tipo_hash: tipo de hash a utilizar - tipo: str
    """
    hash = {
        'sha1':hashlib.sha1,
        'sha224':hashlib.sha224,
        'sha256':hashlib.sha256,
        'sha384':hashlib.sha384,
        'sha512':hashlib.sha512,
        'sha3_224':hashlib.sha3_224,
        'sha3_256':hashlib.sha3_256,
        'sha3_384':hashlib.sha3_384,
        'sha3_512':hashlib.sha3_512,
        #'shake_128':hashlib.shake_128,
        #'shake_256':hashlib.shake_256,
        'blake2b':hashlib.blake2b,
        'blake2s':hashlib.blake2s,
        'md5':hashlib.md5
        }
    

    tipo = tipo_hash
    if tipo not in hash:
        raise argparse.ArgumentTypeError(f"Tipo de hash '{tipo}' no soportado")
    return hash[tipo]


def abrir_diccionario(diccionario):
    """
    Se obtiene el diccionario de palabras que se va a utilizar para realizar la fuerza bruta

    args:
        diccionario: la ruta del diccionario tipo unix /dir1/dir2 -- str
    """
    try:
        with open(diccionario, 'r', encoding='latin-1') as file:
            return file.readlines()
    except FileNotFoundError:
        print("[+]El diccionario no existe")
        exit()
    
def hilo(hash, lista, tipo, inicio, fin):
    for word in lista[inicio:fin]: #Se recorre el la lista de palabras de inicio a fin
        crypyted_password = tipo(word.encode()).hexdigest() #Aqui se esta hasheando la palabra que se almacena en word y se pasa a hexadecimal

        if hash == crypyted_password: #Realzia la comparacion de el hash que se pasa y el que se encripta en el diccionario
            #Guarda la contraseña en un archivo.
            print("[+]Contraseña encontrada: " + word)
            with open("Contraseña.txt", "w", encoding="utf-8") as f:
                f.write(f"Contraseña: {word}")

            os._exit(0)



#Main del programa y donde se hace la fuerza bruta
def brute_force(tipo, hash, dicc, workers=10):
    """
    Realiza fuerza bruta.
    
    args:
        tipo: el tipo de hash que se va a utilizar por ejemplo -t md5 -- str 
        hash: el hash que se va auditar --hash cb68123242154e70e95e1fcd08398ddc --str
        dicc: el diccionario de contraseñas -d /hola/quehace -- str

    """    
    passwords = [p.strip() for p in dicc]
    total = len(passwords)
    chunk = math.ceil(total / workers)
    print("[*] Para detener el script pulsa dos veces ctrl + c")
    process = log.progress('')  # Crea el indicador de progreso
   
    process.status("Haciendo fuerza bruta...")


    try:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for i in range(workers):
                inicio = i * chunk
                fin = (i + 1) * chunk
                executor.submit(hilo, hash, passwords, tipo, inicio, fin)


    except KeyboardInterrupt:
        print("[+]Fuerza bruta interrumpida por el usuario")
        os._exit(0)

    print("[+]Fuerza bruta finalizada")

def main (tipo ,hash, dicc):
    """
    Función principal del programa 
        args:
            hash: hash a auditar - tipo: str
            dicc: diccionario de contraseñas - tipo: str

    """
    if not hash or not dicc or not tipo:
        print("[+]Falta algun argumento")
        exit()


    hash_pass = hash #Texto hasheado.
    tipo_hash = tipo_de_hash(tipo) #Tipo de hash a utilizar
    dic = abrir_diccionario(dicc) #el diccionario
    brute_force(tipo_hash, hash_pass, dic)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script de fuerza bruta a algoritmos hash")
    parser.add_argument("-d", "--dict", type=str, help="La ruta al diccionario que se va a utilizar, por ejemplo -d /usr/share/wordlist/rockyou.txt")
    parser.add_argument("--hash", type=str, help="El hash que se va a auditar.")
    parser.add_argument("-t","--tipo", type=str, help="""El tipo de hash a utilizar por ejemplo -t sha250

        \n--Entre la lista de los hash admitidos.
         [+]sha1
         [+]sha224
         [+]sha256
         [+]sha384
         [+]sha512
         [+]sha3_224
         [+]sha3_256
         [+]sha3_384
         [+]sha3_512
         [+]blake2b
         [+]blake2s
         [+]md5
                        
                        """)

    args = parser.parse_args()
    
    try:
        main(args.tipo, args.hash, args.dict)
    except KeyboardInterrupt:
        print("\n[+] Fuerza bruta interrumpida por el usuario")
        os._exit(0)
