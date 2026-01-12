# Da biblioteca flask traga a classe Flask
from flask import Flask


#instanciando/ criando novo obj flask
#variável __name__ refere a caminho

app = Flask(__name__)

#Endpoints/rotas raiz da pag inical e a função/ verbo a ser executado

#raiz geralmente é uma barra
@app.route("/")
# função a ser executada
def hello_world():
    return " ✮⋆｡°✩⋆˙ Saluton Mondo!⋆⁺₊⋆ ☾⋆⁺₊⋆ "

#para subir
#Debug = ativa apuração que ajuda a receber infromações sobre o servidor - SÓ USA NO DESENVOLVIMENTO - EM PRODUÇÃO DEIXA FALSO
#Se conteúdo da variável name for main, roda
if __name__=="__main__":
    app.run(debug=True)