'''


CRUD


Barbearia

Organizar e gerenciar clientes, agendamentos 
e serviços por meio das operações de cadastro,
consulta, atualização e exclusão de dados.

'''

print('Hello world!')

# input('Precione o Enter para sair...')

nome_cliente = input('inserir seu nome:')


print(f'Olá, {nome_cliente}! Seja bem-vindo(a) a nossa barbearia!')



nome_conta = input ('Digite sua conta:')
print(f'{nome_conta} Correto agora entre com sua senha ')
input  ('Digite sua senha:')

nome_cliente = print ('Acesso permitido')


print("\n=== BARBEARIA ===")
print("1. Cadastrar Cliente")
print("2. Agendar Serviço")
print("3. Meus Agendamentos")
print("4. Serviços e Preços")
print("5. Escolher Barbeiro")
print("6. Histórico e Pagamentos")
print("7. Avaliações")
print("8. Notificações")
print("0. Sair")

escolha = input("\nEscolha uma opção: ")


while True:

    escolha_menu = input("\nEscolha uma opção: ")
    if escolha_menu =='1':

        print("cadastrando cliente...")
        nome_cliente = input("digite o nome do cliente: ")
        telefone_cliente = input("digite o telefone do cliente:" )


    elif escolha_menu =='2':
        print("perfil do cliente")  
        nome_cliente = input("nome completo do cliente:")
        nome_cliente = input("produtos que o cliente prefere:")





    elif escolha_menu == '0':

        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")



   










