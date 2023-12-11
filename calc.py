import sqlite3



class Numbers():
    def __init__(self,n1,op,n2):
        self.n1:int//float = n1
        self.op:str = op
        self.n2:int//float = n2
        self.nf,self.ns,self.o = '','',''
        self.why_n1 = ''
        self.why_n2 = ''
        

    def just_number_n1(self):
        if self.n1.isdigit():
            self.nf = True
            self.why_n1 = 'int'
        elif self.n1[0].isdigit():
            try:
                z = float(self.n1)
                self.nf = True
                self.why_n1 = 'float'
            except:
                self.nf = False
        else:
            self.nf = False


    def just_number_n2(self):
        if self.n2.isdigit():
            self.ns = True
            self.why_n2 = 'int'
        elif self.n2[0].isdigit():
            try:
                z = float(self.n1)
                self.ns = True
                self.why_n2 = 'float'
            except:
                self.ns = False
        else:
            self.ns = False


    def operator(self):
        operatos = {
            '/','*','-','+'
        }
        if self.op in operatos:
            self.o = True
        else:
            self.o = False



def accountant(n1,n2,value):
    if value == 0:
        resp = n1 / n2
        return resp
    elif value == 1:
        resp = n1 * n2
        return resp
    elif value == 2:
        resp = n1 - n2
        return resp
    elif value == 3:
        resp = n1 + n2
        return resp
    else:
        return f'[ERRO]Sintax'

try:
    conect = sqlite3.connect('databased.db')
    cursor = conect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS table_results(
                   id INTEGER PRIMARY KEY,
                   count TEXT

    )
''')
    conect.commit()
except:
    print('[ERRO] Erro de conexão.')



number1 = input('numero = ')
operator = input('operador = ')
number2 = input('numero = ')

results = ''

accountant_made = Numbers(number1,operator,number2)
accountant_made.just_number_n1()
accountant_made.just_number_n2()
accountant_made.operator()





if accountant_made.nf == True and accountant_made.ns == True:
    if accountant_made.o == True:
        complete_count = number1 + operator + number2
        cursor.execute("SELECT * FROM table_results  WHERE count=?",(complete_count,))
        if cursor.fetchone() == None:
            cursor.execute("INSERT INTO table_results (count) VALUES (?)",(complete_count,))
            conect.commit()
            op = ['/','*','-','+']
            for valor,operador in enumerate(op):
                if operador == accountant_made.op:
                    if accountant_made.why_n1 == 'int':
                        if accountant_made.why_n2 == 'int':
                            results = accountant(int(accountant_made.n1),int(accountant_made.n2),valor)
                            print(f'{complete_count} = {results}')
                        elif accountant_made.why_n2 == 'float':
                            results = accountant(int(accountant_made.n1),float(accountant_made.n2),valor)
                            print(f'{complete_count} = {results}')
                        else:
                            print('[ERROR]')
                    elif accountant_made.why_n1 == 'float':
                        if accountant_made.why_n2 == 'float':
                            results = accountant(float(accountant_made.n1),float(accountant_made.n2),valor)
                            print(f'{complete_count} = {results}')
                        elif accountant_made.why_n2 == 'int':
                            results = accountant(float(accountant_made.n1),int(accountant_made.n2),valor)
                            print(f'{complete_count} = {results}')
                        else:
                            print('[ERROR]')
            else:
                ...
        else:
            print('Esta operação já foi utilizada em algum momento.')
            results2 = input(f'Então qual seria o resultado dessa operção? {complete_count} -->')
    
            op = ['/','*','-','+']
            for valor,operador in enumerate(op):
                if operador == accountant_made.op:
                    if accountant_made.why_n1 == 'int':
                        if accountant_made.why_n2 == 'int':
                            results = accountant(int(accountant_made.n1),int(accountant_made.n2),valor)
                        elif accountant_made.why_n2 == 'float':
                            results = accountant(int(accountant_made.n1),float(accountant_made.n2),valor)
                        else:
                            print('[ERROR]')
                    elif accountant_made.why_n1 == 'float':
                        if accountant_made.why_n2 == 'float':
                            results = accountant(float(accountant_made.n1),float(accountant_made.n2),valor)
                        elif accountant_made.why_n2 == 'int':
                            results = accountant(float(accountant_made.n1),int(accountant_made.n2),valor)
                        else:
                            print('[ERROR]')
            else:
                ...
            
            if results2 == str(results):
                print('Correto!')
                print(f'{complete_count} = {results2}')
            else:
                print(f'Errado o resultado de {complete_count} = {results}')

    else:
        print('Operador inserido incorreto!')
else:
    print('Reveja os dados inseridos')



conect.close()


   





