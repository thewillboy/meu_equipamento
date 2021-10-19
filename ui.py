'''
Classe para estruturar a interface gráfica do aplicativo
'''

# Importando as bibliotecas utilizadas pela classe
from tkinter import *
from PIL import ImageTk, Image
from espec import Especificacao
import sys, os

# Definindo a classe para estruturar a interface do aplicativo
class Interface():
    # Método construtor da classe
    def __init__(self):
        # Instanciando a classe para recuperar as informações de hardware do equipamento
        self.computador = Especificacao()
        self.especificacao = self.computador.get_especificacao()
        # Configurando a interface do aplicativo
        self.tela_inicial = Tk()
        self.tela_inicial.title("Meu Equipamento")
        self.tela_inicial.geometry("400x510")
        self.tela_inicial.resizable(0,0)
        # Tamanho do favicon: 
        self.tela_inicial.iconbitmap(self.resource_path("favicon.ico"))
        self.tela_inicial.columnconfigure(0,minsize=200)
        self.tela_inicial.columnconfigure(1,minsize=200)
        self.tela_inicial.configure(background='white')
        # Definindo uma logo para o aplicativo
        # Tamanho da logo: 
        self.logo = ImageTk.PhotoImage(Image.open(self.resource_path("logo.jpg")))
        self.logo_aplicativo = Label(self.tela_inicial, image=self.logo, bg="white")
        self.logo_aplicativo.grid(row=0, columnspan=2, sticky="ew")
        # Definindo as informações a serem exibidas no aplicativo
        self.get_label_topo("Dados do equipamento:____").grid(row=1, columnspan=2, sticky = 'w')
        self.get_label("Nome:",2,0)
        self.get_conteudo_label("hostname",2,1)
        self.get_label("Domínio:",3,0)
        self.get_conteudo_label("dominio",3,1)
        self.get_label("IP:",4,0)
        self.get_conteudo_label("ip_address",4,1)
        self.get_label("MAC:",5,0)
        self.get_conteudo_label("mac_address",5,1)
        self.get_label("S.O.:",6,0)
        self.get_conteudo_label("so",6,1)
        self.get_label("Versão:",7,0)
        self.get_conteudo_label("versao",7,1)
        self.get_label("Build:",8,0)
        self.get_conteudo_label("build",8,1)
        self.get_label("Arquitetura:",9,0)
        self.get_conteudo_label("arquitetura",9,1)
        self.get_label("Instalado em:",10,0)
        self.get_conteudo_label("data_instalacao",10,1)
        self.get_label("Processador:",11,0)
        self.get_conteudo_label("processador",11,1)
        self.get_label("Memória",12,0)
        self.get_conteudo_label("memoria_ram",12,1)
        # Criando e configurando o botão do aplicativo
        self.botao_copiar_espec = Button(self.tela_inicial, text="CLIQUE AQUI PARA COPIAR AS ESPECIFICAÇÕES", command=self.botao_ativado)
        self.botao_copiar_espec.config(bg='#a6ce39',fg='#ffffff',bd=0, font=("Segoe UI Semibold",10), height=3)
        self.botao_copiar_espec.grid(row=13, columnspan=2, sticky="nsew")
        # Inicializando a interface
        self.tela_inicial.mainloop()

    # Métodos para facilitar a formatação dos labels do aplicativo
    # Método para formatar o label do topo do aplicativo
    def get_label_topo(self, nome_label):
        return Label(self.tela_inicial, text=nome_label, font=("Segoe UI",10), bg="white", pady=1)
    # Método para formatar o label principal
    def get_label(self, nome_label, linha, coluna):
        return Label(self.tela_inicial, text=nome_label, font=("Segoe UI",10), bg="white", pady=1).grid(row=linha, column=coluna, sticky = 'w')
    # Método para formatar o conteúdo exibido no label
    def get_conteudo_label(self, conteudo_label, linha, coluna):
        return Label(self.tela_inicial, text=self.especificacao[conteudo_label], font=("Segoe UI",10), wraplength=200, bg="white", pady=1).grid(row=linha, column=coluna, sticky = 'w')
    # Método para alterar o botão após o clique
    def botao_ativado(self):
        self.computador.get_copia_especificacao()
        self.botao_copiar_espec.config(bg='#f6404f',text="INFORMAÇÕES COPIADAS!")
    # Método para adicionar path completo das imagens
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)