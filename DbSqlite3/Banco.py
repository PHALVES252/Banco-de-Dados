import sqlite3



conn=sqlite3.connect('Dbteste3')

print("Conexão estabelecida com sucesso")

cursor=conn.cursor()

Aluno=[('tales',34,'Serra'),
       ('paulo',35,'Vitoria'),
       ('Gustavo',19,'Vilavelha')






       ]


cursor.executemany(" Insert into alunos(nome, idade, cidade)values(?,?,?)",Aluno)

def ordemCrescente():
       cursor.execute('''
           SELECT nome FROM alunos 
           ORDER BY nome ASC  -- Ascendente é o padrão, pode ser omitido
       ''')

       selecao = cursor.fetchall()  # Pega todos os resultados da consulta
       print(selecao)


def ordemDecrescente():
       cursor.execute('''
              SELECT nome from alunos
              order by nome desc



       ''')
       selecao = cursor.fetchall()
       print(selecao)


def idadeMaior():
       cursor.execute('''
       
       select idade from alunos
       order by idade desc
       
       
       
       
       
       
       ''')

       maisvelho=cursor.fetchone()
       print(maisvelho)


while True:

       op=int(input("Digite um um opção"
                    "1 Para crescente\n"
                    "2 Para descrecente\n"
                    "3 Para saber o aluno mais velho"))





       if op==1:
              ordemCrescente()

       if op==2:
              ordemDecrescente()

       if op==3:
            print(f" O aluno mais velho da classe tem {idadeMaior()} anos")

       resp=input("Deseja continuar")

       if resp in 'nN':
              break



cursor.execute('''
    create table if not exists professores(
    id_alunos integer primary key autoincrement,
    nome text not null,
    idade integer  not null,
    cidade text
    
    )



    




''')

cursor.execute('''
    create table if not exists alunos(
    id_alunos integer primary key autoincrement,
    nome text not null,
    idade integer  not null,
    cidade text

    )





''')



Aluno=[('tales',34,'Serra'),
       ('paulo',35,'Vitoria'),
       ('Gustavo',19,'Vilavelha')






       ]


cursor.executemany(" Insert into alunos(nome, idade, cidade)values(?,?,?)",Aluno)





cursor.close()
conn.close()


print("Progama encerrado")
