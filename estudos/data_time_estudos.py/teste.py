from datetime import datetime
import calendar



print('Escolhas as opcoes abaixo')
valores_permitidos = ['1', '2', '3', '4']

while True:
    opcao = input('[1]`ver o tempo atual [2]exit  [3]olhar o calendario [4]dia de amanha')
    
    if opcao == '1':
        print(datetime.now())
    elif opcao == '2':
        break

    elif opcao == '3':
        try:
            calendario = int(input('Insira o ano do seu calendario: '))
            print(calendar.calendar(calendario))

            if calendar.isleap(calendario):
                print('o ano é bisexto')
            else:
                print('O ano nao é bisexto')

        except ValueError:
            print('digite um valor valido')

    elif opcao == '4':
        dia_atual = calendar.monthrange(2024, 32)
        print(dia_atual)

    elif opcao not in valores_permitidos:
        print('Digite apenas os valores permitidos')
    




