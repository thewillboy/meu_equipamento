Meu equipamento
-------------------------------------------------------

O aplicativo "Meu equipamento" foi criado com o intuito de facilitar o suporte técnico, principalmente quando precisamos solicitar alguns dados técnicos para os usuários.

Informações coletadas
-------------------------------------------------------

O aplicativo "Meu equipamento" coleta e exibe as seguintes informações sobre o computador:


* Nome do computador
* Domínio
* Endereço IP
* Endereço MAC
* Sistema Operacional (Windows, etc...)
* Versão do S.O. (11, 10, 7, etc...)
* Build do S.O. (21H2, 2004, 1903, etc...)
* Arquitetura (x64 ou x86)
* Data de instalação do S.O.
* Processador
* Memória RAM

Logo e ícone (favicon)
-------------------------------------------------------

Você pode alterar a logo e o ícone favicon do aplicativo, desde que as novas imagens mantenham as mesmas proporções, nome e extensão (estes últimos podem ser alterados via código)

Compilação
-------------------------------------------------------

Utilize os seguintes comandos do PyInstaller

* pyi-makespec --onefile --icon="favicon.ico" --noconsole .\main.py 

* pyinstaller --onefile --icon="favicon.ico" --noconsole .\main.spec