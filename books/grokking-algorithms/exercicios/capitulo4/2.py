def totalItens(lista):
	if len(lista) == 1:
		return 1
	else:
		return 1 + totalItens(lista[1:])

lista = [1, 2, 3, 4, 5, 6]
print(totalItens(lista))
