from utils.conversor_str_funcao import conversor_str_funcao
from utils.conversor_str_funcao import derivada_funcao

def entrada_funcao():
    try:
        funcao = input(">Digite a função (em termos de x) ou 'sair' para finalizar: ")
        if funcao.lower() == "sair":
            return "sair"
        funcao_numerica = conversor_str_funcao(funcao, 'x')
        funcao_derivada = derivada_funcao(funcao, 'x')
        return funcao_numerica, funcao_derivada
    except Exception as e:
        print(f"Erro ao converter a função: {e}")
        return None

def entrada_ponto_inicial():
    try:
        x0 = input(">Digite o ponto inicial (x0) ou 'sair' para finalizar: ")
        if x0.lower() == "sair":
            return "sair"
        
        x0 = float(x0)
        return x0
    except ValueError:
        print("Entrada inválida do ponto inicial.")
        return None

def entrada_precisao():
    try:
        precisao = input(">Digite a precisão (Ex: 1e-5) ou 'sair' para finalizar: ")
        if precisao.lower() == "sair":
            return "sair"
        
        precisao = float(precisao)

        if precisao <= 0:
            raise ValueError
        
        return precisao
    except ValueError:
        print("Entrada inválida.")
        return None
    
def tabela_newton_raphson():
    print("Tabela de Newton-Raphson")
    print("="*80)
    print("|Iteração| ===== |x0| ===== |f(x0)| ===== |f'(x0)| ===== |x1|")
    print("="*80)

def imprimir_resultado(iteracao, x0, fx0, dfx0, x1):
    print(f"|{iteracao}| ===== |{x0:.4f}| ===== |{fx0:.4f}| ===== |{dfx0:.4f}| ===== |{x1:.4f}|")
    print("="*80)

def newton_raphson():
    funcao, funcao_derivada = entrada_funcao()
    while funcao != "sair" and funcao is None:
        print("Função inválida, digite corretamente a função.")
        funcao = entrada_funcao()
    if funcao == "sair":
        print("Finalizando...")
        return None

    x0 = entrada_ponto_inicial()
    while x0 != "sair" and x0 is None:
        print("Ponto inicial inválido. Digite novamente.")
        x0 = entrada_ponto_inicial()
    if x0 == "sair":
        print("Finalizando...")
        return

    precisao = entrada_precisao()
    while precisao != "sair" and precisao is None:
        print("Precisão inválida. Digite novamente.")
        precisao = entrada_precisao()
    if precisao == "sair":
        print("Finalizando...")
        return

    tabela_newton_raphson()