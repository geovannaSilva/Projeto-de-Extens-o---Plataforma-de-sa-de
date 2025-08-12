print('== SISTEMA CLÍNICA VIDA+ ==')

qtd_cadastros = 0
idades = []
pacientes = []

while True:
    print('\n1.Cadastrar paciente\n'
          '2.Ver estatística\n'
          '3.Buscar paciente\n'
          '4.Listar todos os pacientes\n'
          '5.Sair')

    escolha = int(input('Escolha uma opção:'))

    if escolha==1:
        qtd_cadastros += 1

        nomepaciente = str(input('\nNome do paciente: '))
        idade = int(input('Idade: '))
        idades.append((idade))
        telefone = str(input('Telefone: '))

        pacientes.append({"nome": nomepaciente, "idade": idade})

        print('\nPaciente cadastrado com sucesso!')

    if qtd_cadastros > 0:
        media = sum(idades) / qtd_cadastros

        #paciente mais novo
        pac_novo = min(pacientes, key=lambda p: p["idade"])

        #paciente mais velho
        pac_velho = max(pacientes, key=lambda p: p["idade"])

    if escolha == 2:
        print('\nEstatísticas:')
        print(f'Foram cadastrados {qtd_cadastros} pacientes.')
        print(f'A idade média dos pacientes é: {media}')
        print(f'O paciente mais novo é {pac_novo['nome']} e tem {pac_novo['idade']} anos.')
        print(f'O paciente mais velho é {pac_velho['nome']} e tem {pac_velho['idade']} anos')

    if escolha == 5:
        print('\nSainda do programa...')
        break