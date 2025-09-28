# Tpc2- Jogo dos Fósforos
## nível 1- computador joga em 1 lugar
### O jogo consiste em ir tirando fósforos (1,2,3 ou 4) de um total de 21 à vez alternando com o computador e o último jogador a tirar fósforos perde.

print ("Jogo dos Fósforos-nível 1")
total=21
sabe_jogar=input("Sabes como funciona o jogo? responde com s ou n? ")
while sabe_jogar!= "s" :
    print ("O jogo consiste em ir tirando fósforos (1,2,3 ou 4) de um total de 21, à vez, alternando com o computador e o último jogador a tirar fósforos perde.")
    sabe_jogar=input("Já sabes como funciona o jogo? responde com s ou n? ")
while total>1:
        if total%5!=1 : 
            pc=(total-1)%5
            if pc==0:
                pc=1
        else:
            pc= 1
        total=total-pc
        if total==1:
            print(f"O computador retirou {pc} fósforos!")
            print ("Há 1 fósforo, logo és o último a retirar o fósforo, PERDESTE :( o computador ganhou! ")
        else:
            print(f"O computador retirou {pc} fósforos! Há {total} fósforos! ")
            num=int(input (f"Temos {total} fósforos, quantos queres tirar? "))
            while num!=1 and num!=2 and num!=3 and num!=4 :
                print ("O número que introduziste não se encontra entre 1 e 4, por favor insere um número válido!")
                num=int(input (f"Temos {total} fósforos, quantos queres tirar? "))
            total=total-num
            print(f"Restiraste {num} agora temos {total} fósforos!")
            
            
