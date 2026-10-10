# 1.1
import random
from queue import LifoQueue as Pila


def contar_lineas(nombre: str) -> int:
    f = open(nombre, 'r')
    return len(f.readlines())

# 1.2
def existe_palabra(palabra: str, archivo: str) -> bool:
    f = open(archivo, 'r')
    for i in range(contar_lineas(archivo)):
        for word in f.readline().split():
            if palabra == word:
                return True
    return False

# 1.3
def cantidad_de_apariciones(palabra: str, archivo: str) -> int:
    num: int = 0
    f = open(archivo, 'r')
    for i in range(contar_lineas(archivo)):
        for word in f.readline().split():
            if palabra == word:
                num += 1
    return num

# 2
def clonar_sin_comentarios(archivo: str):
    f = open(archivo, 'r')
    c = open('copia.txt', 'w')    
    for lines in f.readlines():
        _lines = lines.split()
        if _lines[0] != '#':
            c.write(lines)
        
# 3
def reverso(archivo: str):
    f = open(archivo, 'r').readlines()
    c = open('reverso.txt', 'w')
    for i in range(len(f)):
        if 1 == i:
            c.write('\n')
        c.write(f[len(f)-i-1])

# 4
def agregar_linea(archivo: str, linea: str):
    f = open(archivo, 'a')
    f.write(linea)

# 5
def agregar_linea_al_principio(archivo: str, linea: str):
    f = open(archivo, 'r')
    lineas: list[str] = f.readlines()
    f.close()
    f = open(archivo, 'w')
    f.write(linea + '\n')
    f.writelines(lineas)

# 6
def style(b: bytes) -> str:
    return str(b).split("'")[1]

def leer_binario(archivo: str) -> list[str]:
    res: list[str] = []
    f = open(archivo, 'rb')
    for line in f.readlines():
        for word in line.split():
            if len(word) >= 5:
                res.append(style(word))
    return res

# 7
def promedio_estudiante(lu: str) -> float:
    f = open('notas.csv', 'r').readlines()
    nota: float = 0
    cont: int = 0
    for line in f:
        line_aux: list[str] = line.split(',')
        for data in line_aux:
            if str(data) == lu:
                nota += float(line_aux[3])
                cont += 1
    if cont == 0:
        return 0
    return nota / cont

# 8
def generar_numeros_al_azar(n: int, desde: int, hasta: int) -> list[int]:
    res: list[int] = random.sample(range(desde, hasta), n)
    return res

# 9
def pila_de_numeros(numeros: list[int]) -> Pila:
    p = Pila()
    for n in numeros:
        p.put(n)
    return p

# 10
def cantidad_elementos(p: Pila) -> int:
    i: int = 0
    while not p.empty():
        i += 1
        p.get()
    return i

# 11
def maximo_pila(p: Pila) -> int:
    max: int = float('-inf')
    i: int = 0
    while not p.empty():
        if p.get() > max:
            max = p.get()
        i +=1
    return max

# 12
