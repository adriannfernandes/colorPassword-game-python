import time
import bibSenha

print("Seja bem vindo(a) ao [JogoSenha]!")
print("Para uma melhor visualização do jogo aconselhamos que você deixe em [MODO TELA CHEIA]")
nome = str(input("Qual o nome do jogador? "))
informes = str.lower(input("Deseja ver as informações dos desenvolvedores desta versão {} ? ".format(nome)))
if (informes == "sim"):
    print('''             ____________________________________________
            |           >> Desenvolvedores <<            |
            |Adrian Ancelmo Fernandes da Silva           |
            |Idade: 21                                   |
            |Curso: Ciencia da Computação                |
            | And                                        |
            |Nathan José Farias de Almeida Barbosa       |
            |idade: 20                                   |   
            |Curso: Ciencia da Computação                |
            |____________________________________________|
            ''')
    
instrucao = str.lower(input("{}, deseja ler as instruções do jogo? ".format(nome)))
if(instrucao == "sim"):
    print('''
             ___________________________________________________
            |Objetivo do [JogoSenha]:                           |
            |-> O jogo irá criar uma senha de cores de 4 cores, |
            |   o jogador(a)terá 8 chances para acertar a senha |
            |   utilizando as dicas de acertos Totais e Parciais|
             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯''')


inicio = str.lower(input('''Deseja iniciar ao jogo {}?
[Sim]
[Não]                                              
Qual a sua opção? '''.format(nome)))            

while(inicio == "sim"):
    print('''
     _______________________________________________________________________
    |                   >>>{Instruções da pontuação}<<<                     |
    |Pontos TOTAIS significa acerto de Cor e Posição e conferem [7 Pontos]! |
    |Pontos PARCIAIS significa acerto apenas da Cor e conferem [3 Pontos]!  |
     ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯             
-------------------------------------------------------------------------------''')
    coresTotais = ["verde", "azul", "branco", "cinza", "ciano", "roxo"]
    contador = 8
    quantCoresSenha = 4
    pontuacao = 0
    senha = bibSenha.GerarSenha(coresTotais, quantCoresSenha)
    listaChute = []
    print("Cores disponiveis: {}".format(coresTotais))
    while contador != 0:
        contador -=  1
        for i in range(len(senha)):
            chute = str.lower(input("Digite a cor: "))
            listaChute.append(chute)
        validade = bibSenha.ValidarPalpite(listaChute,coresTotais)
        if(validade):
            testeVitoria = bibSenha.TestarVitoria (listaChute, senha)
            if testeVitoria:
                print("Parabéns {},você conseguiu acertar a sequência!!".format(nome))
                contador = 0
                inicio = str.lower(input("Deseja jogar novamente? "))
                
            else:
                posicao = bibSenha.TestarAcertosTotais(listaChute, senha)
                cor = bibSenha.TestarAcertosParciais(listaChute, senha)
                pontuacao += bibSenha.CalcularPontosGanhos (listaChute, senha)
                if(contador >= 1):
                    print("Infelizmente não foi dessa vez!! VOCÊ AINDA TEM {} CHANCES !!".format(contador))
                    if(cor - posicao >= 0):
                        print('''
                 ___________________
                | Acertos TOTAIS {}  |
                | Acertos PARCIAIS {}|
                 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ '''.format(posicao, cor - posicao))
                    else:
                        print('''
                 ___________________
                | Acertos TOTAIS {}  |
                | Acertos PARCIAIS {}|
                 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ '''.format(posicao, 0))
                
                if(contador == 0):
                    print("A senha era: {}".format(senha))
                    print("Seus pontos na rodada: {}".format(pontuacao))
                    print("{Acabou suas chances!!!}")                    
                    mensagem = bibSenha.DefinirMensagem(pontuacao)
                    print(mensagem)
                    
                    
                    inicio = str.lower(input("Deseja jogar novemente? "))
    
                listaChute = []
             
        else:
            contador = 0
            print("Seu palpite não é valido!!")
            inicio = str.lower(input("Deseja jogar novemente? "))
   
if(inicio != "sim"):
    print("Finalizando...")
    time.sleep(1)
    print("Tome um cartãozinho e volte sempre!! ")
    time.sleep(2)
    
