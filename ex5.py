def funcao_detectada(n):
    if (n % 2 == 0):
        return 'É par'
    else:
        return 'É ímpar'

print(funcao_detectada(int(input('Entre com um número: '))))