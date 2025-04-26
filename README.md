# Script de Fuerza Bruta para Hashes de Contraseñas

Este script permite realizar fuerza bruta en local para encontrar contraseñas a partir de un hash proporcionado.

## Desarrollado por
**xXJuanDavidXx**

---

## Características

- Compatible con múltiples algoritmos hash: `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`, `blake2b`, `blake2s` y `md5`.
- Utiliza diccionarios para probar contraseñas.
- Soporte multihilo para acelerar el proceso.
- Guarda la contraseña encontrada en un archivo `Contraseña.txt`.

---

## Uso

### Ejecución
```bash
python script.py -t <tipo_hash> --hash <hash> -d <ruta_diccionario>
```

### Parámetros
- `-t` o `--tipo`: Tipo de hash a utilizar (ejemplo: `md5`, `sha256`).
- `--hash`: Hash que se desea auditar.
- `-d` o `--dict`: Ruta al diccionario de contraseñas.

### Ejemplo
```bash
python script.py -t md5 --hash cb68123242154e70e95e1fcd08398ddc -d /usr/share/wordlist/rockyou.txt
```

---

## Funciones Principales

- **`tipo_de_hash(tipo_hash)`**  
  Verifica y selecciona el algoritmo hash especificado.

- **`abrir_diccionario(diccionario)`**  
  Abre y carga las palabras del diccionario para su uso.

- **`hilo(hash, lista, tipo, inicio, fin)`**  
  Realiza fuerza bruta sobre un subconjunto del diccionario.

- **`brute_force(tipo, hash, dicc, workers=10)`**  
  Divide el trabajo en hilos y realiza la fuerza bruta.

- **`main(tipo, hash, dicc)`**  
  Función principal para validar argumentos y ejecutar el proceso.

---

## Requisitos

- Python 3.x
- Librerías: `hashlib`, `argparse`, `concurrent.futures`, `os`, `math`, `pwn`

---

## Notas

- **Interrupción**: Presiona `Ctrl + C` dos veces para detener el script.
- **Advertencia**: Este script debe ser utilizado únicamente con fines educativos o en entornos autorizados.

---
