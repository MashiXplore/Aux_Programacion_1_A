def obtener_pivote(lista):
    return lista[0]

def obtener_menores(lista, pivote):
    menores = []
    for elemento in lista[1:]:
        if elemento <= pivote:
            menores.append(elemento)
    return menores

def obtener_mayores(lista, pivote):
    mayores = []
    for elemento in lista[1:]:
        if elemento > pivote:
            mayores.append(elemento)
    return mayores

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = obtener_pivote(lista)
        menores = obtener_menores(lista, pivote)
        mayores = obtener_mayores(lista, pivote)
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

def main():
    vector = [10, 5, 3, 8, 4, 2, 9]
    print("Lista original:", vector)
    ordenada = quick_sort(vector)
    print("Lista ordenada:", ordenada)

main()
