
tabMeteo = [((2022,1,20), 2, 16, 0), ((2022,1,21), 1, 13, 0.2), ((2022,1,23), 6, 19, 0.6), ((2022,1,24), 3, 18, 0.8),((2022,2,20), 6, 19, 0.2), ((2022,2,24), 3, 18, 0.2), ((2022,2,28), 3, 18, 0.2)]

def menu():
    cond=True
    while cond:
        modo=int(input("""
    - 1: Calcular temperatura média;
    - 2: Guardar tabela metereologica num ficheiro;
    - 3: Listar a tabela metereologica do ficheiro;
    - 4: Calcular temperatura mínima;
    - 5: Calcular amplitude térmica;
    - 6: Calcular o dia da precipitação máxima;
    - 7: Dias em que a precipitação foi superior ao limite p;
    - 8: Dias consecutivos em que a precipitação foi inferior ao limite p;
    - 9: Desenhar os gráficos da temperatura mínima, máxima e de pluviosidade.
    - 0: Sair da aplicação
             """))
        if modo==1:
            print(medias(tabMeteo))
        elif modo==2:
            guardaTabMeteo(tabMeteo, "meteorologia.txt")
        elif modo==3:
            carregaTabMeteo("meteorologia.txt")
        elif modo==4:
            print(minMin(tabMeteo))
        elif modo==5:
            print(amplTerm(tabMeteo))
        elif modo==6:
            print(maxChuva(tabMeteo))
        elif modo==7:
            p=float(input("Qual o limite de precipitação que quer?"))
            print(diasChuvosos(tabMeteo, p))
        elif modo==8:
            p=float(input("Qual o limite de precipitação que quer?"))
            print(maxPeriodoCalor(tabMeteo, p))
        elif modo==9:
            grafTabMeteo(tabMeteo)
        elif modo == 0:
            print("Programa Encerrado.")
            cond = False
        else:
            print("Insira um modo válido!")


def medias(tabMeteo):
    res = []
    for i in tabMeteo:
        temp_media=(i[1]+i[2])/2
        lista=(i[0], temp_media)
        res.append(lista)
    return res

def guardaTabMeteo(t, fnome):
    f=open(fnome, "w")
    for data, tmin ,tmax ,prec in t:
        ano, mes, dia= data
        f.write(f"{ano}-{mes}-{dia} ; {tmin}; {tmax}; {prec}\n")
    f.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file=open(fnome, "r")
    for line in file:
        print(line)
        line=line.strip()
        campos = [x.strip() for x in line.split(";")]
        data, tmin, tmax, prec= campos
        ano, mes, dia = data.split("-")
        tuplo=((int(ano), int(mes), int(dia)), float(tmin), float(tmax), float(prec) )
        res.append(tuplo)
    file.close()
    return res

def minMin(tabMeteo):
    temp_min=tabMeteo[0][1]
    for i in tabMeteo:
        if temp_min>i[1]:
            temp_min=i[1]
    return temp_min 

def amplTerm(tabMeteo):
    res = []
    for i in tabMeteo:
        temp_max=i[2]
        temp_min=i[1]
        amptemp= temp_max-temp_min
        res.append((i[0], amptemp))
    return res 

def maxChuva(tabMeteo):
    max_prec=tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for i in tabMeteo:
        if max_prec<i[3]:
            max_prec=i[3]
            max_data=i[0]
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    for i in tabMeteo:
        if i[3]>p:
            tuplo=(i[0], i[3])
            res.append(tuplo)
    return res

def maxPeriodoCalor(tabMeteo, p):
    maior=0
    atual=0
    for i in tabMeteo:
        if i[3] < p:     
            atual = atual +1
            if atual > maior:
                maior = atual
        else:
            atual = 0    
    return maior


from matplotlib import pyplot as plt
def grafTabMeteo(t):
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    ytmin=[tmin for data, tmin, tmax, prec in t]
    ytmax=[tmax for data, tmin, tmax, prec in t]
    y_prec=[prec for *_, prec in t]


    plt.plot(x,ytmin, label="Temperatura Mínima (ºC)", color="blue", marker="o")
    plt.plot(x,ytmax, label="Temperatura Máxima (ºC)", color="red", marker="o")
    plt.legend()
    plt.title("Tabela Metreológica")
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

    plt.bar(x,y_prec)
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
    return

menu()