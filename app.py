#teste 3 app

from database import criar_tabela, conectar

criar_tabela()

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço (opcional, 0 se não tiver): "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                   (nome, quantidade, preco))
    conn.commit()
    conn.close()
    print("Produto adicionado com sucesso!")

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    print("\n=== ESTOQUE ATUAL ===")
    for p in produtos:
        print(f"ID: {p[0]} | Produto: {p[1]} | Qtd: {p[2]} | Preço: R${p[3]}")
    print("======================\n")

def atualizar_quantidade():
    listar_produtos()
    pid = int(input("ID do produto para atualizar: "))
    nova_qtd = int(input("Nova quantidade: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET quantidade=? WHERE id=?", (nova_qtd, pid))
    conn.commit()
    conn.close()
    print("Quantidade atualizada!")

def remover_produto():
    listar_produtos()
    pid = int(input("ID do produto para remover: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id=?", (pid,))
    conn.commit()
    conn.close()
    print("Produto removido!")

def menu():
    while True:
        print("""
============== MENU ==============
1 - Adicionar produto
2 - Listar produtos
3 - Atualizar quantidade
4 - Remover produto
0 - Sair
==================================
""")
        opc = input("Escolha: ")

        if opc == "1":
            adicionar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            atualizar_quantidade()
        elif opc == "4":
            remover_produto()
        elif opc == "0":
            break
        else:
            print("Opção inválida!")

menu()
