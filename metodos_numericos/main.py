from raizes.bissecao import bissecao
from utils.conversor_str_funcao import conversor_str_funcao

def menu():
    print("Escolha um método numérico:")
    print("1. Método da Bisseção")
    print("2. Método de Newton")
    print("3. Método da Secante")
    opcao = input("Digite o número da opção desejada: ")
    return opcao

def main():
    opcao = menu()
    match opcao:
       case "1":
           bissecao()
       case "2":
           print("Ainda em desenvolvimento")
       case "3":
           print("Ainda em desenvolvimento")
           
       case _:
           print("Opção inválida.")

if __name__ == "__main__":
    main()