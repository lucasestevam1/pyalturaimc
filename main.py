from imc import imc
import alturaideal
import PySimpleGUI as sg

class tela:
    def __init__(self):
        sg.theme('reddit')
        layout = [
        [sg.Text('Aviso: Na altura use "." e não use ",". Nos outros campos não use ambos.')],
        [sg.Text('Idade: (1/18)'), sg.Input(key='idade')],
        [sg.Text('Altura: (cm)'), sg.Input(key='altura')],
        [sg.Text('Peso: (KG em números inteiros)'), sg.Input(key='peso')],
        [sg.Text('Gênero:          ')],
        [sg.Radio('Feminino', 'genero', key='f'),sg.Radio('Masculino', 'genero', key='m')],
        [sg.Button('Enviar dados')],
        [sg.Output(size=(40,30))]
        ]
        self.janela = sg.Window("Preencha o formulário").layout(layout)
    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            idade = self.values['idade']
            femea = self.values['f']
            peso = self.values['peso']
            altura = self.values['altura']
            if idade == '' or femea == '':
                print('Você esqueceu de preencher algum campo. ')
            else:
                if femea == True:
                    genero = 'feminino'
                else:
                    genero = 'masculino'
                idade = str(idade)
                alturaideal.altura(idade,genero)
                imc(peso, altura)
            
tela()
tela().iniciar()
