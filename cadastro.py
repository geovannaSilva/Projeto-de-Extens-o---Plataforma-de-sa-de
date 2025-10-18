print('== SISTEMA CLÍNICA VIDA+ ==')

import time

qtd_cadastros = 0
idades = []
pacientes = []

while True:
    print("\nInforme a opção desejada:")
    print('\n1.Cadastrar paciente'
          '\n2.Ver estatística'
          '\n3.Buscar paciente'
          '\n4.Listar todos os pacientes'
          '\n5.Sair')

    try:
        escolha = int(input('\nEscolha uma opção:'))
    except(ValueError):
        print("Digite um valor válido.")

        # Pequena pausa entre as telas
        time.sleep(0.6)

    if escolha==1:
        qtd_cadastros += 1

        nomepaciente = str(input('\nNome do paciente: '))
        idade = int(input('Idade: '))
        idades.append((idade))
        telefone = str(input('Telefone: '))


        pacientes.append({"nome": nomepaciente, "idade": idade, "telefone":telefone})

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

    if escolha == 3:
        if pacientes:
            busca_paciente = str(input("\nDigite o nome do paciente que deseja buscar: "))
            encontrado = False

            for p in pacientes:
                if p["nome"].strip().lower() == busca_paciente.strip().lower():
                    print(f"Paciente encontrado: \n"f"{p['nome']} \n{p['idade']} anos \n{p['telefone']}")
                    encontrado = True

            if not encontrado:
                print(f"O Paciente {busca_paciente} não foi cadastrado!")


    if escolha == 4:
        print(f"\nOs pacientes cadastrados são: \n{pacientes}")


    if escolha == 5:
        # Pequena pausa para encerramento
        time.sleep(0.6)
        print('\nPrograma encerrado!')
        break
