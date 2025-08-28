# Métodos Numéricos em Python

Este projeto implementa vários métodos numéricos em Python, oferecendo uma interface de linha de comando para interagir com eles.

## Funcionalidades

O projeto atualmente inclui os seguintes métodos:

-   **Cálculo de Raízes de Funções:**
    -   Método da Bisseção

O menu principal também inclui placeholders para:
-   Método de Newton (em desenvolvimento)
-   Método da Secante (em desenvolvimento)

## Dependências

O projeto utiliza as seguintes bibliotecas Python:

-   `numpy`
-   `scipy`
-   `sympy`
-   `matplotlib`

A lista completa de dependências está no arquivo `requirements.txt`.

## Instalação

1.  **Clone o repositório (caso ainda não tenha feito):**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd uniube/metodos_numericos
    ```

2.  **Crie e ative um ambiente virtual:**
    É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

    ```bash
    # Criar o ambiente virtual
    python -m venv .venv

    # Ativar no Linux/macOS
    source .venv/bin/activate

    # Ativar no Windows (PowerShell)
    # .\.venv\Scripts\Activate.ps1
    ```

3.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o `pip`.

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

Para executar o programa, simplesmente rode o arquivo `main.py` a partir do diretório `metodos_numericos`:

```bash
python main.py
```

Você será apresentado a um menu para escolher o método numérico que deseja utilizar.
