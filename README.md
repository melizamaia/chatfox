# 🦊 ChatFox

> Sistema de chat em tempo real com **Django Channels**, **JWT** e **WebSocket**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![Channels](https://img.shields.io/badge/Channels-4.3.1-orange.svg)](https://channels.readthedocs.io/)
[![JWT](https://img.shields.io/badge/Auth-JWT-yellow.svg)](https://django-rest-framework-simplejwt.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📋 Sobre o Projeto

**ChatFox** é um sistema de chat em tempo real desenvolvido com **Django + Channels + JWT**, permitindo **conexões WebSocket autenticadas**.  
O projeto combina **API REST (login)** com **middleware de autenticação JWT** para WebSocket, garantindo segurança e comunicação instantânea.

---

## ✨ Funcionalidades Implementadas

- 🔐 **Autenticação JWT via REST** (`/api/auth/login/`)
- ⚡ **Autenticação JWT via WebSocket** (`?token=<access_token>`)
- 💬 **Chat em tempo real** via Channels (consumers)
- 🧠 **Middleware personalizado** que valida o token JWT e injeta `scope["user"]`
- 🧩 **Página interativa de teste** em `/` para colar o token e enviar mensagens
- 🌍 **Internacionalização**: `pt-br` / `America/Sao_Paulo`

---

## 🧩 Arquitetura

```text
Cliente (Browser)
   │
   ├── HTTP Login (JWT)
   │      POST /api/auth/login/
   │      → {"access": "<token>", "refresh": "..."}
   │
   └── WebSocket (Channels)
          ws://localhost:8000/ws/chat/<room>/?token=<access_token>
```

- **Django REST Framework + SimpleJWT** → autenticação REST  
- **Django Channels + Daphne** → servidor ASGI WebSocket  
- **JWTAuthMiddlewareStack** → valida o token antes de conectar  
- **ChatConsumer** → gerencia conexão, envio e broadcast

---

## 🧪 Página de Teste Interativa

O projeto inclui uma interface simples em `http://localhost:8000/`:

1. Cole o token JWT (campo `access` retornado pelo login)
2. Clique em **Conectar WS**
3. Envie mensagens em tempo real

📎 Arquivo: `templates/chat/home.html`

> 💡 Dica: abra duas abas com o mesmo token e sala (`sala1`) — as mensagens aparecem instantaneamente nas duas!

---

## 🔐 Fluxo de Autenticação JWT

### 1️⃣ Login REST

```bash
POST /api/auth/login/
Content-Type: application/json

{
  "username": "admin",
  "password": "senha123"
}
```

Retorna:
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

### 2️⃣ Conexão WebSocket

```text
ws://localhost:8000/ws/chat/sala1/?token=<access_token>
```

---

## ⚙️ Como Rodar Localmente

```bash
git clone https://github.com/melizamaia/chatfox.git
cd chatfox

# Ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Migrações e superusuário
python manage.py migrate
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver
```

Acesse:
- 🌐 Página de teste → http://localhost:8000/
- 🔐 JWT login → http://localhost:8000/api/auth/login/
- ⚙️ Admin → http://localhost:8000/admin/

---

## 🏗️ Estrutura do Projeto

```markdown
chatfox/
├── chatfox/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── channels_middleware.py
│   ├── wsgi.py
│   └── apps.py
├── chat/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── routing.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── templates/chat/home.html
├── manage.py
├── requirements.txt
├── db.sqlite3
├── docs/
│   ├── img/
│   └── README.md
└── static/
  ├── css/
  ├── js/
  └── img/
```

---

## 🧠 Tecnologias

| Stack | Descrição |
|:------|:-----------|
| **Python 3.12** | Linguagem principal |
| **Django 5.2.7** | Framework web |
| **Django Channels 4.3.1** | WebSocket e async |
| **SimpleJWT** | Autenticação JWT |
| **Daphne** | Servidor ASGI |
| **SQLite** | Banco local (dev) |

---

## 🧭 Roadmap

| Etapa | Descrição | Status |
|:------|:-----------|:------:|
| 1 | Configuração inicial do projeto | ✅ |
| 2 | Estrutura Django básica | ✅ |
| 3 | Autenticação JWT (REST) | ✅ |
| 4 | Autenticação JWT (WebSocket) | ✅ |
| 5 | Sistema de chat em tempo real (consumers) | ✅ |
| 6 | Interface do usuário | 🚧 |
| 7 | Histórico de mensagens | 🔜 |
| 8 | Uploads, notificações, status online | 🔜 |
| 9 | Deploy (Daphne + Redis + Docker) | 🔜 |

---

## 👩‍💻 Autora

**Meliza Maia**  
💼 Desenvolvedora Backend e Analista de Dados  
🌐 [github.com/melizamaia](https://github.com/melizamaia)  
📧 melizamaia@gmail.com

---

## 📄 Licença

Este projeto está sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE).