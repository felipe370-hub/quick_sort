def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivot]
    meio = [x for x in lista if x == pivot]
    direita = [x for x in lista if x > pivot]
    return quick_sort(esquerda) + meio + quick_sort(direita)

def main():
    exemplos = [
        [3, 6, 8, 10, 1, 2, 1],
        [1, 4, 3, 9, 7, 4],
        [5, 9, 1, 3, 4, 6, 6, 3],
        [10, 7, 8, 9, 1, 5]
    ]
    
    for lista in exemplos:
        print("Lista original:", lista)
        lista_ordenada = quick_sort(lista)
        print("Lista ordenada:", lista_ordenada)
        print()  # Adiciona uma linha em branco para separar os resultados

if __name__ == "__main__":
    main()
