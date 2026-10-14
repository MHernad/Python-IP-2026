import random
from queue import LifoQueue as Pila
from queue import Queue as Cola

# Pilas
# 1
def generar_numeros_al_azar(n: int, desde: int, hasta: int) -> Pila[int]:
    p = Pila()
    for num in range(n):
        p.put(random.randint(desde, hasta))
    return p

# 2
def cantidad_elementos(p: Pila) -> int:
    i: int = 0
    l: list[int] = []
    while not p.empty():
        i += 1
        l.append(p.get())
    for x in range(len(l)-1, 0, -1):
        p.put(l[x])
    return i

# 3
def maximo_pila(p: Pila) -> int:
    max: int = float('-inf')
    while not p.empty():
        if p.get() > max:
            max = p.get()
    return max

# 4
def buscar_nota_maxima(p: Pila[(str, int)]) -> tuple[str, int]:
    nota_max: tuple[str, int] = ('', 0)
    for num in range(cantidad_elementos(p)):
        nota: tuple[str, int] = p.get()
        if nota[1] > nota_max[1]:
            nota_max = nota
    return nota_max

# 5
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
        if p.get() == '(' and p.empty():
            return False
    return True

# 6
def evaluar_expresion(s: str) -> float:
    p = Pila()
    l: list[str] = s.split()
    for item in l:
        match item:
            case '+':
                n1 = float(p.get())
                n2 = float(p.get())
                p.put(n1+n2)
            case '-':
                n1 = float(p.get())
                n2 = float(p.get())
                p.put(n2-n1)
            case '*':
                n1 = float(p.get())
                n2 = float(p.get())
                p.put(n1*n2)
            case '/':
                n1 = float(p.get())
                n2 = float(p.get())
                p.put(n2/n1)
            case _:
                p.put(item)

    return float(p.get())

# 7
def intercalar(p1: Pila[int], p2: Pila[int]) -> Pila[int]:
    p: Pila = Pila()
    while not p1.empty():
        p.put(p1.get())
        p.put(p2.get())
    return p

# Colas
# 8
def generar_numeros_al_azar_cola(n: int, d: int, h: int) -> Cola[int]:
    c = Cola()
    for num in range(n):
        c.put(random.randint(d, h))
    return c

# 9
def cantidad_elementos_cola(c: Cola[int]) -> int:
    i: int = 0
    l: list[int] = []
    while not c.empty():
        i += 1
        l.append(c.get())
    for x in l:
        c.put(x)
    return i

# 10
def maximo_cola(c: Cola) -> int:
    max: int = float('-inf')
    while not c.empty():
        if max < c.get():
            max = c.get()
    return max

# 11
def buscar_nota_minima(c: Cola[(str, int)]) -> tuple[str, int]:
    max: int = float('inf')
    nota_min: tuple[str, int] = ('', max)
    for num in range(cantidad_elementos_cola(c)):
        nota: tuple[str, int] = c.get()
        if nota[1] < nota_min[1]:
            nota_min = nota
    return nota_min

# 12
def intercalar_cola(c1: Cola[int], c2: Cola[int]) -> Cola[int]:
    c = Cola()
    while not c1.empty():
        c.put(c1.get())
        c.put(c2.get())
    return c

# 13.1
def armar_secuencia_juego() -> Cola[int]:
    c = Cola()
    sec: list[int] = random.sample(range(100), 100)
    for n in sec:
        c.put(n)
    return c

# 13.2
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

# 14
def pacientes_urgentes(c: Cola[(int, str, str)]):
    n: int = 0
    while not c.empty():
        paciente: tuple = c.get()
        if paciente[0] in [1,2,3]:
            n += 1
    return n

# 15
def atencion_a_clientes(c: Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    cola_prioritaria: Cola = Cola()
    cola_preferencial: Cola = Cola()
    cola_chud: Cola = Cola()
    cola_final: Cola = Cola()
    for i in range(cantidad_elementos_cola(c)):
        persona = c.get()
        if persona[3]:
            cola_prioritaria.put(persona)
        elif persona[2]:
            cola_preferencial.put(persona)
        else:
            cola_chud.put(persona)
    while not cola_prioritaria.empty():
        cola_final.put(cola_prioritaria.get())
    while not cola_preferencial.empty():
        cola_final.put(cola_preferencial.get())
    while not cola_chud.empty():
        cola_final.put(cola_chud.get())
    return cola_final

# Diccionarios
# 16
def cantidad_de_apariciones(l: list[(str, int)], n: str) -> int:
    i: int = 0
    for item in l:
        if item[0] == n:
            i += 1
    return i

def promedio_x_estudiante(notas: list[(str, float)]) -> dict[str, float]:
    d: dict[str, int] = {}
    for alumno in notas:
        if not alumno[0] in d.keys():
            d[alumno[0]] = alumno[1]
        else:
            d[alumno[0]] = d[alumno[0]] + alumno[1]
    for alum in d.keys():
        d[alum] = d[alum] / cantidad_de_apariciones(notas, alum)
    return d

# 17
# a
def visitar_sitio(hist: dict[(str, Pila[str])], user: str, web: str):
    if user not in hist.keys():
        p: Pila = Pila()
        p.put(web)
        hist[user] = p
    else:
        p: Pila = hist[user]
        p.put(web)
        hist[user] = p

# b
def navegar_atras(hist: dict[(str, Pila[str])], user: str) -> str:
    p: Pila = Pila()
    p = hist[user]
    web: str = p.get()
    hist[user] = p
    return web

# 18

# Archivos Viejo
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

