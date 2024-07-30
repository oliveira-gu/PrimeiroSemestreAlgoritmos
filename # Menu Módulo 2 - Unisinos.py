# Menu Módulo 2 - Unisinos
def get_menu_options():
    menu_options = ('1','2','3','4','5','6','7')
    while True:
        print('Olá fulano')
        print('Digite a opção desejada: ')
        print('1 ) Verificar triângulo')
        print('2 ) Calcular equação do segundo grau')
        print('3 ) Conferir data')
        print('4 ) Verificar tamanho do texto')
        print('5 ) Analisar CPF')
        print('6 ) Contar caracteres')
        print('7 ) Sair')
        print()
        user_input = input("Digite a opção desejada: ")
        if user_input in menu_options:
            return user_input 
        else:
            print()
            print("Opção não disponível! Tente novamente: ")
while True:
    user_input = get_menu_options()
    if user_input == '1':
        print()
        print("Opção 1: Verifcar triângulo")
        def triangulo_valido (a,b,c): 
            if (a+b<c and b+c<a and c+a<b):
                return True
            else:
                return False       
        a = float(input("Digite o valor de um dos lados: "))
        b = float(input("Digite o valor do outro lado: "))
        c = float(input("Digite o valor do outro lado: "))
        if (a < b + c and b < c + a and c < a + b):
            if (a == b and b == c):
                print("É um triângulo equilátero")
            else:
                if (a == b or b == c or c == a):
                    print("É um triângulo isóseles")
                else:
                    print("É um triângulo escaleno")
        else:
            print("Não é um triângulo")
        print()
    elif user_input == '2':
        print()
        print("Opção 2: Calcular equação do segundo grau")
        def baskara (a,b,c):
            delta = (b**2) - (4*a*c)
            x1 = (((-1)*b) + (delta**0.5))/(2*a)
            x2 = (((-1)*b) - (delta**0.5))/(2*a)
            if delta > 0:
                print("Como Delta > 0, temos dois valores diferentes de raízes:", x1, x2 )
                2
            elif delta == 0:
                print("Nossa equação só possui uma raiz real:",x1)
            else:
                print("Como Delta < 0, não temos raízes reais!")
        a = float(input("Digite o valor de a: "))
        if a == 0:
                print("Não se trata de uma equação do segundo grau")
                print()
                continue
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        baskara(a,b,c)
        print()
    elif user_input == '3':
        print()
        print("Opção 3: Conferir data")       
        def contagemData (dia,mes,ano):
            meses = ["janeiro","fevereiro","março","abril","maio","junho",
                    "julho","agosto","setembro","outubro","novembro","dezembro"]
            list30 = ["abril","junho", "setembro","novembro"]
            list31 = ["fevereiro","março","maio","julho","agosto","outubro","dezembro"]           
            if dia == "28" and mes == "janeiro":
                print("A data está correta")
            elif dia == "30" and mes in list30:
                print("A data está correta")
            elif dia == "31" and mes in list31:
                print("A data está correta")
            else:
                print("A data não está correta")
        dia = (input("Digite o dia: "))
        mes = (input("Digite o mês: "))
        ano = (input("Digite o ano: "))
        contagemData(dia,mes,ano)
        print()
    elif user_input == '4':
        print()
        print("Verificar tamanho do texto")
        texto = input("Digite o seu texto aqui: ")
        texto_tamanho = len(texto)
        if texto_tamanho < 5:
            print("Texto é muito pequeno, pois contém menos de 5 caracteres.")
        elif texto_tamanho >= 5 and texto_tamanho < 15:
            print("Texto é tamanho médio, pois contém entre 5 e 15 caracteres.")
        elif texto_tamanho >= 15 and texto_tamanho < 20:
            print("Texto é grande, pois contem entre 15 e 20 caracteres.")
        else: 
            print("O texto é inválido, pois contém mais de 20 caracteres.")
        print()
    elif user_input == '5':
        print("Opção 5: Analisar CPF")
        def contadorCpf (cpf):
            y = cpf.isdigit()
            if (len(cpf)==11) and y == True:
                print("CPF é válido")
            else:
                print("CPF é inválido")
        cpf = input("Digite o seu CPF (sem pontuação ou traços): ")
        contadorCpf(cpf)
        print()
    elif user_input == '6':
        print("Opção 6: Contar caracteres")
        vogal = 0
        espaco = 0
        outrosCaracteres = 0
        texto = input("Digite um texto: ")
        for letra in texto:
            if letra in "aeiou":
                vogal += 1
            elif letra in " ":
                espaco += 1
            else:
                outrosCaracteres += 1
        print("O texto contém {} vogais, {} espaços e {} (consoantes e caracteres especiais)".format(vogal,espaco,outrosCaracteres))
        print()
    elif user_input == '7':
        print()
        print("Obrigado por utilizar nosso sistema.")
        exit()