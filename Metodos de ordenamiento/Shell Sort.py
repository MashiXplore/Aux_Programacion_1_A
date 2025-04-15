def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def main():
    vector = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", vector)
    shell_sort(vector)
    print("Ordenado con Shell Sort:", vector)

main()