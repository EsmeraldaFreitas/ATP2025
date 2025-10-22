def menu():
    cond=True
    while cond:
        modo=int(input("""
    - 1: Criar uma turma;
    - 2: Inserir um aluno na turma;
    - 3: Listar a turma;
    - 4: Consultar um aluno por id;
    - 5: Guardar a turma em ficheiro;
    - 6: Carregar uma turma dum ficheiro;
    - 0: Sair da aplicação
             """))
        if modo==1:
            turma=criarturma()
        elif modo==2:
            inseriraluno(turma)
        elif modo==3:
            listarturma(turma)
        elif modo==4:
            consultarid(turma)
        elif modo==5:
            fnome="turmainfo"
            guardarturma(turma, fnome)
        elif modo==6:
            fnome="turmainfo"
            carregarturma(fnome)
        elif modo == 0:
            print("Programa Encerrado.")
            cond = False
        else:
            print("Insira um modo válido!")

#`aluno = (nome, id, [notaTPC, notaProj, notaTeste])`

#`turma = [aluno]`

def criarturma():
    Turma=[]
    return Turma

def inseriraluno(Turma):
    nome=input("Insira o nome do aluno que deseja inserir: ")
    id=int(input("Insira o id do aluno que deseja inserir: "))
    notaTPC=float(input("Insira a nota do Tpc : "))
    notaProj=float(input("Insira a nota do projeto : "))
    notaTeste=float(input("Insira a nota do teste: "))
    Turma.append((nome,id,[notaTPC, notaProj, notaTeste]))
    return Turma

def listarturma(Turma):
    for aluno in Turma:
        print(f" O aluno {aluno[0]} com id {aluno[1]} teve uma nota de {aluno[2][0]} no TPC, {aluno[2][1]} no projeto e {aluno[2][2]} e no teste.")
    return 

def consultarid(Turma):
    consultar=int(input("Qual o ID do aluno que quer consultar? "))
    for aluno in Turma:
        if consultar==aluno[1]:
            print(f"O aluno de ID {consultar} chama-se: {aluno[0]} ")
        else:
            print("Não existe um aluno com esse ID!")
    return 

def guardarturma(Turma, fnome):
    file = open(fnome,"w") # "r", "w"
    res= ""
    for p in Turma:
        for termo in Turma:
            aluno ,id, nota = termo
            res= res+ str(aluno) + ";" + str(id) + ";" + str(nota) + "|" 
        res= res + "\n"
    file.write(res)
    file.close()
    return 

def carregarturma(fnome):
    Turma = []
    file = open(fnome,"r")
    text =file.read()
    Turma_text = text.split("\n")
    for p_texte in Turma_text[:-1]:
        listap=[]
        termos_text=p_texte.split("|")
        for t_text in termos_text[:-1]:
            nome, id, nota =t_text.split(";")
            termo=(str(nome), int(id), list(nota) )
            listap.append(termo)
        Turma.append(termo)
    file.close()
    return Turma

menu()