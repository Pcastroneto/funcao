def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j]< lista[i]:
                lista[i], lista[j] = lista[j], lista[i]  
    return lista

lista = [5,2,9,1,7,3,220,35,31,45,67,89,74,31,13,27]
lista_ordenada = ordenar_lista(lista)
print('A lista ordenada é:', lista_ordenada)