def ingrese():
    n = int(input("Ingrese un numero: "))
    matris = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    return matris , n 

def imprime(matris,n):
    for i in range(n):
        for j in range(n):
            print(matris[i][j], end=" ")
        print()
matris,n = ingrese()
imprime(matris,n)
