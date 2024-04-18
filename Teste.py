senha = 1234
saldo_atual = 0
passagem = 6
passagem_reserva = 6
contador = 2
acesso = True
confirma_senha = 0
domingo = False
tarifa_domingo = passagem * 0.5
while acesso == True:
    usuario = int(input('Qual é o seu cartão de acesso?\n'
                        'Usuário - 1\n'
                        'Administrador - 2\n'
                        'Sair - 3\n'))
    menu1, menu2 = True, True
    if usuario == 1:
        while menu1:
            menu1 = int(input('Seja bem-vindo, usuário!\n'
                              'O que deseja fazer?\n'
                              'Recarregar cartão - 1\n'
                              'Usar cartão - 2\n'
                              'Voltar - 3\n'))
            if menu1 == 1:
                saldo_recarga = float(input('Quantos créditos gostaria de recarregar?\n'))
                saldo_atual += saldo_recarga
                print(f'Novo saldo: {saldo_atual:.2f} créditos\n')

            elif menu1 == 2:
                if saldo_atual < passagem:
                    print('Você não possui saldo suficiente para essa transação\n')
                else:
                    print(f'Novo saldo {saldo_atual - passagem:.2f} créditos.\n')
                    saldo_atual = saldo_atual - passagem
            elif menu1 == 3:
                menu1 = False
            else:
                print(f'Opção inválida. Tente novamente.\n')
                continue

    elif usuario == 2:
        confirma_senha = int(input('Por favor, digite sua senha.\n'))
        while senha != confirma_senha:
            if contador > 0:
                print(f'Senha incorreta. {contador} tentativas restantes.\n')
                confirma_senha = int(input('Por favor, digite sua senha novamente.\n'))
                if senha == confirma_senha:
                    contador = 2
                    pass
                contador = contador - 1
            elif contador == 0:
                break
        if contador == 0:
            print('Tentativas excedidas, tente novamente mais tarde.\n')

        elif confirma_senha == senha:
            contador = 2
            while menu2:
                menu2 = int(input('Seja bem-vindo, administrador!\n'
                                  'O que deseja fazer?\n'
                                  'Visualizar créditos - 1\n'
                                  'Atualizar valor da passagem - 2\n'
                                  'Tarifa de Domingo - 3\n'
                                  'Voltar - 4\n'))
                if menu2 == 1:
                    print(f'O cartão possui {saldo_atual} créditos.\n')

                elif menu2 == 2:
                    if domingo == False:
                        passagem = float(input('Qual o novo valor da passagem?\n'))
                        print(f'O valor da passagem foi definido para {passagem}\n')
                        passagem_reserva = passagem
                        tarifa_domingo = passagem * 0.5
                        print(f'Se hoje fosse domingo, a passagem seria {tarifa_domingo}\n')
                    elif domingo == True:
                        passagem = float(input('Qual o novo valor da passagem?\n'))
                        print(f'O valor da passagem foi definido para {passagem}\n')
                        passagem_reserva = passagem
                        tarifa_domingo = passagem * 0.5
                        passagem = tarifa_domingo
                        print(f'Como hoje é domingo, a passagem será {passagem}\n')
                elif menu2 == 3:
                    if domingo == False:
                        domingo = True
                        passagem = tarifa_domingo
                        print('Tarifa de Domingo Ativada.\n')
                    else:
                        domingo = False
                        passagem = passagem_reserva
                        print('Tarifa de Domingo Desativada.\n')
                    pass
                elif menu2 == 4:
                    menu2 = False
                else:
                    print(f'Opção inválida. Tente novamente.\n')
                    continue
    elif usuario == 3:
        acesso = False
    else:
        print('Opção Inválida. Tente novamente.\n')
