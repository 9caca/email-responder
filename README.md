<h1>AI Email Assistant</h1>

##  💡 Descrição
Este é um projeto para criar um sistema que responde e-mails automaticamente usando Python.  
O objetivo é praticar programação Python e explorar conceitos como automação, processamento de texto e inteligência artificial.  

O projeto é dividido em três etapas principais:

1. **Modelo básico**: Respostas automáticas baseadas em palavras-chave e templates pré-definidos. 🚧
2. **Integração com IA**: Uso de inteligência artificial (OpenAI API) para gerar respostas personalizadas.
3. **Treinamento e aprimoramento**: Aprimorar a personalização e criar um histórico de e-mails para análise e melhoria contínua.

##  💡 Pré-requisitos

* Python 3.9+ ![Python](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&color=3776AB)
* Conta de e-mail (preferencialmente Gmail, com IMAP habilitado)
* Dependências do projeto:
  * `imaplib`
  * `smtplib`
  * `openai` (a partir da Parte 2)
  * `pandas` (opcional, para manipulação de dados)
---

##  💡 Configuração do Ambiente Local

### Pré-requisitos
1. **Python 3.9+**
2. **Conta Gmail com acesso IMAP habilitado** (veja [Configuração do Gmail](#configuração-do-gmail)).

### Passo a Passo
1. Clone o repositório:</br>
    `git clone https://github.com/usuario/ai-email-assistant.git
     cd ai-email-assistant`
2. Crie e ative um ambiente virtual:</br>
    `python -m venv venv
     venv\Scripts\activate`
3. Instale as dependências:</br>
    `pip install -r requirements.txt`
4. Configure as variáveis de ambiente:
    - Crie um arquivo `.env` com o seguinte conteúdo:</br>
    `EMAIL=seu-email@gmail.com`</br>
    `PASSWORD=sua-senha-de-aplicativo`</br>
    `IMAP_SERVER=imap.gmail.com`</br>
    `SMTP_SERVER=smtp.gmail.com`</br>
    `SMTP_PORT=587`</br>
5. Execute o script de teste `main.py`
    - O script irá conectar ao servidor IMAP e listar as pastas disponíveis.

###  💡 Configuração do Gmail
1. Habilite o acesso IMAP em Configurações > Encaminhamento e POP/IMAP.
2. Ative a verificação em duas etapas e gere uma senha de aplicativo:
  - Acesse Configurações de Segurança do Google.
  - Siga as instruções para gerar uma senha de aplicativo.

###  💡 Possíveis Problemas e Soluções
Erro: `[ALERT] Invalid credentials (Failure)`
  - Verifique se o acesso IMAP está ativado.
  - Use uma senha de aplicativo em vez da senha principal.

___
  
##  💡 Meta
- Carlos Hayashi - @9caca
- Distribuído sob a licença [MIT License](https://https://github.com/9caca/AirCnC/blob/master/LICENSE)