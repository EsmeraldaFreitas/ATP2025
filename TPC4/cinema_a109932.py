## TPC4- CINEMA
# Modelo:
#   Cinema = [Sala]
#   Sala = [nlugares, vendidos, filme] 
#   nlugares = Int
#   vendidos = [lugar]
#   filme = String
#   lugar = Int

def menu():
    cinema = []
    v = True
    while v:
        print("""\n===== Menu =====
(1) Inserir Sala
(2) Listar Filmes
(3) Disponibilidade de Lugar
(4) Vender Bilhete
(5) Listar Disponibilidades
(0) Sair do Programa""")
        modo = int(input("Que modo deseja? "))
        if modo == 1:
            cinema = inserir_salas(cinema)
        elif modo == 2:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                listar_filmes(cinema)
        elif modo == 3:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                verificar_disponibilidade(cinema)
        elif modo == 4:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                cinema = vender_bilhetes(cinema)
        elif modo == 5:
            if len(cinema) == 0:
                print("Não há salas!")
            else:
                listar_disponibilidade(cinema)
        elif modo == 0:
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")


def existeFilme(cinema, filme):
    for sala in cinema:
        if sala[2].lower() == filme.lower():
            return True
    return False


def inserir_salas(cinema):
    filme = input("Nome do filme: ")
    if not existeFilme(cinema, filme):
        nlugares = int(input("Número total de lugares: "))
        sala = [nlugares, [], filme]
        cinema.append(sala)
        print(f"Sala com o filme '{filme}' adicionada com sucesso!")
    else:
        print("Já existe uma sala com esse filme!")
    return cinema


def listar_filmes(cinema):
    if len(cinema) == 0:
        print("Não existem salas registadas.")
    else:
        for sala in cinema:
            print(f"Filme em exibição: {sala[2]}")


def disponivel(cinema, filme, lugar):
    for sala in cinema:
        if sala[2].lower() == filme.lower():
            if lugar < 1 or lugar > sala[0]:
                print("Lugar inválido!")
                return False
            if lugar in sala[1]:
                print("Esse lugar já se encontra ocupado!")
                return False
            return True
    print("Filme não encontrado!")
    return False


def vender_bilhetes(cinema):
    filme = input("Filme: ")
    lugar = int(input("Lugar: "))
    novo_cinema = []
    for sala in cinema:
        if sala[2].lower() == filme.lower():
            if disponivel(cinema, filme, lugar):
                vendidos_novo = sala[1] + [lugar]
                print(f"Bilhete vendido para '{filme}', lugar {lugar}.")
            else:
                vendidos_novo = sala[1]
        else:
            vendidos_novo = sala[1]
        novo_cinema.append([sala[0], vendidos_novo, sala[2]])
    return novo_cinema


def listar_disponibilidade(cinema):
    if len(cinema) == 0:
        print("Não existem salas registadas!")
    else:
        for sala in cinema:
            disponiveis = sala[0] - len(sala[1])
            print(f"- {sala[2]}: {disponiveis} lugares disponíveis ({len(sala[1])} vendidos)")


def verificar_disponibilidade(cinema):
    filme = input("Filme: ")
    lugar = int(input("Lugar: "))
    if disponivel(cinema, filme, lugar):
        print("Lugar disponível!")
    else:
        print("Lugar indisponível.")


menu()