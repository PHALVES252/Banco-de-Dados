# Banco-de-Dados
 Conceito teoricos sobre a disciplina de banco de dados


 de 1970 para 1986, a ibm mudou o nome da linguagem de sequel para sql(Estrutury languagem language)


 nome="ana';drop table alunos;--"
 query f select *from alunos where='

 escapagem coreta

 select from alunos where nome='ana''s cafe';
 Apostrofo é um delimitador

 Escapagem, é um processo de tratar carcteres especiais inseridos em entradas de dados para que seja interpretados de forma literal

 Parametros dinamicas-placeholders,
 nome="Anas's Café"
 cursor.execute('select from alunos where nome=?",(nome,))

 con faz a ponte-comunicação
 values(?,?,?)

 select coluna1,coluna
 from nometablea
 where condiçao
 [order by coluna{asc |desc]]

         Select fetchall
 cursor.execute('Select *from alunos')
 resultados=cursor.fetchall() recupera todos os dados resultados

 for linha in resultados:
         print(linha)


fetchone- retorna o primeiro registro encontrado

cursor.execute('select nome, idade from alunos where cidade=?,(vitoria)
resultador-


UPDATE

UPDATE NOMETABELA

SET COLUNA1==VALOR--DEFINE QUAIS CAMPOS SERÃO ALTERADOS
WHERE CONDIÇÃO


CURSOR. EXECUTE('''
UPDATE ALUNOS
SET CIDADE=?
""",('RIO DE JANIERO','Carlos'))


  CODIGO


import sqlite3

conn=sqlite3.connect('senac_PauloHenrique')
print("Conexão estabelecida com sucesso")

cursor=conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS ALUNO(
    ID_ALUNO INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    IDADE INTEGER NOT NULL,CHECK(IDADE<0),
    CIDADE TEXT
    
    )

'''
)


  
ALUNOS=[
 ('Paulo',34,'Serra'),
 ('gUSTAVO',19,'Vilavelha')




]


cursor.executemany("INSERT INTO ALUNO(NOME,IDADE,CIDADE') (VALUES(?,?,?)",ALUNOS)











cursor.execute('''

    CREATE TABLE IF NOT EXISTS PROFESSOR(
    ID_PROFESSOR INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL
    
    
    )

'''
)


PROFESSORES=[
 ('Ludovico')

]

cursor.executemany("INSERT INTO PROFESSOR(NOME) (VALUES(?)",PROFESSORES)




import sqlite3

conn=sqlite3.connect("bancoCadastro.db")

print("Conexão estabelecida com sucesso")

cursor=conn.cursor()


# Regras de negocio
# 1 um mesmo cpf não pode ser cadastrado mais de um vez
# 2 todos os noms devem ser salvos em letras maisculas

cursor.execute('''

        create table if not exists alunos(
        id_alunos integer primary key autoincrement,
        nome text not null,
        cpf text not null)




''')








while True:
    nome=input("Iforme o nome do aluno").upper()
    cpf=input("Digite o cpf")
    
    
    if cpf_existe(cursor,cpf):
        print("cpf já cadastrado")
        
    else:
        cursor.execute('insert into aluno (nome,cpf) Values(?,?,?)'(nome,cpf))


  frfffffff[


  import sqlite3

conn=sqlite3.connect("bancoCadastro.db")

print("Conexão estabelecida com sucesso")

cursor=conn.cursor()


# Regras de negocio
# 1 um mesmo cpf não pode ser cadastrado mais de um vez
# 2 todos os noms devem ser salvos em letras maisculas

cursor.execute('''

        create table if not exists alunos(
        id_alunos integer primary key autoincrement,
        nome text not null,
        cpf text not null)




''')


def cpf_existe(cursor,cpf):
    cursor.execute(
        '''
        select * from alunos where
        
        
        
        '''



    )





while True:
    nome=input("Iforme o nome do aluno").upper()
    cpf=input("Digite o cpf")


    if cpf_existe(cursor,cpf):
        print("cpf já cadastrado")

    else:
        cursor.execute('insert into aluno (nome,cpf) Values(?,?)',(nome,cpf))
        cp




cursor.close()
conn.close

cursor.close()
conn.close



cursor.close()
conn.close()
