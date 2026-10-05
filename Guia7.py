import random

# 1.1
def pertenece(lista: list, elem: int) -> bool:  # Version 1
    return lista.count(elem) != 0

def pertenece_v2(lista: list, elem: int) -> bool: # Version 2
    for e in lista:
        if e == elem: return True
    return False

def pertenece_v3(lista: list, elem: int) -> bool: # Version 3
    i: int = 0
    while i < len(lista):
        if lista[i] == elem: return True
        else: i += 1
    return False

# 1.2
def divide_a_todos(lista: list, d: int) -> bool:
    for num in lista:
        if num % d != 0: return False
    return True

# 1.3
def suma_total(lista: list) -> int:
    n: int = 0
    for num in lista:
        n += num
    return n

# 1.4
def ordenados(lista: list) -> bool:
    i: int = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]: return False
        else: i += 1
    return True

# 1.5
def palabra_larga(lista: list) -> bool:
    for palabra in lista:
        if len(palabra) > 7: return True
    return False

# 1.6
def palindromos(palabra: str) -> bool:
    l: int = len(palabra) // 2
    for letra in range(l):
        if palabra[letra] != palabra[len(palabra) - letra - 1]: return False
    return True

# 1.7
def cumple_caracteres(psw: str) -> bool:        
    minus: bool = False
    mayus: bool = False
    num: bool = False
    lowercase: str = 'abcdefghijklmnopqrstuvwxyz'
    uppercase: str = str.upper(lowercase)
    numbers: str = '0123456789'
    for letra in psw:
        if pertenece(lowercase, letra): minus = True
        elif pertenece(uppercase, letra): mayus = True
        elif pertenece(numbers, letra): num = True
    return minus and mayus and num

def password(psw: str) -> str:
    if len(psw) < 5: return 'ROJA'
    elif len(psw) > 8 and cumple_caracteres(psw): return 'VERDE'
    else: return 'AMARILLO'

# 1.8
def saldo_actual(act: list) -> int:
    saldo: int = 0
    for mov in act:
        if mov[0] == 'R': saldo -= mov[1]
        elif mov[0] == 'I': saldo += mov[1]
    return saldo

# 1.9
def tres_vocales(palabra: str) -> bool:
    vocales: str = 'aeiou'
    n: int = 0
    for letra in palabra:
        for vocal in vocales:
            if str.lower(letra) == vocal:
                n += 1
                vocales = vocales.replace(vocal, "")
    return n >= 3

# 2.1
def cero_en_pares(lista: list):
    for i in range(len(lista)):
        if (i+1) % 2 == 0: 
            lista[i] = 0

# 2.2
def cero_en_pares_2(lista: list) -> list:
    otra_lista: list = []
    for i in range(len(lista)):
        if (i+1) % 2 == 0: 
            otra_lista.append(0)
        else: 
            otra_lista.append(lista[i])
    return otra_lista

# 2.3
def quita_vocales(palabra: str) -> str:
    res: str = ""
    vocales: str = "aeiouAEIOU"
    for letra in palabra:
        if letra not in vocales:
            res += letra
    return res

# 2.4
def reemplaza_vocales(palabra: str) -> str:
    res: str = ""
    vocales: str = "aeiouAEIOU"
    for letra in palabra:
        if letra not in vocales:
            res += letra
        else: res += '_'
    return res

# 2.5
def invertir_str(palabra: str) -> str:
    res: str = ""
    for i in range(len(palabra), 0, -1):
        res += palabra[i-1]
    return res

# 3.1
def nombres() -> list:
    res: list = []
    word: str = ""
    while str.lower(word) != "listo":
        word = input("Ingrese el nombre del alumno: ")
        res.append(word)
    res.pop()
    return res

# 3.2
def historial() -> list:
    accion: str = input("Que desea hacer: ")
    res: list = []
    monto: int = 0
    while str.upper(accion) != 'X':
        monto = input("Ingrese el monto: ")
        res.append((accion, monto))
        accion = input("Que desea hacer: ")
    return res

# 3.3
def valor_carta(x: int) -> float:
    if x > 9:
        return 0.5
    else:
        return x

def siete_y_medio() -> list:
    cartas: list = []
    valor = random.choice([1,2,3,4,5,6,7,10,11,12])
    cartas.append(valor)
    total: float = valor_carta(valor)
    accion: str = input("El total actual es: " + str(total) + " Seguir? y/n ")
    while str.lower(accion) == 'y':
        valor = random.choice([1,2,3,4,5,6,7,10,11,12])
        cartas.append(valor)
        total += valor_carta(valor)
        accion = input("El total actual es: " + str(total) + " Seguir? y/n ")
    if total > 7.5: return ["Perdiste", total, cartas]
    else: return ["Ganaste", total, cartas]

# 4.1
def pertenece_a_cada_uno(matriz: list, elem: int) -> list:
    res: list = []
    for fila in matriz:
        if pertenece(fila, elem):
            res.append(True)
        else:
            res.append(False)
    return res

# 4.2
def es_matriz(matriz:list[list]) -> bool:
    l: int = len(matriz[0])
    for fila in matriz:
        if len(fila) == 0 or len(fila) != l:
            return False
    return True
