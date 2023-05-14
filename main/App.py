while True:
    print('Conversor de BRL')
    print('[ 1 ] Dolar')
    print('[ 2 ] Euro')
    print('[ 3 ] Libras')
    print('[ 4 ] Kwanzas')
    print('[ 0 ] Sair')

    opcao = input('Escolha uma opção: ')

    if(opcao == '1'):
        real = float(input('Digite o valor em real: '))
        dolar = float(input('Digite o valor atual do Dolar: '))
        
        conversao = (real / dolar)

        print('R${} = ${:.2f} '.format(real, conversao))

    elif(opcao == '2'):
        real = float(input('Digite o valor em real: '))
        euro = float(input('Digite o valor atual do Euro'))

        conversao = (real / euro)

        print('R${} = €{:.2f} '.format(real, conversao))

    elif(opcao == '3'):
        real = float(input('Digite o valor em real: '))
        libras = float(input('Digite o valor atual das Libras'))

        conversao = (real / libras)

        print('R${} = £{:.2f} '.format(real, conversao))
    
    elif(opcao == '4'):
        real = float(input('Digite o valor em real: '))
        kwanzas = float(input('Digite o valor atual do Kwanzas: '))

        conversao = (real * kwanzas)

        print('R${} = Kz{:.2f} '.format(real, conversao))

    elif(opcao == '0'):
        print('Até logo!')
        break

    else:
        print('Opção inválida, tente novamente!')
