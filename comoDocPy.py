##EXEMPLO 01
##Antes

C = 0
i = 0
t = 0

M = C * (1 + i) ^ t

##Depois > comentario e organização no codigo com uma nova abordagem

# Montante com juros compostos:
m1 = lambda pa, r, t: pa * (1 + r)**t

##EXEMPLO 02
##Antes

def calculate_compound_interest_investment(pa, r, t):
    return pa * (1 + r)**t

##Depois > variaveis bem escritas e diretas

def calculate_compound_interest_investment(
    principal_amount, rate, time
):
    return principal_amount * (1 + rate)**time

##EXEMPLO 03
## DOCSTRINGS
## sempre estará localizada na primeira linha do mesmo,
## dentro de 3 aspas duplas para abrir e 3 para fechar

def calculate_compound_interest_investment(
    principal_amount, rate, time
):
    """
    Returns the compound interest an accrued amount that includes
    principal plus interest.

    :param principal_amount: float
    :param rate: float
    :param time: int

    :return float principal_amount * (1 + rate)**time:
    """
    return principal_amount * (1 + rate)**time

## As docstring ficam salvas no método mágico __doc__ das funções e classes que as implementam.
##print(calculate_compound_interest_investment.__doc__)

##EXEMPLO 03
## anotações e type hints

def multiplica(x: float, y: float) -> float:
    return x * y
multiplica(4, "e")
