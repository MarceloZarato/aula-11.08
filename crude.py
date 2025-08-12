from conexao import conectar


def inserir ():
    con = conectar ()
    cur = con.cursor ()
    nome = input ("Nome do Produto: ")
    preco = float(input("Preço: "))
    validade = input("Data de Validade: ")
    tipo = input("Tipo: ")
    lote = input ("Lote: ")
    ml = float(input("Ml: "))
    piramide = input ("Piramide: ")
    inspiracao = input ("Inspiração: ")
    marca = input ("Marca: ")
    ocasiao = input ("Ocasião: ")
    familia = input ("Família: ")
    cur.execute("INSERT INTO produtos (nome, preco, validade, tipo, lote, ml, piramide, inspiracao, marca, ocasiao, familia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nome,preco,validade,tipo,lote,ml,piramide,inspiracao,marca,ocasiao,familia))
    con.commit ()
    con.close()

def listar ():
    con = conectar ()
    cur = con.cursor()
    cur.execute("SELECT * FROM  produtos")
    for p in cur.fetchall():
        print (p)
    con.close()

def atualizar():
    con = conectar
    cur = con.cursor()
    id_produto = int(input("ID do produto: "))
    preco = float (input("Novo preço: "))
    cur.execute ("UPDATE produtos SET preco = %s WHERE id = %s", (preco,id_produto,))
    con.commit()
    con.close()
    
    
def excluir():
    con = conectar
    cur = con.cursor()
    id_produto = int(input("ID para excluir: "))
    cur.execute ("DELETE FROM produtos WHERE id= %s", (id_produto,))
    con.commit()
    con.close()

def menu ():
    while True:
        print ('1 - Inserir Produto')
        print ('2 - Listar Produto')
        print ('3 - Atualizar Produto')
        print ('4 - Excluir Produto')
        print ('5 - Sair')

        opcao = input ("Escolha: ")

        if opcao == "1":
            inserir ()
        elif opcao == "2":
            listar ()
        elif opcao == "3":
            atualizar ()
        elif opcao == "4":
            excluir ()
        elif opcao == "5":
            break



menu ()