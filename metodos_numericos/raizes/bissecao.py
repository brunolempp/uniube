import math as mt
from utils.conversor_str_funcao import conversor_str_funcao

def num_iteracoes(a, b, precisao):
    num_iteracoes = mt.ceil((mt.log(b - a) - mt.log(precisao))/ mt.log(2))
    return num_iteracoes

def entrada_funcao():
    try:
        funcao = input(">Digite a função (em termos de x) ou 'sair' para finalizar: ")
        if funcao.lower() == "sair":
            return "sair"
        funcao_numerica = conversor_str_funcao(funcao, 'x')
        return funcao_numerica
    except Exception as e:
        print(f"Erro ao converter a função: {e}")
        return None

def entrada_intervalo():
    try:
        a = input(">Digite o limite inferior (a) ou 'sair' para finalizar: ")
        b = input(">Digite o limite superior (b) ou 'sair' para finalizar: ")

        if a.lower() == "sair" or b.lower() == "sair":
            return "sair", "sair"
        
        a = float(a)
        b = float(b)

        if a >= b:
            raise ValueError("O limite inferior deve ser menor que o limite superior.")
        return a, b
    except ValueError:
        print(f"Entrada inválida dos limites.: {ValueError}")
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

def tabela_bissecao():
    print("Tabela de Bisseção")
    print("="*80)
    print("|Iteração| ===== |a| ===== |b| ===== |xn| ===== |f(a)| ===== |f(xn)|")
    print("="*80)

def imprimir_resultado(iteracao, a, b, xn, fa, fxn):
    print(f"|{iteracao}| ===== |{a:.4f}| ===== |{b:.4f}| ===== |{xn:.4f}| ===== |{fa:.4f}| ===== |{fxn:.4f}|")
    print("="*80)


def bissecao():

    funcao = entrada_funcao()
    while funcao != "sair" and funcao is None:
        print("Função inválida, digite corretamente a função.")
        funcao = entrada_funcao()
    if funcao == "sair":
        print("Finalizando...")
        return None
    
    a, b = entrada_intervalo()
    while a != "sair" and b != "sair" and (a is None or b is None or funcao(a) * funcao(b) > 0 or a >= b):
        print("Intervalo inválido. f(a) e f(b) devem ter sinais opostos.")
        a, b = entrada_intervalo()
    if a == "sair" or b == "sair":
        print("Finalizando...")
        return None

    precisao = entrada_precisao()
    while precisao != "sair" and precisao is None:
        print("Precisão inválida. Digite novamente.")
        precisao = entrada_precisao()
    if precisao == "sair":
        print("Finalizando...")
        return None

    k_parada = num_iteracoes(a, b, precisao)
    print(f"Número de iterações máxima: {k_parada}")

    tabela_bissecao()

    for k in range(1, k_parada + 1):
        xn = (a + b) / 2
        fxn = funcao(xn)
        fa = funcao(a)

        imprimir_resultado(k, a, b, xn, fa, fxn)

        if abs(fxn) < precisao:
            print(f"Solução encontrada: x = {xn:.4f}, f(x) = {fxn:.4f}")
            return xn

        if fa * fxn < 0:
            b = xn
        else:
            a = xn

    print("Número máximo de iterações atingido.")
    return None
