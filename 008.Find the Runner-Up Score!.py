if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    listaTemporaria = sorted(list(set(arr)))
    print(listaTemporaria[-2])
