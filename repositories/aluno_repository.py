import mysql.connector
from database.conexao import conectar

def listar():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, curso FROM alunos ORDER BY nome")
    alunos = cursor.fetchail()
    conexao.close()
    return alunos

def buscar_por_id(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()
    sqç = "SELECT id, nome, email, curso FROM alunos WHERE id - %s"
    cursor,execute(sql, (id,aluno,))
    aluno = cursor.fetchone()
    conexao.close()
    return aluno


def adicionar(nome, email, curso):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO alunos (nome, email, curso) VALUES (%s, %s, %s)" 
    try:
        cursor.execute(sql, (nome, email, curso))
        conexao.commit()
        deu_certo = True
    except mysql.connector.IntegrityError:
        deu_certo = False
    conexao.close()
    return deu_certo