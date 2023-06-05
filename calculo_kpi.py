"""
Dados das empresas:
                          XPTO           YZTO
DIAS                       360            360
RECEITA LIQUIDA          10000          10000
CUSTOS                    7000           7000
ESTOQUES                   100            600
CONTAS A RECEBER           100            600
FORNECEDORES               600            100

PME = PRAZO MEDIO DE ESTOQUES(INICIA NA COMPRA DO MATERIAL E TERMINA NA VENDA DO PRODUTO)
PMR = PRAZO MEDIO DE RECEBIMENTOS(INICIA NA VENDA DO PRODUTO E TERMINA NO RECEBIMENTO)
PMP = PRAZO MEDIO DE PAGAMENTOS(INICIA NA COMPRA DO FORNECEDOR E TERMINA NO PAGAMENTO AO FORNECEDOR)
C.O = CICLO OPERACIONAL
C.C - CICLO DE CAIXA

"""

dias = 360
pme1 = []
pmr1 = []
pmp1 = []
co1 = []
cc1 = []


def pme():
    estoque = float(input('Informe o estoque:'))
    custos = float(input('Informe os custos:'))
    resultado = (estoque/custos) * dias
    pme1.append(resultado)
    return print('O pme e:', round(resultado))


def pmr():
    contas_receber = float(input('Informe o valor do contas a receber:'))
    receita_liquida = float(input('Informe o valor da receita liquida:'))
    resultado = (contas_receber/receita_liquida) * dias
    pmr1.append(resultado)
    return print('O pmr e:', round(resultado))


def pmp():
    fornecedores = float(input('Informe o valor dos fornecedores:'))
    custos = float(input('Informe o valor dos custos:'))
    resultado = (fornecedores/custos) * dias
    pmp1.append(resultado)
    return print('O pmp e:', round(resultado))


def co():
    resultado = pme1[0] + pmr1[0]
    co1.append(resultado)
    return print('O C.O e:', round(resultado))


def cc():
    resultado = co1[0] - pmp1[0]
    cc1.append(resultado)
    return print('O C.C e:', round(resultado))


pme()
pmr()
pmp()
co()
cc()
