# Configuração Inicial
import random
lista = ["Computador", "Hardware", "Teclado", "Python"]
palavraSorteada = random.choice(lista).upper()
palavraEscondida = "_"*len(palavraSorteada)
letrasTentadas = []
TentativasMax = 6

# Desenho e Pedido
while True:
    print(f"_____\n|   |\n|\n|\n|   {' '.join(palavraEscondida)}")
    print("="*40)
    chute = input("Digite uma letra: ").upper()

# Listagem dos Chutes
    if chute in letrasTentadas:
        print("Você já digitou essa letra!")
        continue
    letrasTentadas.append(chute)

# Verificar Acerto
    if chute in palavraSorteada:

        palavraEscondida = ''.join(chute if chute == palavraSorteada[indice] else palavraEscondida[indice] for indice in range(len(palavraSorteada)))

#        Correção = []
#        for i in range(len(palavraSorteada)):
#            if chute == palavraSorteada[i]:
#                Correção.append(chute)
#            else:
#                Correção.append(palavraEscondida[i])
#        palavraEscondida = ''.join(Correção)

    else:
        TentativasMax -= 1
        print(f"Letra incorreta. Você tem mais {TentativasMax} chances!")

# Finalizar Jogo
    if palavraEscondida == palavraSorteada:
        print("Você acertou! Parabéns!!!")
        break
    elif TentativasMax == 0:
        print(f"Tentativas esgotadas. Você perdeu.\nA palavra era {palavraSorteada}")
        break