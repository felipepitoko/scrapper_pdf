import sqlite3
import pandas as pd
class Database:
    def create_connection():
        conn = sqlite3.connect('test_db.sqlite')
        conn.row_factory = sqlite3.Row
        return conn

    def criar_tabela(conn):
        c = conn.cursor()
        print('Criando tabela...')
        c.execute("""CREATE TABLE IF NOT EXISTS tabelaIPCA (
            ano varchar(4) NOT NULL,
            mes varchar(3) NOT NULL,
            baseIPCA float NOT NULL,
            createdAt timestamp NOT NULL DEFAULT current_timestamp,
            updatedAt timestamp,
            PRIMARY KEY (ano,mes)
            );
        """)
        print('Tabela criada')
        conn.commit()
        return True
    
    def alimentar_primeiros_dados(conn,df):
        c = conn.cursor()
        c.execute("""select * from tabelaIPCA""")
        records = c.fetchall()
        if(len(records) == 0):
            print('Atualizei a base')
            df.to_sql("tabelaIPCA", conn, if_exists="append", index=False)
        else: print('Nao atualizei nada.')
        
        return True

    def inserir_registro(conn, ano, mes, baseIPCA):
        try:             
            c = conn.cursor()
            sql = "INSERT INTO tabelaIPCA (ano, mes, baseIPCA) VALUES ('{0}', '{1}',{2})".format(ano,mes,baseIPCA)
            c.execute(sql)
            c.execute("select * from tabelaIPCA where rowid=last_insert_rowid()")
            records = c.fetchone()

            if(not records):
                return {}

            conn.commit()
            return dict(records)
        except sqlite3.IntegrityError:
            return {}        

    def consultar_todos(conn):
        # c = conn.cursor()
        # c.execute("SELECT * FROM tabelaIPCA")
        df = pd.read_sql_query("SELECT * FROM tabelaIPCA order by ano desc", conn)
        data = df.to_dict('r')
        # dict = {}
        # for linha in data:
        #     ano = linha['ANO']
        #     linha.pop('ANO')
        #     dict[ano] = linha
        return data

    def consultar_mes_ano(conn:any,ano:str, mes:str):
        sql = ''
        if(ano != '' and mes != ''): sql = "Select * from tabelaIPCA where ano='"+ano+"' and mes='"+mes+"' order by ano desc"
        elif(ano != ''): sql = "Select * from tabelaIPCA where ano='"+ano+"' order by ano desc"
        elif(mes != ''): sql = "Select * from tabelaIPCA where mes='"+mes+"'order by ano desc"
        else: sql = 'Select * from tabelaIPCA order by ano desc'

        df = pd.read_sql_query(sql, conn)
        data = df.to_dict('r')
        return data

    def excluir_registro(conn,ano,mes):        
        c = conn.cursor()
        c.execute("select * from tabelaIPCA where mes='{0}' and ano='{1}'".format(mes, ano))
        records = c.fetchone()

        if(not records):
            return {}

        c.execute("DELETE FROM tabelaIPCA where mes='{0}' and ano='{1}'".format(mes,ano))
        conn.commit()
        return dict(records)

    def atualizar_registro(conn,baseIPCA,ano,mes):    
        print(baseIPCA,ano,mes)    
        c = conn.cursor()
        c.execute("update tabelaIPCA set baseIPCA={0},updatedAt=current_timestamp where mes='{1}' and ano='{2}'".format(baseIPCA, mes, ano))
        c.execute("Select * from tabelaIPCA where mes='{0}' and ano='{1}'".format(mes, ano))
        records = c.fetchone()
        print('Achei isso:',records)

        if(not records):
            return {}

        conn.commit()
        return dict(records)