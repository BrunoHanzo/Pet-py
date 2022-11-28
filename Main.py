from Menu import Menu
from Choices import Choices

while True:
    Menu.MenuPrincipal()
    opcao_menu = input().upper()
    if opcao_menu == 'E':
        print('FIM DO PROGRAMA!')
        print('OBRIGADO E VOLTE SEMPRE!!')
        break
    elif opcao_menu not in 'CSF':
        print('OPÇÃO INVÁLIDA!')
    else:
        choice = Choices(0)
        if opcao_menu == 'C':
            choice.choice_cliente()

        elif opcao_menu == 'S':
            choice.choice_servicos()

        elif opcao_menu == 'F':
            choice.choice_financeiro()



