<h1>SEquencia de criação</h1>

1° requirements.txt  que fica na pasta mãe

2° app.py

3° bd no ternimal

python -m flask shell - ir 
retorno
Ctrl click to launch VS Code Native REPL
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
App: app
Instance: C:\Users\arfur\Documents\python_geral\rocketseat_py_flask\instance

digitar

3.1 -  transformar todas as class (modelagens) em tabelas
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- não tem retorno no terminal

<span style="color: #ff8922;">db.create_all()</span>

3.2 - session = propriedade do db que armazena conexação com banco
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commit() - método que armazena as mudanças
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- não possui retorno no terminal

<span style="color: #ff8922;">db.session.commit()</span>

3.3 sair do bd do ternimal, flask shell

<span style="color: #ff8922;">exit()</span>

3.4 aparecerá uma pasta chamada instance, como arquico ecommerce.db

Para visualizar o arquivo: extensão SQLite viewer 

4 - criar rota post
aba enviroment - new - + - no bloco lateral em new environment por API_enviroment_local (esta parte não deu certo para mim então vou na raça)

new - http - escolher método - neste caso post -
http://127.0.0.1:5000/api/products/add
 (aqui só rodar o app.py que aparece o localhost e depois só completar com endpoint criado)

 body - raw - json

 {
    "name": "TV",
    "price": 5999,
    "description": "TV 4k branca smartTV"
}

send

retorno 200 ok + no body o corpo payload criado

5° ir para ecommerce.db - verá o produto celular criado, que ficará fixo