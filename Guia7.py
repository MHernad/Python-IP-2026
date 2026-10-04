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
