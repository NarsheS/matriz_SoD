import psycopg2
from db.postgre import conectar_banco_dados

def novoPerfil(codigo_sistema, nome_do_perfil, descricao_do_usuario, senha, adm):
  try:
    conn = conectar_banco_dados()

    cursor = conn.cursor()
    insert_query = """
    INSERT INTO perfis_de_acesso (codigo_sistema, nome_do_perfil, descricao_do_usuario, senha, adm)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (codigo_sistema, nome_do_perfil, descricao_do_usuario, senha, adm))
    conn.commit()

    cursor.close()
    conn.close()

  except psycopg2.Error as e:
    print(f"Erro ao criar novo perfil: {e}")