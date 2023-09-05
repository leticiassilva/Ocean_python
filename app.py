from flask import Flask
from flask import render_template
app = Flask("Meu app")

posts = [
    {
    "titulo": "Minha primeira postagem",
    "texto": "teste"
    },
    {
    "titulo": "Segundo Post",
    'texto': "outro teste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)

