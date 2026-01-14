# Da biblioteca flask traga a classe Flask
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

#instanciando/ criando novo obj flask
#variável __name__ refere a caminho

app = Flask(__name__)

#caminho para bd do sqlalchemy
# "SQLALCHEMY_DATABASE-URI" - diz onde está o bd
# caminho padrão, inicia com sqlite(neste caso por ser lite):///nome_do_bd (o arquivo a ser usado)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

#iniciar ação de conexão do db(database / bd banco de dados)
#app que é a variável que possui o flask
db = SQLAlchemy(app)

#modelagem, tabelas com collumn and row
# terá colunas com id, name, price, description
#linhas terão as infromações
#para criar model usa-se class + nome

class Product(db.Model):
     #colunas
     # db referente à variável db de conexão
     id = db.Column(db.Integer, primary_key=True)
     # obrigatório
     # deu erro TypeError: Additional arguments should be named <dialectname>_<argument>, got 'nullble' 
     # correto é nullable
     name = db.Column(db.String(150), nullable=False)
     price = db.Column(db.Float, nullable=False )
     # text não tem limitação de caracteres como string
     # opcional
     description = db.Column(db.Text, nullable=True )

#criar bd - ctrl j (terminal) - python -m flask shell - ir para docm/seque.md



#---- Endpoints/rotas raiz da pag inical e a função/ verbo a ser executado ---

#raiz geralmente é uma barra
@app.route("/")
# função a ser executada
def hello_world():
    return " ✮⋆｡°✩⋆˙ Saluton Mondo!⋆⁺₊⋆ ☾⋆⁺₊⋆ "

#rota POST product - new product/novo produto

@app.route("/api/products/add", methods=["POST"])
# se quiser aceitar mais de uma método só por , e outro método "POST", "GET"
#SNACKCASE n_p
#payload = corpo de requisição, dados enviados para API, servidor com rota POST ou PUT - será formato json com chave e valor
def add_product():
    #recuperar dados
    #request vem do flask
    data = request.json
    #criando produto e savando na variável product
    # Product é da classe criada anteriormente
    #nome=data["name"] - pega variável data, e dentro é o valor da chave de acesso do dict
    # método.get recupera a chave
    # 1° método se não achar dá erro, no segundo se não achar retorna valor que por dentro do parenteses "None"
    product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
    #add no db
    db.session.add(product)
    db.session.commit()
    return "201 - produto cadastro"
# ir passo 4 docm/seque.md

#----------------------------------

#para subir
#Debug = ativa apuração que ajuda a receber infromações sobre o servidor - SÓ USA NO DESENVOLVIMENTO - EM PRODUÇÃO DEIXA FALSO
#Se conteúdo da variável name for main, roda
if __name__=="__main__":
    app.run(debug=True)
    
    