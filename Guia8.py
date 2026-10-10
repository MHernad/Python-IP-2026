# 1.1
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

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
    while not p.empty():
        if p.get() > max:
            max = p.get()
    return max

# 12
def esta_bien_balanecada(s: str) -> bool:
    p = Pila()
    for c in s:
        if c == '(' and p.empty():
            p.put(c)
        elif c == '(':
            if p.get() != ')':
                return False
        elif c == ')':
            if p.empty() or p.get() != '(':
                return False
    return True

# 13
def cola_numeros(numeros: list[int]) -> Cola:
    c = Cola()
    for n in numeros:
        c.put(n)
    return c

# 14
def cola_size(c: Cola) -> int:
    i: int = 0
    while not c.empty():
        i += 1
        c.get()
    return i

# 15
def maximo_cola(c: Cola) -> int:
    max: int = float('-inf')
    while not c.empty():
        if max < c.get():
            max = c.get()
    return max

# 16.1
def armar_secuencia_juego() -> Cola[int]:
    c = Cola()
    sec: list[int] = random.sample(range(100), 100)
    for n in sec:
        c.put(n)
    return c

# 16.2
def pertenece(lista: list, elem: int) -> bool:
    return lista.count(elem) != 0

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    while not bolillero.empty() and len(carton) > 0:
        num: int = bolillero.get()
        if pertenece(carton, num):
            carton.remove(num)
        jugadas += 1
    return jugadas

# 17
def pacientes_urgentes(c: Cola[(int, str, str)]):
    n: int = 0
    while not c.empty():
        paciente: tuple = c.get()
        if paciente[0] in [1,2,3]:
            n += 1
    return n

# 18
def agrupar_longitud(archivo: str) -> dict:
    d: dict = {}
    f = open(archivo, 'r').readlines()
    for line in f:
        for word in line.split():
            key = len(word)
            if key not in d.keys():
                d[key] = 1
            else:
                d.update({key: d[key]+1})
    return d

# 19
def promedios(archivo: str) -> dict:
    d: dict = {}
    f = open(archivo, 'r')
    f.readline()
    f = f.readlines()
    for line in f:
        words = line.split(',')
        key:str = words[0]
        nota: float = float(words[3])
        if key not in d.keys():
            d[key] = (nota, 1)
        else:
            d[key] = (d[key][0] + nota, d[key][1] + 1)
    for key in d.keys():
        d[key] = d[key][0] / d[key][1]
    return d

# 20
def palabra_mas_frecuente(archivo: str) -> str:
    d: dict = {}
    f = open(archivo, 'r').readlines()
    for line in f:
        for word in line.split():
            word = str.lower(word)
            if word not in d.keys():
                d[word] = 1
            else:
                d[word] = d[word] + 1
    s: str = ""
    c: int = 0
    for key in d.keys():
        if d[key] > c:
            c = d[key]
            s = key
    return s