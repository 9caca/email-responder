# 📌 Notas Técnicas - AI Email Assistant

Este arquivo contém detalhes técnicos e notas de desenvolvimento do projeto AI Email Assistant.

---

## 🔹 1. Configuração inicial  

✅ **Objetivo:** Preparacao e organizacao do projeto para que fique apresentavel e de facil entendimento para quem acessar esse repositorio no GitHub..  

### **Checklist Concluído**  
- [X] Adicionar um arquivo README.md com uma descrição inicial do projeto.
- [X] Criar ambiente virtual
    - Instalar bibliotecas
- [X] Configurar o .gitignore para Python:
- [X] Instalar Dependências Básicas:
    - Editar o arquivo `requirements.txt`
- [x] Configurar as variaveis do ambiente
    - Editar o arquivo `.env` com dados de acesso ao email e servidor. (Esse nao sera' enviado por causa do `.gitignore`
- [x] Adicionar as regras para ignorar arquivos de ambiente virtual (venv/) e outros arquivos desnecessários (ex.: *.pyc, .DS_Store).
 - [X] Confirmar que o ambiente virtual está ativado e funcionando corretamente.
 - [X] Testar a instalação das bibliotecas especificadas no `requirements.txt`.
 - [X] Configurar e testar o acesso ao servidor de e-mail usando as variáveis de ambiente do arquivo `.env`.
 - [X] Implementar um script simples para conexão com o servidor de e-mail (IMAP/SMTP) e listar as pastas disponíveis (apenas para verificação).
- [X] Criar uma estrutura inicial de diretórios e arquivos para o projeto (ex.: `src/`, `tests/`, etc.).
- [X] Atualizar o arquivo `README.md` com informações sobre como configurar e testar o ambiente local.
- [X] Documentar possíveis problemas e soluções no arquivo `README.md` (se necessário).
- [X] Validar se todos os arquivos desnecessários estão sendo ignorados pelo `.gitignore`.

---

## 🔹 2. Modelo Básico: Respostas Automáticas  

✅ **Objetivo:** Criar um sistema de resposta automática baseado em palavras-chave.  

### **Checklist Concluído**  
- [x] Adicionar um script básico em `src/` para ler e-mails de uma conta de teste.  
- [x] Filtrar e-mails não lidos na caixa de entrada.  
- [x] Implementar um script inicial para envio de e-mails com mensagens pré-definidas.  
- [x] Testar o envio e recebimento de e-mails entre contas de teste.  
- [X] Adicionar um script básico em `src/` para ler e-mails de uma conta de teste.
- [X] Filtrar e-mails não lidos na caixa de entrada.
- [X] Implementar um script inicial para envio de e-mails com mensagens pré-definidas (pode ser usado um template fixo).
- [X] Testar o envio e recebimento de e-mails entre contas de teste.
- [X] Garantir que o script não responda a e-mails enviados por sistemas automáticos (ex.: no-reply).

---

## 🔹 2. Integração com OpenAI API  

✅ **Objetivo:** Usar IA para gerar respostas mais naturais e dinâmicas.  

### **Checklist Concluído**  
- [x] Criar uma conta na OpenAI.  
- [x] Instalar a biblioteca OpenAI (`pip install openai`).  
- [x] Configurar a chave de API no projeto.  
- [x] Testar a conexão com a OpenAI.  
- [x] Documentar a configuração.  

---

## 🔹 3. Problemas e Soluções  

### 🔴 Erro: "You exceeded your current quota"  
✅ **Solução:** Verificar saldo na OpenAI e adicionar créditos.  

### 🔴 Erro: `[ALERT] Invalid credentials (Failure)`  
✅ **Solução:**  
- Habilitar IMAP no Gmail.  
- Gerar uma senha de aplicativo para autenticação.  

---

## 🚀 Próximos Passos  

📌 **Treinamento e Aprimoramento**  
- Criar um banco de dados para armazenar e-mails processados.  
- Analisar padrões de e-mails recebidos e ajustar respostas.  
- Implementar sistema de feedback para avaliar respostas da IA.  
