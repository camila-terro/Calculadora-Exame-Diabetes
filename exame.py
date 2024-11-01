#Importação de módulos do Kivy para a interface gráfica 
from kivymd.app import MDApp        
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
  
class ManipulaJanela: # Classe responsável por manipular as configurações da janela 
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        Window.size = (self.largura, self.altura)

class MeuApp(MDApp): #Classe principal do aplicativo que herda de MDApp
    def build(self):  #Cria uma instância da classe ManipulaJanela 
        manipulador = ManipulaJanela(600, 800)
        manipulador.ajustar_tamanho_janela()

        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20) # Cria um layout em caixa vertical

        # Inicializa os campos de texto para as entradas        
        self.val1 = MDTextField(hint_text="Digite o valor da glicemia em jejum", input_filter="float")
        self.val2 = MDTextField(hint_text="Digite a porcentagem de hemoglobina glicada", input_filter="float")
        self.val3 = MDTextField(hint_text="Digite o número de tolerância a glicemia", input_filter="float")

        # Cria um botão para calcular os resultados
        botao_calcular = MDRaisedButton(text="Calcular Exame", on_release=self.calcular_resultados, pos_hint={'center_x': 0.5} )
        self.resultado = MDLabel(text="Resultado: ", halign="center") # Cria um rótulo para apresentar os resultados

        # Adiciona os widgets ao layout  
        layout.add_widget(self.val1)
        layout.add_widget(self.val2)
        layout.add_widget(self.val3)
        layout.add_widget(botao_calcular)
        layout.add_widget(self.resultado)

        return layout
    
     # Método para verificar o resultado da glicemia em jejum
    def verificar_glicemia(self,val1):
        if val1 == 99: 
            return "Normal" 
        elif 100 <= val1 <= 125: 
            return "Pré-diabetes" 
        elif val1 > 126: 
            return "Diabético"
        else:
            return "valor incorreto"
        
    # Método para verificar o resultado da hemoglobina glicada  
    def verificar_hemoglobina(self,val2):
        if val2 == 5.7: 
            return "Normal" 
        elif 5.7 <= val2 <= 6.4: 
            return "Pré-diabetes" 
        elif val2 > 6.5: 
            return "Diabético"
        else:
            return "valor incorreto"
        
    # Método para verificar o resultado da tolerância a glicemia  
    def verificar_tolerancia(self,val3):
        if val3 < 140: 
            return "Normal" 
        elif 140 <= val3 <= 199: 
            return "Pré-diabetes" 
        elif val3 >= 200: 
            return "Diabético"
        else:
            return "valor incorreto"
        
    def calcular_resultados(self, instance):  # Método que é chamado ao pressionar o botão de calcular  
        val1 = float(self.val1.text)    # Converte as entradas de texto para float  
        val2 = float(self.val2.text) 
        val3 = float(self.val3.text)

        # Chama os métodos de verificação para cada entrada
        resultado_glicemia = self.verificar_glicemia(val1) 
        resultado_hemoglobina = self.verificar_hemoglobina(val2) 
        resultado_tolerancia = self.verificar_tolerancia(val3)
        
        # Atualiza o rótulo para mostrar os resultados 
        self.resultado.text = f"Resultado: \nGlicemia: {resultado_glicemia} \n Hemoglobina: {resultado_hemoglobina} \n Tolerância: {resultado_tolerancia}"

MeuApp().run()