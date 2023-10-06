import json
import os

produtos = []

def cadastrar_produto():
    codigo = len(produtos) + 1
    nome = input("Informe o nome do produto: ")
    valor_compra = float(input("Informe o valor de compra: "))
    quantidade = int(input("Informe a quantidade em estoque: "))
    valor_venda = valor_compra * 1.25
    produto = {
        "codigo": codigo,
        "nome": nome,
        "valor_compra": valor_compra,
        "valor_venda": valor_venda,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")
    
def relatorio_produtos():
    print("Relatório de Produtos")
    print("--------------------")
    for produto in produtos:
        print("Código: ", produto["codigo"])
        print("Nome: ", produto["nome"])
        print("Valor de compra: ", produto["valor_compra"])
        print("Valor de venda: ", produto["valor_venda"])
        print("Quantidade: ", produto["quantidade"])
        print("--------------------")
        
def relatorio_estoque_baixo():
    print("Relatório de Estoque Baixo")
    print("--------------------")
    for produto in produtos:
        if produto["quantidade"] <= 5:
            print("Código: ", produto["codigo"])
            print("Nome: ", produto["nome"])
            print("Valor de compra: ", produto["valor_compra"])
            print("Valor de venda: ", produto["valor_venda"])
            print("Quantidade: ", produto["quantidade"])
            print("--------------------")
            
def exportar_dados():
    print("Exportar dados")
    print("--------------------")
    print("Exportando dados para o arquivo produtos.json...")
    with open("produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo)
    print("Dados exportados com sucesso!")
    print("--------------------")
    
def menu():
    print("Varejão do João")
    print("[1] Cadastrar de produto")
    print("[2] Relatório de produtos")
    print("[3] Relatório de Estoque Baixo")
    print("[4] Exportar dados")
    print("[0] Sair")
    opcao = int(input("Informe a opção desejada: "))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        relatorio_produtos()
    elif opcao == 3:
        relatorio_estoque_baixo()
    elif opcao == 4:
        exportar_dados()
    elif opcao == 0:
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")
    os.system("pause")
    os.system("cls")
    menu()
    
menu()
