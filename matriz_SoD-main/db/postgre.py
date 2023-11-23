import psycopg2


def conectar_banco_dados():
    try:
    # Informações de conexão
        user = 'ollpgsww'
        password = 'spVTM3i3HOViCL_QEWjPcXURGTGF1CRH'
        host = 'isabelle.db.elephantsql.com'
        database = 'ollpgsww'

        # Construir a string de conexão
        conn_string = f"postgresql://{user}:{password}@{host}/{database}"

        # Conectar ao banco de dados
        conn = psycopg2.connect(conn_string)
        print("Conexão bem-sucedida!")
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def desconectar():
    conn = conectar_banco_dados()

    if conn:
        conn.close()

    else:
        return None
