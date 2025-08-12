# 🎮 GameHub Mavizera 😎

Aplicação web feita com **Flask** e **SQLite** para gerenciar categorias e jogos.  
Segue o padrão **MVC** com **Repositories** para acesso ao banco de dados e **Services** para regras de negócio.

---

##  Entidades

### Categoria
- **id** (int) — Identificador único.
- **nome** (str) — Nome da categoria (ex.: Ação, RPG, Esporte).
- **descricao** (str) — Descrição da categoria.
- **plataforma** (str) — Plataforma associada (ex.: PC, PS5, Xbox).

### Jogo
- **id** (int) — Identificador único.
- **nome** (str) — Nome do jogo.
- **preco** (float) — Preço do jogo.
- **desenvolvedor** (str) — Nome do desenvolvedor ou estúdio.
- **categoria_id** (int) — ID da categoria à qual o jogo pertence.

---

##  Relacionamento
- **1:N** → Uma categoria pode ter vários jogos.
- Não é permitido excluir uma categoria caso ela tenha jogos registrados.

##  Como Executar o Projeto

1. Crie o ambiente virtual
    ```bash
    python -m venv venv
    ```
2. Ative o ambiente virtual
    ```bash
    venv\Scripts\activate
    ```
3. Instale as dependências
    ```bash
    pip install --upgrade pip
    pip install Flask
    ```
4. Execute o servidor
    ```bash
    python run.py
    ```