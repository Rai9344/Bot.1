import os

def processar_resposta(resposta, name):
    if resposta == '1':
        print(f'''{os.linesep}  A luz é um tipo de onda eletromagnética visível,
formada pela propagação em conjunto de um campo elétrico e um magnético.
Como é característico da radiação eletromagnética, a luz pode propagar-se através de diversos meios
e sofrer alterações de velocidade ao passar de um meio de propagação para outro.
No vácuo, a luz possui velocidade máxima equivalente a 3,0 x 10 8 m/s.''')
    elif resposta == '2':
        print('''
        O que é buraco negro
Buraco negro é uma região do espaço-tempo em que o campo gravitacional é tão intenso que nada — nenhuma
partícula ou radiação eletromagnética como a luz — pode escapar dela.
A teoria da relatividade geral prevê que uma massa suficientemente compacta pode deformar o
espaço-tempo para formar um buraco negro.
        ''')
    elif resposta == '3':
        print('''
       O que é anã-branca
Uma estrela anã branca é o produto final da evolução da vida de uma estrela.
As dimensões de um tal objeto, tal como o seu nome deixa antever, são reduzidas,
aproximando-se do tamanho da Terra. No entanto a sua massa poderá ser maior ainda que a do nosso Sol.
        ''')
    elif resposta == '4':
        print(''' {}
        Espaço-Tempo
Um novo estudo, publicado na revista Science, declara que a maneira como o tecido espaço-tempo gira
em um redemoinho cósmico em torno de uma estrela morta confirma mais uma previsão da Teoria da
Relatividade Geral de Einstein.
Essa previsão, conhecida como arrasto de quadros ou efeito Lense-Thirring, afirma que o espaço-tempo
vai se mover em torno de um corpo massivo e rotativo. Por exemplo, se à Terra estivesse submersa em
mel, à medida que o planeta girasse, o mel ao redor iria se movimentar também – o mesmo conceito se
aplica ao espaço-tempo.
        ''')
    else:
        print('digite apenas 1, 2, 3, 4')
def start():
        #apresentar o chartbot
        print('ola bem vindo ao cienciaRai.com')
        #pedir nome
nome = input('digite seu nome: ')
        #pedir e-mail
email = input('seu e-mail: ')
while True:
    # Oferece o menu de opções
    resposta = input(
    f'O que gostaria de saber hoje?{os.linesep}[1] - O que é luz?{os.linesep}[2] - O que é Buraco Negro?{os.linesep}[3] - O que é Anã-Branca?{os.linesep}[4] - O que Espaço-Tempo?{os.linesep}')
    #processar a resposta enviada
    processar_resposta(resposta, nome)

if __name__ == '_main_':
         start()