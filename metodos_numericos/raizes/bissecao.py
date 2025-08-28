import math as mt
from utils.conversor_str_funcao import conversor_str_funcao

def num_iteracoes(a, b, precisao):
    num_iteracoes = mt.ceil((mt.log(b - a) - mt.log(precisao))/ mt.log(2))
    return num_iteracoes

def entrada_funcao():
    try:
        funcao = input(">Digite a função (em termos de x): ")
        funcao_numerica = conversor_str_funcao(funcao, 'x')
        return funcao_numerica
    except Exception as e:
        print(f"Erro ao converter a função: {e}")
        return None

def entrada_intervalo():
    try:
        a = float(input(">Digite o limite inferior (a): "))
        b = float(input(">Digite o limite superior (b): "))
        return a, b
    except ValueError:
        print("Entrada inválida dos limites inválidas.")
        return None

def entrada_precisao():
    try:
        precisao = float(input(">Digite a precisão (Ex: 1e-5): "))
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
    a, b = entrada_intervalo()
    precisao = entrada_precisao()

    if funcao is None or a is None or b is None or precisao is None:
        print("Entrada inválida.")
        return None

    k_parada = num_iteracoes(a, b, precisao)
    print(f"Número de iterações necessárias: {k_parada}")

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
