import math
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
def suma_total(lista: list[int]) -> int:
    n: int = 0
    for num in lista:
        n += num
    return n

# 1.4
def maximo(lista: list[int]) -> int:
    max: int = -1
    for num in lista:
        if num > max:
            max = num
    return max

# 1.5
def minimo(lista: list[int]) -> int:
    min: int = math.inf
    for num in lista:
        if num < min:
            min = num
    return min

# 1.6
def ordenados(lista: list[int]) -> bool:
    i: int = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]: return False
        else: i += 1
    return True

# 1.7
def pos_maximo(lista: list[int]) -> int:
    max: int = maximo(lista)
    for i in range(len(lista)):
        if max == lista[i]: return i+1

# 1.8
def pos_minimo(lista: list[int]) -> int:
    min: int = minimo(lista)
    for i in range(len(lista)):
        if min == lista[i]: return i+1

# 1.9
def palabra_larga(lista: list) -> bool:
    for palabra in lista:
        if len(palabra) > 7: return True
    return False

# 1.10
def palindromos(palabra: str) -> bool:
    l: int = len(palabra) // 2
    for letra in range(l):
        if palabra[letra] != palabra[len(palabra) - letra - 1]: return False
    return True

# 1.11
def iguales_consecutivos(lista: list[int]) -> bool:
    num: int = 0
    for i in range(len(lista)-1):
        if lista[i] != num:
            num = lista[i]
        elif lista[i] == num and lista[i+1] == num: 
            return True
    return False

# 1.12
def tres_vocales(palabra: str) -> bool:
    vocales: str = 'aeiou'
    n: int = 0
    for letra in palabra:
        for vocal in vocales:
            if str.lower(letra) == vocal:
                n += 1
                vocales = vocales.replace(vocal, "")
    return n >= 3

# 1.13
def pos_secuencia_ordenada_mas_larga(lista: list[int]) -> int:
    pos: int = 0
    l: int = 0
    l_max: int = 0
    for i in range(len(lista)-1):
        if lista[i] + 1 == lista[i+1]:
            if l > l_max:
                pos = i
                l_max = l
            l += 1
        else: l = 0
    return pos - l_max + 1

# 1.14
def cantidad_de_impares(lista: list[int]) -> int:
    total: int = 0
    for num in lista:
        while num > 9:
            if (num%10) % 2 == 1:
                total += 1
            num = num // 10
        if num % 2 == 1: 
            total += 1
    return total

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

# 2.6
def quitar_repetidos(palabra: str) -> str:
    res: str = ""
    for c in palabra:
        if not pertenece(res, c):
            res = res + c
    return res

# 3
def resultado_materia(notas: list[int]) -> int:
    promedio: int = 0
    for n in notas:
        if n < 4:
            return 3
        else:
            promedio += n
    promedio = promedio // len(notas)
    if promedio >= 7:
        return 1
    else:
        return 2

# 4
def saldo_actual(act: list) -> int:
    saldo: int = 0
    for mov in act:
        if mov[0] == 'R': saldo -= mov[1]
        elif mov[0] == 'I': saldo += mov[1]
    return saldo

# 5
def pertenece_a_cada_uno(matriz: list, elem: int) -> list:
    res: list = []
    for fila in matriz:
        if pertenece(fila, elem):
            res.append(True)
        else:
            res.append(False)
    return res

# 6.1
def es_matriz(matriz:list[list[int]]) -> bool:
    l: int = len(matriz[0])
    for fila in matriz:
        if len(fila) == 0 or len(fila) != l:
            return False
    return True

# 6.2
def filas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for fila in matriz:
        if not ordenados(fila):
            res.append(False)
        else:
            res.append(True)
    return res

# 6.3
def columna(matriz: list[list], c) -> list:
    res: list[int] = []
    for fila in matriz:
        res.append(fila[c-1])
    return res

# 6.4
def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for c in matriz[0]:
        if ordenados(columna(matriz, c)):
            res.append(True)
        else:
            res.append(False)
    return res

# 6.5
def transponer(matriz: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(len(matriz[0])):
        res.append(columna(matriz, i+1))
    return res

# 6.6
def todos_iguales(fila: list[str], elem: str) -> bool:
    for i in range(len(fila)):
        if fila[i] != elem:
            return False
    return True

def tateti(tablero: list[list[str]]) -> int:
    for fila in tablero:
        if todos_iguales(fila, 'O'): return 0
        elif todos_iguales(fila, 'X'): return 1
        else:
            for i in range(len(fila)):
                if todos_iguales(columna(tablero, i), 'O'): return 0
                elif todos_iguales(columna(tablero, i), 'X'): return 1
    if tablero[1][1] == tablero[0][0] and tablero[1][1] == tablero[2][2] and tablero[1][1] == 'O': return 0
    elif tablero[1][1] == tablero[0][0] and tablero[1][1] == tablero[2][2] and tablero[1][1] == 'X': return 1
    elif tablero[1][1] == tablero[0][2] and tablero[1][1] == tablero[2][0] and tablero[1][1] == 'O': return 0
    elif tablero[1][1] == tablero[0][2] and tablero[1][1] == tablero[2][0] and tablero[1][1] == 'X': return 1
    else: return 2 

# 7.1
def nombres() -> list:
    res: list = []
    word: str = ""
    while str.lower(word) != "listo":
        word = input("Ingrese el nombre del alumno: ")
        res.append(word)
    res.pop()
    return res

# 7.2
def historial() -> list:
    accion: str = input("Que desea hacer: ")
    res: list = []
    monto: int = 0
    while str.upper(accion) != 'X':
        monto = input("Ingrese el monto: ")
        res.append((accion, monto))
        accion = input("Que desea hacer: ")
    return res

# 7.3
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

# 7.4
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
