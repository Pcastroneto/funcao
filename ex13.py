#abs é do python dando um valor absoluto
def calcular_raiz_quadrada(numero, precisao=0.0001):
    raiz = numero/2
    while abs(numero - raiz**2)> precisao:
        raiz = (raiz + numero/raiz)/2
    return raiz

numero = 81
raiz = calcular_raiz_quadrada(numero)
print("A raiz quadrada de", numero,"é", raiz)
# abs usado para mostrar o valor absoluto de um numero
#Exemplo abaixo 
print(abs(-5))