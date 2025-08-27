import sympy as sp
import math as mt

def conversor_str_funcao(funcao_str:str, variavel_str:str):
    try:
        variavel = sp.symbols(variavel_str)
        funcao = sp.sympify(funcao_str)
        funcao_num = sp.lambdify(variavel, funcao, modules=[mt])
        return funcao_num
    except (SyntaxError, sp.SympifyError) as e:
        print(f"Erro ao converter a função: {e}")
        return None