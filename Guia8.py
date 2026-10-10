# 1.1
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

