from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def aplicar_desconto(self, desconto):
        if 0 < desconto < 100:
            self.__preco -= self.__preco * (desconto / 100)
            return True
        return False

    def __str__(self):
        return (
            f"<strong>Produto:</strong> {self.__nome}<br>"
            f"<strong>Preço:</strong> R$ {self.__preco:.2f}<br>"
            f"<strong>Estoque:</strong> {self.__estoque} unidades"
        )

# Armazenar produtos
produtos = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome_original = request.form['nome'].strip()
        nome = nome_original.lower()
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])

        produtos[nome] = Produto(nome_original, preco, estoque)
        return render_template('resultado.html', mensagem=f"✅ Produto '{nome_original}' cadastrado com sucesso!")

    return render_template('cadastrar.html')

@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    if request.method == 'POST':
        nome = request.form['nome'].strip().lower()
        if nome in produtos:
            return render_template('resultado.html', mensagem=str(produtos[nome]))
        else:
            return render_template('resultado.html', mensagem="⚠️ Produto não encontrado.")
    return render_template('consultar.html')

@app.route('/desconto', methods=['GET', 'POST'])
def desconto():
    if request.method == 'POST':
        nome = request.form['nome'].strip().lower()
        try:
            desconto = float(request.form['desconto'])
        except ValueError:
            return render_template('resultado.html', mensagem="⚠️ Desconto inválido.")

        if nome in produtos:
            if produtos[nome].aplicar_desconto(desconto):
                return render_template('resultado.html', mensagem="✅ Desconto aplicado com sucesso!")
            else:
                return render_template('resultado.html', mensagem="⚠️ O desconto deve estar entre 0 e 100.")
        else:
            return render_template('resultado.html', mensagem="⚠️ Produto não encontrado.")
    return render_template('desconto.html')

if __name__ == '__main__':
    app.run(debug=True)
