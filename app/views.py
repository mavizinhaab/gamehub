from app import app
from flask import render_template, request, redirect, url_for
from app.models.categoria_model import CategoriaModel
from app.service.categoria_service import CategoriaService
from app.models.jogo_model import JogoModel
from app.service.jogo_service import JogoService

categoria_service = CategoriaService()
jogo_service = JogoService()

@app.route('/')
def index():
    return redirect(url_for('listar_categorias'))

# ================== CATEGORIAS ==================

@app.route('/categorias')
def listar_categorias():
    categorias = categoria_service.get_all_categorias()
    return render_template('gamehub/categorias/lista_de_categorias.html', categorias=categorias)

@app.route('/categorias/novo', methods=['GET', 'POST'])
def criar_categoria():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        plataforma = request.form['plataforma']
        categoria_service.create_categoria(
            CategoriaModel(id=None, nome=nome, descricao=descricao, plataforma=plataforma)
        )
        return redirect(url_for('listar_categorias'))
    return render_template('gamehub/categorias/formulario_categorias.html')

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = categoria_service.get_categoria_by_id(id)
    if request.method == 'POST':
        categoria_service.update_categoria(
            CategoriaModel(
                id=id,
                nome=request.form['nome'],
                descricao=request.form['descricao'],
                plataforma = request.form['plataforma']
            )
        )
        return redirect(url_for('listar_categorias'))
    return render_template('gamehub/categorias/formulario_categorias.html', categoria=categoria)

@app.route('/categorias/excluir/<int:id>')
def excluir_categoria(id):
    categoria_service.delete_categoria(id)
    return redirect(url_for('listar_categorias'))

# ================== JOGOS ==================

@app.route('/jogos')
def listar_jogos():
    jogos = jogo_service.get_all_jogos()
    return render_template('gamehub/jogos/lista_de_jogos.html', jogos=jogos)

@app.route('/jogos/novo', methods=['GET', 'POST'])
def criar_jogo():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        desenvolvedor = request.form['desenvolvedor']
        categoria_id = int(request.form['categoria_id'])
        jogo_service.create_jogo(
            JogoModel(
                id=None,
                nome=nome,
                preco=preco,
                desenvolvedor=desenvolvedor,
                categoria_id=categoria_id
            )
        )
        return redirect(url_for('listar_jogos'))
    return render_template(
        'gamehub/jogos/formulario_jogos.html',
        categorias=categoria_service.get_all_categorias()
    )

@app.route('/jogos/editar/<int:id>', methods=['GET', 'POST'])
def editar_jogo(id):
    jogo = jogo_service.get_jogo_by_id(id)
    if request.method == 'POST':
        jogo_service.update_jogo(
            JogoModel(
                id=id,
                nome=request.form['nome'],
                preco=float(request.form['preco']),
                desenvolvedor = request.form['desenvolvedor'],
                categoria_id=int(request.form['categoria_id'])
            )
        )
        return redirect(url_for('listar_jogos'))
    return render_template(
        'gamehub/jogos/formulario_jogos.html',
        jogo=jogo,
        categorias=categoria_service.get_all_categorias()
    )

@app.route('/jogos/excluir/<int:id>')
def excluir_jogo(id):
    jogo_service.delete_jogo(id)
    return redirect(url_for('listar_jogos'))
