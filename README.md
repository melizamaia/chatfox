# 🦊 ChatFox

> Sistema de chat em tempo real com Django Channels e WebSocket

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)](https://www.djangoproject.com/)
[![Channels](https://img.shields.io/badge/Channels-4.3.1-orange.svg)](https://channels.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Sobre o Projeto

**ChatFox** é uma aplicação de chat em tempo real construída com Django e Django Channels, permitindo comunicação instantânea via WebSocket. O projeto utiliza tecnologias modernas para oferecer uma experiência fluida e responsiva.

### ✨ Características

- 💬 **Chat em Tempo Real** via WebSocket
- 🔐 **Autenticação JWT** para segurança
- 🌐 **API REST** completa com Django REST Framework
- ⚡ **Assíncrono** com Django Channels e ASGI
- 🎨 **Interface Moderna** (em desenvolvimento)
- 🌍 **Internacionalização** em Português (pt-br)

---

## 🚀 Tecnologias

### Backend
- **Django 5.2.7** - Framework web robusto
- **Django Channels 4.3.1** - Suporte WebSocket e comunicação assíncrona
- **Django REST Framework 3.16.1** - API REST poderosa
- **Daphne 4.2.1** - Servidor ASGI para WebSocket
- **SimpleJWT 5.5.1** - Autenticação JWT

### Banco de Dados
- **SQLite** (desenvolvimento)
- Suporte para PostgreSQL/MySQL (produção)

### Outras Dependências
- **Twisted** - Framework de rede assíncrona
- **Channels** - Extensão WebSocket para Django
- **PyTest** - Framework de testes

---

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/chatfox.git
cd chatfox
```

2. **Crie e ative o ambiente virtual**

```bash
# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure o banco de dados**

```bash
python manage.py migrate
```

5. **Crie um superusuário**

```bash
python manage.py createsuperuser
```

6. **Rode o servidor**

```bash
python manage.py runserver
```

7. **Acesse a aplicação**

- Site: http://localhost:8000/
- Admin: http://localhost:8000/admin/

---

## 🏗️ Estrutura do Projeto

```
chatfox/
├── chatfox/                 # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py         # Configurações principais
│   ├── urls.py             # Rotas principais
│   ├── asgi.py             # Configuração ASGI/WebSocket
│   └── wsgi.py             # Configuração WSGI
├── chat/                    # App de chat (a ser criado)
│   ├── migrations/
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Views e APIs
│   ├── consumers.py        # WebSocket consumers
│   └── routing.py          # Rotas WebSocket
├── manage.py               # CLI do Django
├── requirements.txt        # Dependências
├── pyproject.toml          # Configuração do projeto
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Este arquivo
```

---

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Django
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Banco de Dados (opcional)
DATABASE_URL=postgresql://user:password@localhost:5432/chatfox

# JWT
JWT_ACCESS_TOKEN_LIFETIME=60  # minutos
JWT_REFRESH_TOKEN_LIFETIME=1440  # minutos (1 dia)
```

### Settings Principais

**Localização:**
- Idioma: Português do Brasil (pt-br)
- Timezone: America/Sao_Paulo

**Channels:**
- Backend: InMemoryChannelLayer (desenvolvimento)
- Para produção: usar Redis

---

## 🎮 Uso

### API REST

#### Autenticação

**Obter Token JWT:**
```bash
POST /api/token/
{
  "username": "usuario",
  "password": "senha"
}
```

**Refresh Token:**
```bash
POST /api/token/refresh/
{
  "refresh": "seu-refresh-token"
}
```

### WebSocket

**Conectar ao chat:**
```javascript
const chatSocket = new WebSocket(
    'ws://localhost:8000/ws/chat/room_name/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data.message);
};

chatSocket.send(JSON.stringify({
    'message': 'Olá, mundo!'
}));
```

---

## 🧪 Testes

```bash
# Rodar todos os testes
pytest

# Rodar com coverage
pytest --cov=chatfox

# Rodar testes específicos
pytest chat/tests/test_models.py
```

---

## 📚 Documentação Adicional

### Como Funciona o WebSocket

1. Cliente conecta via `ws://`
2. Autenticação via JWT (opcional)
3. Consumer recebe mensagens
4. Broadcast para todos os clientes conectados
5. Persistência no banco de dados

### Fluxo de Mensagens

```
Cliente 1 → WebSocket → Consumer → Channel Layer → Consumer → WebSocket → Cliente 2
                                        ↓
                                   Banco de Dados
```

---

## 🛠️ Desenvolvimento

### Criar um novo app

```bash
python manage.py startapp nome_do_app
```

### Fazer migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### Coletar arquivos estáticos

```bash
python manage.py collectstatic
```

### Criar um superusuário adicional

```bash
python manage.py createsuperuser
```

---

## 🚢 Deploy

### Usando Daphne (produção)

```bash
# Instalar dependências adicionais
pip install channels-redis

# Configurar Redis no settings.py
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Rodar com Daphne
daphne -b 0.0.0.0 -p 8000 chatfox.asgi:application
```

### Docker (em desenvolvimento)

```dockerfile
# Dockerfile básico
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "chatfox.asgi:application"]
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'feat: Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

### Padrão de Commits

Este projeto segue [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `style:` - Formatação
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Tarefas diversas

---

## 📝 Roadmap

- [x] Configuração inicial do projeto
- [x] Estrutura Django básica
- [x] Autenticação JWT
- [ ] Sistema de chat em tempo real
- [ ] Interface do usuário
- [ ] Sistema de salas de chat
- [ ] Notificações push
- [ ] Upload de arquivos/imagens
- [ ] Mensagens privadas
- [ ] Status online/offline
- [ ] Histórico de mensagens
- [ ] Busca de mensagens
- [ ] Emojis e reações
- [ ] Testes automatizados
- [ ] Deploy em produção

---

## 🐛 Problemas Conhecidos

Nenhum no momento. Reporte bugs na [seção Issues](https://github.com/SEU-USUARIO/chatfox/issues).

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👥 Autores

**Meliza Maia**
- GitHub: [@melizamaia](https://github.com/melizamaia)
- Email: melizamaia@gmail.com

---

## 🙏 Agradecimentos

- [Django](https://www.djangoproject.com/) - Framework web incrível
- [Channels](https://channels.readthedocs.io/) - Suporte WebSocket
- [DRF](https://www.django-rest-framework.org/) - API REST poderosa
- Comunidade Python/Django