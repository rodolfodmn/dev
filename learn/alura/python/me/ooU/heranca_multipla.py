class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('horas registradas...')

    def mostrar_tarefas(self):
        print('fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa, Caelum')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'mostrando cursos - {mes}', if mes else 'mostrando cursos desse mes')

class Alura (Funcionario):
    def busca_perguntas_sem_resposta(self):
        print('mostrando perguntas não respondidas do forum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass
 

class Pleno(Alura, Caelum, Hipster):
    pass



jose = Junior('José')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)
