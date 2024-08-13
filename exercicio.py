# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def fazer_multiplicacao(multiplicador):
    def duplicar(numero):
        return numero * multiplicador
    return duplicar

duplicar = fazer_multiplicacao(2)
triplicar = fazer_multiplicacao(3)
quadriplicar = fazer_multiplicacao(4)

print(duplicar(5))
print(triplicar(5))
print(quadriplicar(5))