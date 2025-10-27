import pymysql

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="Joao-2006",
        database="teste"
    )

    print("✅ Conectado ao MySQL com PyMySQL!")

    cursor = conn.cursor()

    # Inserir dados
    cursor.execute("INSERT INTO teste1 (nome, email) VALUES (%s, %s)", ("pedro", "pedro@gmail.com"))
    conn.commit()

    # Buscar dados
    cursor.execute("SELECT * FROM teste1")
    resultado = cursor.fetchall()

    print("📍 Dados na tabela:")
    for linha in resultado:
        print(linha)

except Exception as e:
    print("Erro:", e)

finally:
    if conn:
        conn.close()
        print("🔌 Conexão encerrada")
