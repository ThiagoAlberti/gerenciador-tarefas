import sqlite3

# Conectar ao banco (ou criar se não existir)
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        concluida BOOLEAN NOT NULL DEFAULT 0
    )
''')
conn.commit()

def adicionar_tarefa(descricao):
    cursor.execute('INSERT INTO tarefas (descricao) VALUES (?)', (descricao,))
    conn.commit()
    print("Tarefa adicionada!")

def listar_tarefas():
    cursor.execute('SELECT id, descricao, concluida FROM tarefas')
    for id, descricao, concluida in cursor.fetchall():
        status = "✔️" if concluida else "❌"
        print(f"{id} - {descricao} [{status}]")

def concluir_tarefa(id):
    cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (id,))
    conn.commit()
    print("Tarefa marcada como concluída.")

def deletar_tarefa(id):
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    print("Tarefa deletada.")

def atualizar_tarefa(id, nova_descricao):
    cursor.execute('UPDATE tarefas SET descricao = ? WHERE id = ?', (nova_descricao, id))
    conn.commit()
    print("Tarefa atualizada.")

# Menu simples de terminal
while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Atualizar tarefa")
    print("5. Deletar tarefa")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        desc = input("Descrição da tarefa: ")
        adicionar_tarefa(desc)
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        id_tarefa = int(input("ID da tarefa: "))
        concluir_tarefa(id_tarefa)
    elif escolha == "4":
        id_tarefa = int(input("ID da tarefa: "))
        nova_desc = input("Nova descrição: ")
        atualizar_tarefa(id_tarefa, nova_desc)
    elif escolha == "5":
        id_tarefa = int(input("ID da tarefa: "))
        deletar_tarefa(id_tarefa)
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")

conn.close()
