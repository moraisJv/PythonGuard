# Validação do Nome
print("# Validação do Nome")
print("---------------------")

# Removemos o 'match' que quebrava o código
print("what's your first name?")
name = input("what's your first name? ")

if len(str(name)) > 100:
    print("your name is very long (lol)")
else:  # Agora com os dois-pontos (:) obrigatórios
    print("name is fine!")
      
# Validação do Número
print("\n# Validação do Número")
print("----------------------")

def validar_number():
    # Removemos o 'match:' e tiramos o ':' que estava no final do print
    print("what's your number? ")
    # Para guardar o valor usamos apenas um '='. O '==' serve apenas para testar se é igual.
    number = int(input("Enter number: ")) 
    return number

# Chamamos a função para ela rodar
validar_number()
 
# Validação do CPF (Corrigido 'rint' para 'print')
print("\n# Validação do CPF")
print("-------------------")

def validar_cpf():
    print("what's your CPF?")
    # Mudamos 'number' para uma frase de texto para o usuário entender o que digitar
    cpf = int(input("Enter CPF: "))
    # Corrigido de 'CPF' para 'cpf' para coincidir com a linha de cima (Python diferencia maiúsculas de minúsculas)
    print(f"Processo concluído para o CPF: {cpf}")

validar_cpf()
    
# Validação de Senha
print("\n# Validação da senha")
print("--------------------")

def validar_password():
    print("what's your password?")
    password = input("what's your password? ")

    # Se a pessoa digitar "python", ela fica presa no loop pedindo outra senha
    while password == "python":
        print("Sua senha não pode ser 'python'!")
        password = input("password: ")
    
    # Se a senha for diferente de "python", sai do loop e mostra que está tudo bem
    print("fine!")

validar_password()

 # hello world, this code was made for 1337(me), he is a god students btw !
 # this code was made for ETEC Uirapuru student
