import math

#Ejercicio 1

# 1.1
def RaizDe2() -> int:
    return round(math.sqrt(2),4)

# 1.2
def imprimir_hola():
    print("hola")

# 1.3
def imprimir_verso():
    print("Me quedo con vos, yo sigo de largo, voy a buscarte\nQue noche magica, ciudad de Buenos Aires\nSe queman las horas de esta manera, nadie me espera\nComo me gusta verte caminar asi")

# 1.4
def factorial_de_2():
    return math.factorial(2)

# 1.5
def factorial_de_3():
    return math.factorial(3)

# 1.6
def factorial_de_4():
    return math.factorial(4)

# 1.7
def factorial_de_5():
    return math.factorial(5)

# Ejercicio 2

# 2.1
def imprimir_saludo(nombre: str):
    print("Hola " + nombre)

# 2.2
def raiz_cuadrada_de(numero: int):
    return math.sqrt(numero)

# 2.3
def fahrenheit_a_celcius(numero: int) -> int:
    return (numero-32)*5/9

# 2.4
def imprimir_dos_veces(estribillo: str):
    print(estribillo*2)

# 2.5
def es_multiplo_de(numero: int, divisor: int) -> bool:
    return numero % divisor == 0

# 2.6
def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)

# 2.7
def cantidad_de_pizzas(comensales: int, min_cant_porciones:int) -> int:
    porciones_totales: int = min_cant_porciones*comensales
    pizzas_necesarias: float = porciones_totales / 8
    if pizzas_necesarias % 1 == 0:
        return porciones_totales // 8
    else:
        return porciones_totales // 8 + 1

# 3.1
def alguno_es_cero(n1: int, n2: int) -> bool:
    return n1 == 0 or n2 == 0

# 3.2
def ambos_son_cero(n1:int, n2: int) -> bool:
    return n1 == 0 and n2 == 0

# 3.3
def problema_es_nombre_largo(nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# 3.4
def es_bisiesto(año: int) -> bool:
    return año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)

# 4.1
def peso_pino(altura: int) -> int:
    if altura >= 3:
        return 900 + (altura - 3) * 200
    else:
        return altura * 300

# 4.2
def es_peso_util(peso: int) -> bool:
    return peso >= 400 and peso <= 1000

# 4.3
def sirve_pino(altura: int) -> bool:
    if altura == 1: return False
    elif altura > 3: return False
    else: return True

# 4.4
def sirve_pino_v2(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))

# 5.1
def doble_si_es_par(numero: int) -> int:
    if es_par(numero): return numero*2
    else: return numero

# 5.2
def consecutivo_de_impares(numero: int) -> int:
    if es_par(numero): return numero
    else: return numero + 1

# 5.3
def random_bullshit_go(numero: int) -> int:
    if es_multiplo_de(numero, 9): return numero * 3
    elif es_multiplo_de(numero, 3): return numero * 2
    else: return numero

# 5.4
def lindo_nombre(nombre: str) -> str:
    if len(nombre) < 5: return "Tu nombre tiene menos de 5 caracteres"
    else: return "Tu nombre tiene muchas letras!"

# 5.5
def el_rango(numero: int) -> str:
    if numero < 5: return "Menor a 5"
    elif numero > 9 and numero < 21: return "Entre 10 y 20"
    elif numero > 20: return "Mayor a 20"

# 5.6
def a_trabajar(genero: str, edad: int) -> str:
    if edad < 18: return "Andá de vacaciones"
    elif edad >= 60 and genero == "F": return "Andá de vacaciones"
    elif edad >= 65 and genero == "M": return "Andá de vacaciones"
    else: return "Te toca trabajar"

# 6.1
def numeros_del_1_al_10():
    numero: int = 1
    while(numero < 11): 
        print(numero)
        numero += 1
    return False

# 6.2
def numeros_pares_entre_10_y_40():
    numero: int = 10
    while(numero < 41):
        if es_par(numero):
            print(numero)
        numero += 1

# 6.3
def eco():
    numero: int = 1
    while(numero < 11): 
        print("eco")
        numero += 1
    return False

# 6.4
def cuenta_regresiva(numero: int):
    while(numero > 0):
        print(numero)
        numero += 1
    print("Despegue") 

# 6.5
def saltos_en_el_tiempo(año_de_partida: int, año_de_llegada: int):
    año: int = año_de_partida
    while(año > año_de_llegada):
        print("Viajo un año al pasado, estamos en el año " + str(año))
        año -= 1
    print("Llego al " + str(año))

# 6.6
def more_bullshit(partida: int):
    while(partida > 384):
        print("Viajo veinte años al pasado, estamos en el año " + str(partida))
        partida -= 20
    print("Llegamos al año " + str(partida))

# 7.1
def uno_al_diez():
    for num in range (10):
        print(num + 1)

# 7.2
def diez_al_cuarenta():
    for num in range(10, 41, 2):
        print(num)

# 7.3
def echo():
    for num in range(10):
        print("eco")

# 7.4
def rocket_launch(n: int):
    for num in range(n, 0, -1):
        print(num)
    print("Despegue")

# 7.5
def time_travel(salida: int, llegada: int):
    for num in range(salida, llegada-1, -1):
        print("Viajo un año al pasado, estamos en el año " + str(num))

# 7.6
def aristoteles(salida: int):
    for num in range(salida, 384, -20):
        print("Viajo veinte años al pasado, estamos en el año " + str(num))
    print("Llegamos para conocer a Aristoteles")