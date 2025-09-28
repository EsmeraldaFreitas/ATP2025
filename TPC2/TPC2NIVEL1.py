# Tpc2- Jogo dos Fósforos
## nível 1- computador joga em 2 lugar
### O jogo consiste em ir tirando fósforos (1,2,3 ou 4) de um total de 21 à vez alternando com o computador e o último jogador a tirar fósforos perde.

print ("Jogo dos Fósforos-nível 1")
total=21
sabe_jogar=input("Sabes como funciona o jogo? responde com s ou n? ")
while sabe_jogar!= "s" :
    print ("O jogo consiste em ir tirando fósforos (1,2,3 ou 4) de um total de 21, à vez, alternando com o computador e o último jogador a tirar fósforos perde.")
    sabe_jogar=input("Já sabes como funciona o jogo? responde com s ou n? ")
while total>1:
    num=int(input (f"Temos {total} fósforos, quantos queres tirar? "))
    while num!=1 and num!=2 and num!=3 and num!=4 :
        print ("O número que introduziste não se encontra entre 1 e 4, por favor insere um número válido!")
        num=int(input (f"Temos {total} fósforos, quantos queres tirar? "))
    total=total-num
    print(f"Restiraste {num} agora temos {total} fósforos!")
    
    pc=5-num
    total=total-pc
    print(f"O computador retirou {pc} fósforos!  ")
if total==1:
    print ("Há 1 fósforo, logo és o último a retirar o fósforo, PERDESTE :( o computador ganhou! ")

