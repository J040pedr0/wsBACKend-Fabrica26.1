# wsBACKend-Fabrica26.1


Projeto Django desenvolvido  para a disciplina de Backend - Fabrica de software 2026.1

## tecnologias usadas

- Python 3.12
- django 5.0
- PostgreSQL
- Docker 
- Django REST Framework
- JWT Authentication
- Rick and Morty API

## Requisitos Do Projeto 

- Crud completo com 3 entidades relacionadas (User, Collections, Character)
- Consumo da API externa Rick and Morty API(achei que atenderia os requisitos por ser gratuita e publica alem de ser bem estruturada e por ter dados variados)
- Banco de daos PostgreSQL com Docker
- Autenticação com JWT Tokens
- DockerFile e Docker-compose
- Boas práticas de programação (atendendo as regras da sala como "snake_case")
- Documentação completa e feita para ter entendimento facil

## Como executar localmente (SQLite)

1. Clone o repositório:
   ```bash
   git clone https://github.com/J040pedr0/wsBACKend-Fabrica26.1.git
   cd wsBACKend-Fabrica26.1


## ESTRUTURA DO PROJETO

wsBACKend-Fabrica26.1/
├── apps/
│   ├── accounts/          # Autenticação e usuário customizado
│   ├── collections/       # Coleções, personagens e favoritos
│   └── external_api/      # Integração com API externa (Rick and Morty)
├── core/                  # Configurações do Django
├── templates/             # Templates HTML (Jinja)
├── static/                # Arquivos estáticos (CSS, imagens)
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

## 👤 Autor

- Nome: [João Pedro Alexandre ALves]
- RGM: [39471748]

> **!ATENÇÃO!:** A maior parte dos commits e o código final estão na branch `master`. Certifique-se de estar nela ao analisar o repositório.