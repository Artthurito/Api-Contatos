# 🚀 API de Gerenciamento de Contatos

A aplicação permite o gerenciamento completo de contatos (CRUD), utilizando boas práticas de desenvolvimento, validação de dados e arquitetura limpa.

---

## 📋 Funcionalidades e Requisitos Atendidos

O projeto cumpre 100% dos requisitos solicitados no desafio técnico:

- [x] **CRUD Completo:** Criação, Listagem, Atualização e Exclusão de contatos.
- [x] **Identificador Único:** Uso de **UUID** para IDs dos contatos.
- [x] **Cálculo Automático:** A idade é calculada dinamicamente baseada na data de nascimento.
- [x] **Validação de Dados:** Uso de Pydantic para garantir e-mails válidos e campos obrigatórios.
- [x] **Persistência:** Banco de dados relacional (SQLite) via ORM (SQLAlchemy).
- [x] **Status Codes:** Retornos HTTP corretos (201 Created, 404 Not Found, 204 No Content).
- [x] **Ordenação:** Listagem ordenada alfabeticamente por nome.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** FastAPI (Alta performance e validação automática)
* **Banco de Dados:** SQLite (Simplicidade e portabilidade)
* **ORM:** SQLAlchemy (Abstração e segurança contra SQL Injection)
* **Servidor:** Uvicorn (Servidor ASGI)

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar a API em sua máquina local.

### 1. Clone o repositório
```bash
git clone [https://github.com/Artthurito/Api-Contatos.git](https://github.com/Artthurito/Api-Contatos.git)
cd Api-Contatos
```
2. Instale as dependências
Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual, mas para teste rápido, instale direto:
```bash
pip install -r requirements.txt
```
3. Execute o servidor
Rode o comando abaixo para iniciar a aplicação:
```bash
uvicorn ApiContatos:app --reload
```
O servidor iniciará em http://127.0.0.1:8000.

---

## 📚 Documentação da API
O projeto conta com uma documentação interativa gerada automaticamente pelo FastAPI. Após rodar o servidor, acesse:

http://127.0.0.1:8000/docs

Nesta página, é possível testar todas as rotas (POST, GET, PUT, DELETE) diretamente pelo navegador.

---

## 🏗️ Estrutura do Projeto
O código foi organizado focando em simplicidade e clareza:

- Models (SQLAlchemy): Definição da tabela e colunas do banco.

- Schemas (Pydantic): Validação de entrada e serialização de resposta (DTOs).

- Database: Configuração de sessão e conexão.

- Rotas: Endpoints da API seguindo os verbos HTTP REST.

Desenvolvido por Arthur Angeli
