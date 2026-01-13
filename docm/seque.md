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

1.1 -  transformar todas as class (modelagens) em tabelas
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- não tem retorno no terminal

<span style="color: #ff8922;">db.create_all()</span>

1.2 - session = propriedade do db que armazena conexação com banco
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- commit() - método que armazena as mudanças
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- não possui retorno no terminal

<span style="color: #ff8922;">db.session.commit()</span>

1.3 sair do bd do ternimal, flask shell

<span style="color: #ff8922;">exit()</span>

1.4 aparecerá uma pasta chamada instance, como arquico ecommerce.db

Para visualizar o arquivo: extensão SQLite viewer 