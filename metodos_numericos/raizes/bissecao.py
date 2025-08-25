def bissecao(funcao, a, b, precisao):
    if funcao(a) * funcao(b) >= 0:
        print("Intervalo inválido.")
        return None
    while (b - a) / 2 > precisao:
        ponto_medio = (a + b) / 2
        if funcao(ponto_medio) == 0:
            return ponto_medio
        elif funcao(a) * funcao(ponto_medio) < 0:
            b = ponto_medio
        else:
            a = ponto_medio
    return (a + b) / 2