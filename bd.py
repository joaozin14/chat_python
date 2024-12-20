import sqlite3

def conecta_bd():
    conexao = sqlite3.connect('dados.db')
    return conexao

def inserir_dados(cpf ,nome, data_nasc, telefone):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    
    cursor.execute(
        """
        INSERT INTO cliente(cpf, nome, data_nasc, telefone)
        VALUES (?, ?, ?, ?)
        """, (cpf, nome, data_nasc, telefone))
    
    conexao.commit()
    conexao.close()


def obter_dados(cpf):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT * FROM cliente
    WHERE cpf = ?
    """, (cpf,))
    dados = cursor.fetchall()
    cursor.close()
    return dados

def excluir_cliente(cpf):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("""
                   DELETE FROM cliente
                   WHERE cpf = ?
                   """, (cpf,))
    conexao.commit()
    conexao.close() 

def alterar_telefone(telefone, cpf):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute("""
    UPDATE cliente
    SET telefone = ?
    WHERE cpf = ? 
    """, (telefone, cpf))
    conexao.commit()
    conexao.close() 