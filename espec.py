'''
Classe para listar as especificações de hardware do equipamento
'''

# Importando as bibliotecas utilizadas pela classe
from platform import system, release, version
from socket import gethostname, gethostbyname
from re import findall
from uuid import getnode
from psutil import virtual_memory
from win32com.client import GetObject
from datetime import datetime
from pyperclip import copy

# Definindo a classe para tratar as especificações de hardware
class Especificacao():
    # Método construtor da classe
    def __init__(self):
        self.especificacao={}
        try:
            self.especificacao={}
            self.especificacao['so']=system()
            self.especificacao['versao']=release()
            self.especificacao['build']=version()
            self.especificacao['hostname']=gethostname()
            self.especificacao['ip_address']=gethostbyname(gethostname())
            self.especificacao['mac_address']=':'.join(findall('..', '%012x' % getnode()))
            # Capturar informações do SO 
            root_winmgmts = GetObject("winmgmts:root\cimv2")
            cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
            os = root_winmgmts.ExecQuery("Select * from Win32_OperatingSystem")
            dom = root_winmgmts.ExecQuery("Select * from Win32_ComputerSystem")
            mentype = root_winmgmts.ExecQuery("Select * from Win32_PhysicalMemory")
            tipo = self.get_tipo_memoria(mentype[0].SMBIOSMemoryType)
            self.especificacao['memoria_ram']=str(round(virtual_memory().total / (1024.0 **3)))+"GB " + tipo
            self.especificacao['processador']=cpus[0].Name
            self.especificacao['arquitetura']=os[0].OSArchitecture
            self.especificacao['dominio']=dom[0].Domain
            # Converter a data de instalação para o padrão mmddaaaa
            data_instalacao=datetime.strptime(os[0].InstallDate[:8],'%Y%m%d')
            self.especificacao['data_instalacao']=str(data_instalacao.strftime('%d/%m/%Y'))
        except Exception as erro:
            print(erro)
    # Método para envio dos dados
    def get_especificacao(self):
        return self.especificacao
    # Método para copiar o conteúdo para a área de transferência
    def get_copia_especificacao(self):
        especificacao_equipamento = "Nome: " + self.especificacao['hostname'] + "\nDomínio: " + self.especificacao['dominio'] +"\nIP: " + self.especificacao['ip_address'] + "\nMAC: " + self.especificacao['mac_address'] + "\nS.O.: " + self.especificacao['so'] + "\nVersão: " + self.especificacao['versao'] + "\nBuild: " + self.especificacao['build'] + "\nArquitetura: " + self.especificacao['arquitetura'] + "\nInstalado em: " + self.especificacao['data_instalacao'] + "\nProcessador: " + self.especificacao['processador'] + "\nMemória: " + self.especificacao['memoria_ram']
        return copy(especificacao_equipamento)
    # Método para identificar o tipo da memória
    def get_tipo_memoria(self, codigo):
            if codigo == 20:
                return "DDR"
            elif codigo == 21:
                return "DDR2"
            elif codigo == 22:
                return "DDR2 FB-DIMM"
            elif codigo == 24:
                return "DDR3"
            elif codigo == 26:
                return "DDR4"
            else:
                return "Tipo desconhecido"

'''
https://www.winhelponline.com/blog/determine-memory-module-type-ddr-ddr2-ddr3-installed/
Memory Type/SMBIOSMemoryType	RAM Type
20	DDR
21	DDR2
22	DDR2 FB-DIMM
24	DDR3
26	DDR4
'''