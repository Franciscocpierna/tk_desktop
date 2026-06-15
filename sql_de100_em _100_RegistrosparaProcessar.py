# Começamos com o offset zerado
offset = 0

while True:
    # 1. Trocamos o '%s' por '?' que é o padrão do SQLite
    query = """
    SELECT a.codigo, b.nome, a.compra, a.vencimento, a.descricao, a.pagamento,
           a.tipo, c.nome, a.valpagar, a.desconto, a.juros, a.documento, 
           a.tparcela, a.cs, a.produto, d.nome
    FROM contas a, fornecedor b, tipo c, produto d 
    WHERE a.codigo = b.codigo 
      AND a.tipo = c.codigo 
      AND a.produto = d.codigo 
    ORDER BY b.nome ASC
    LIMIT 100 OFFSET ?
    """
    
    # 2. Executa passando a tupla (offset,) exigida pelo sqlite3
    cursor.execute(query, (offset,))
    
    registros = cursor.fetchall()
    
    # Se a lista vier vazia, encontramos o fim dos registros
    if not registros:
        print("Todos os registros foram processados!")
        break
        
    print(f"Processando lote de registros do {offset + 1} ao {offset + len(registros)}...")
    for linha in registros:
        # Sua lógica aqui (Exemplo: ler os dados da tupla)
        # codigo = linha[0]
        # nome_fornecedor = linha[1]
        pass

    # Incrementa fixo de 100 em 100
    offset += 100