# django-orm-lab

## 1. Sobre o projeto

Este é um pequeno CRUD de livros desenvolvido em Django para uma aula prática de Ciência da Computação. Ele será usado para estudar **Models**, **Django ORM**, **migrations** e a relação entre objetos Python e registros no banco de dados.

O sistema permite listar, cadastrar, visualizar, editar e excluir livros. A implementação inicial é propositalmente simples para que a modelagem possa evoluir durante a aula.

## 2. Pré-requisitos

- Python 3.12 ou superior;
- Git;
- um ambiente virtual Python (recomendado).

Confirme a versão instalada com `python --version` ou `python3 --version`.

## 3. Clonando o projeto

```bash
git clone <URL_DO_REPOSITORIO>
cd django-orm-lab
```

## 4. Criando o ambiente virtual

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows (Prompt de Comando):

```bat
python -m venv .venv
.venv\Scripts\activate
```

No PowerShell, o comando de ativação é `.venv\Scripts\Activate.ps1`.

## 5. Instalando as dependências

Com o ambiente virtual ativo, execute:

```bash
pip install -r requirements.txt
```

## 6. Preparando o banco

Crie o banco SQLite e aplique as migrations:

```bash
python manage.py migrate
```

O arquivo `db.sqlite3` será criado na raiz do projeto. Ele não é versionado: a estrutura do banco é reconstruída pelas migrations.

## 7. Inserindo os dados de exemplo

Carregue a fixture que contém quatro livros:

```bash
python manage.py loaddata livros
```

O comando pode ser executado em um banco recém-criado para que o CRUD já comece preenchido.

## 8. Executando

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse <http://127.0.0.1:8000/> no navegador. A página inicial redireciona para a lista de livros.

Para encerrar o servidor, pressione `Ctrl+C` no terminal.

## 9. Estrutura do projeto

```text
django-orm-lab/
├── biblioteca/              # Aplicação responsável pelo CRUD de livros
│   ├── fixtures/            # Dados de exemplo
│   ├── migrations/          # Histórico de alterações do banco
│   ├── forms.py             # Formulário baseado no model Livro
│   ├── models.py            # Definição do model Livro
│   ├── urls.py              # Rotas da aplicação
│   └── views.py             # Fluxo entre requisição, ORM e templates
├── config/                  # Configurações e URLs gerais do projeto
├── static/                  # Arquivos CSS
├── templates/               # Páginas HTML renderizadas pelo Django
├── manage.py                # Entrada para comandos administrativos
├── requirements.txt         # Dependências Python
└── db.sqlite3               # Banco local, criado por migrate (não versionado)
```

Arquivos importantes:

- `manage.py`: executa comandos como `runserver`, `migrate` e `loaddata`;
- `biblioteca/models.py`: descreve a estrutura dos livros no banco;
- `biblioteca/views.py`: recebe requisições e usa o ORM para consultar ou alterar livros;
- `biblioteca/urls.py`: associa endereços às views;
- `templates/`: contém a interface HTML;
- `db.sqlite3`: armazena os dados locais e pode ser recriado a partir das migrations e da fixture.

## Comandos úteis durante a aula

Depois de alterar um model, o fluxo usual é:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

As rotas principais são `/livros/`, `/livros/novo/`, `/livros/<id>/`, `/livros/<id>/editar/` e `/livros/<id>/excluir/`.
