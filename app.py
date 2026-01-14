# Da biblioteca flask traga a classe Flask
from flask import Flask, request, jsonify
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
    # 1° erros depois acerto
    # aqui para verificar se há chave no payload
    # no payload ficaria so com price e description, por exemplo, sem linha do name
    if "name" not in data or "price" not in data: 
        return ({"error": "Name ans price are required"}), 400
    # aqui para verificar o valor, obervar que a chave está dentro do colchete, porque é o valor desta chave que quero receber, não a chave em si
    # não possui in porque já foi analisado existência de chave, então não tem erro KeyError
    # is None depois de price porque ele é número, e zero é valor, então deve ser nulo para dar erro. Já name é retorno de true ou false, não precisa de adiconais de comparação
    # no payload ficaria "name": "", ou price: Null
    if not data["name"] or data["price"] is None: 
        return ({"error": "Invalid data"}), 400
        #criando produto e savando na variável product
    # Product é da classe criada anteriormente
    # verificar dados - tratamento erro
    # verfica se a chave está no data
    if "name" in data and "price" in data:
        #nome=data["name"] - pega variável data, e dentro é o valor da chave de acesso do dict
        # método.get recupera a chave
        # 1° método se não achar dá erro, no segundo se não achar retorna valor que por dentro do parenteses "None"
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        #add no db
        db.session.add(product)
        db.session.commit()
        # este retorno é uma tupla, dentro tem dict {} que é body, n° é status
        return {"message": "Product created"}, 201
# ir passo 4 docm/seque.md
# ir para passo 5 docm/seque.md

# deletar
# <tipo:parametro>
# vai delatar pegando id do produto
@app.route("/api/products/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    #recuperar produto
    # pesquisee pegue o id do produto da class produto
    product = Product.query.get(product_id)
    #verificar se é válido, existe
    # if product != None: se produto for diferente de None, o que significa SE PRODUTO É VALIDO if product
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product Deleted"}), 200
    return jsonify({"error": "Failed to delete product"}), 404
    
#Recuperar detalhes
@app.route("/app/products/")
    
    
    
#----------------------------------

#para subir
#Debug = ativa apuração que ajuda a receber infromações sobre o servidor - SÓ USA NO DESENVOLVIMENTO - EM PRODUÇÃO DEIXA FALSO
#Se conteúdo da variável name for main, roda
if __name__=="__main__":
    app.run(debug=True)
    
    