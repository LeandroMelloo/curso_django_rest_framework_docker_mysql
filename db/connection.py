import psycopg2

try :
    connection = psycopg2.connect(
        database = 'santander',
        user = 'postgres',
        password = 'admin',
        host = 'localhost',
        port = '5432'
    )
    cursor = connection.cursor()
    print ('Você está conectado ao banco de dados PostgreSQL')
except(Exception, psycopg2.Error) as erro:
    print ('Erro ao conectar ao banco de dados PostgreSQL', erro)
    connection = None
finally:
    if connection != None:
        cursor.close()
        connection.close ()
        print('A conexão PostgreSQL está encerrada')