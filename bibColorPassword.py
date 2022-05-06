import random
coresTotais = ["verde", "azul", "branco", "cinza", "ciano", "roxo"]
    
def GerarSenha (coresTotais, quantCoresSenha):
    i = 0
    lista = []
    while i < quantCoresSenha:
        senha = random.choice(coresTotais)
        if senha in lista:
            continue
        else:
            lista.append(senha)
            i += 1
    return lista

def ValidarPalpite(listaChute, coresTotais):
    validacao = True
    for i in range(len(listaChute)):
        if(listaChute[i] in coresTotais) and (listaChute.count(listaChute[i]) == 1):
            continue
        else:
            validacao = False
    return validacao

def TestarVitoria (listaChute, senha):
    vitoria = True
    for i in range(len(senha)):
        if(listaChute[i] != senha[i]):
            vitoria = False
    return vitoria

def TestarAcertosTotais(listaChute, senha):
    quantPosicao = 0
    for i in range(len(senha)):       
        if(listaChute[i] == senha[i]):
            quantPosicao +=1
    return quantPosicao

def TestarAcertosParciais (listaChute, senha):
    quantParciais = 0
    for i in range(len(senha)):
        if(listaChute[i] in senha):
            quantParciais += 1
    return quantParciais

def CalcularPontosGanhos (listaChute, senha):
    parciais = (TestarAcertosParciais(listaChute, senha)- TestarAcertosTotais(listaChute, senha)) * 3
    totais = TestarAcertosTotais(listaChute, senha) * 7
    resultado = parciais + totais
    return resultado

def DefinirMensagem (pontuacao):
    menos20 = "Hum, você precisa melhorar seus palpites!"
    entre20e30 = "Seus palpites foram bons, continue assim!"
    mais30 = "Muito bom, você quase acertou! Talvez na próxima!"
    if(pontuacao < 20):
        return menos20
    elif(pontuacao > 19) and (pontuacao < 30):
        return entre20e30
    elif(pontuacao > 30):
        return mais30
