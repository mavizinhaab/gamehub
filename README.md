# 🎮 GameHub 

Aplicação web desenvolvida em **Flask** com banco de dados **SQLite**, destinada à gestão de categorias e jogos.  
O projeto segue o padrão arquitetural **MVC** (Model-View-Controller), utilizando **Repositories** para acesso aos dados e **Services** para encapsular as regras de negócio.

---

##  Entidades

### Categoria
- **id** (int) — Identificador único da categoria.
- **nome** (str) — Nome da categoria (ex.: Ação, RPG, Esportes).
- **descricao** (str) — Descrição detalhada da categoria.
- **plataforma** (str) — Plataforma associada à categoria (ex.: PC, PS5, Xbox).

### Jogo
- **id** (int) — Identificador único do jogo.
- **nome** (str) — Nome do jogo.
- **preco** (float) — Valor comercial do jogo.
- **desenvolvedor** (str) — Nome do desenvolvedor ou estúdio responsável.
- **categoria_id** (int) — Referência à categoria à qual o jogo está vinculado.

---

## Relacionamento

- Relação **1:N** — Uma categoria pode conter diversos jogos.
- A exclusão de uma categoria não é permitida caso existam jogos vinculados a ela, garantindo integridade dos dados.

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